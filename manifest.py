"""Manifest + verifier for every cited artifact under docs/funding/.

Raw draws are protected at BUILD time: their filename is their content hash, so a
different response becomes a different file and can never overwrite the support of a
claim. Derived files (pools, controls, extracted text, reports) carry ordinary names
and therefore have no such protection — they are protected at RECORD time instead, by
this manifest.

    python docs/funding/manifest.py build    # write MANIFEST.json
    python docs/funding/manifest.py verify   # recompute and fail on any drift
"""
import hashlib
import json
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "MANIFEST.json")
SKIP = {"MANIFEST.json"}

# The manifest is an INTEGRITY record. It is not a publish list, and a release must
# never be built by copying everything in it — that is how our own funding plan was
# copied into a release folder. Publication is therefore OPT-IN: anything not matched
# below is publish=false, and adding a file to the repository never makes it public.
PUBLISH = [
    "REPORT_01_WHAT_WE_EXCLUDED.md", "COUNTING_CRITERION.md", "TARGET_SELECTION.md",
    "COUNT_RESULT.md", "EXTERNAL_LEDGER.md", "ENUMERATION_ROUND_1.md",
    "ENUMERATION_ROUNDS_2_4.md", "AUDIT_T01_BLEU.md", "AUDIT_T02_COCO.md",
    "AUDIT_T03_T05.md", "cases.json",
    "snapshots/README.md", "snapshots/holdout_control_ROUGE.json",
    "snapshots/holdout_control_SQUAD.json", "snapshots/v3_websearch_SQUAD.json",
    "snapshots/directed_search_T02.json", "snapshots/prior_art_T02_COCO.json",
    "snapshots/pool.json", "snapshots/pool_r2.json", "snapshots/pool_r3.json",
    "snapshots/pool_r4.json", "snapshots/v2_titles_ROUGE.json",
]
PUBLISH_PREFIX = ["snapshots/openalex_raw/", "en/"]
PUBLISH_SUFFIX = [".py"]

# Named so a reader can see WHY, not just that it is withheld.
WITHHELD = {
    "FUNDING_PLAN.md": "internal — the project's funding position and strategy",
    "snapshots/CORRUPT_prior_W2101105183.txt": "corrupt derived file, kept as evidence",
}
WITHHELD_SUFFIX = {
    ".pdf": "third-party paper — not ours to redistribute (see SOURCES.md)",
}


def publishable(rel):
    if rel in WITHHELD:
        return False, WITHHELD[rel]
    for suf, why in WITHHELD_SUFFIX.items():
        if rel.endswith(suf):
            return False, why
    if rel in PUBLISH:
        return True, ""
    if any(rel.startswith(p) for p in PUBLISH_PREFIX):
        return True, ""
    if any(rel.endswith(s) for s in PUBLISH_SUFFIX) and "/" not in rel:
        return True, ""
    if rel.startswith("snapshots/") and rel.endswith(".txt"):
        return False, "text extracted from a third-party paper (see SOURCES.md)"
    return False, "not on the publish allow-list"


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def walk():
    for base, dirs, files in os.walk(ROOT):
        # 2026-08-27: `.git` was walked into once this became a published
        # repository, and a fresh clone reported 28 unrecorded files that were
        # git's own bookkeeping. An integrity record covers the artifacts, not
        # the machinery that transported them.
        dirs[:] = [d for d in dirs if d not in ("__pycache__", ".git")]
        raw = os.path.basename(base) == "openalex_raw"
        for name in sorted(files):
            if name in SKIP:
                continue
            rel = os.path.relpath(os.path.join(base, name), ROOT).replace("\\", "/")
            yield rel, os.path.join(base, name), raw


def build():
    entries = []
    for rel, full, raw in walk():
        d = sha256(full)
        pub, why = publishable(rel)
        e = {
            "path": rel,
            "sha256": d,
            "bytes": os.path.getsize(full),
            "content_addressed": bool(raw and os.path.basename(rel)[:16] == d[:16]),
            "publish": pub,
        }
        if not pub:
            e["withheld_because"] = why
        entries.append(e)
    doc = {
        "schema": "scios-funding/manifest/v1",
        "generated": "2026-08-26",
        "note": ("Raw draws are protected at build time by content-addressed filenames. "
                 "Derived files are protected at record time by this manifest. "
                 "Any cited file must appear here with its hash. "
                 "This is an INTEGRITY record, not a publish list: build a release from "
                 "entries with publish=true only. Publication is opt-in; anything not on "
                 "the allow-list is withheld with a stated reason."),
        "count": len(entries),
        "entries": entries,
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=1)
    ca = sum(1 for e in entries if e["content_addressed"])
    pub = sum(1 for e in entries if e["publish"])
    print("manifest:", len(entries), "files |", ca, "content-addressed |",
          len(entries) - ca, "manifest-protected")
    print("publish:", pub, "true |", len(entries) - pub, "false (withheld, each with a reason)")
    for e in entries:
        if not e["publish"] and not e["path"].endswith((".pdf", ".txt")):
            print("   withheld:", e["path"], "--", e["withheld_because"])
    print("->", OUT)


def verify():
    doc = json.load(open(OUT, encoding="utf-8"))
    have = {rel: full for rel, full, _ in walk()}
    drift, missing, added = [], [], []
    for e in doc["entries"]:
        full = have.pop(e["path"], None)
        if full is None:
            missing.append(e["path"])
        elif sha256(full) != e["sha256"]:
            drift.append(e["path"])
    added = sorted(have)
    for tag, items in (("DRIFTED", drift), ("MISSING", missing), ("UNRECORDED", added)):
        for p in items:
            print(tag, p)
    ok = not (drift or missing)
    print("verify:", "OK" if ok else "FAIL",
          f"| checked {doc['count']} | drift {len(drift)} | missing {len(missing)} |"
          f" unrecorded {len(added)}")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    {"build": build, "verify": verify}[sys.argv[1]]()
