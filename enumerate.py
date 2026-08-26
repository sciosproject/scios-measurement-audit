"""Enumeration for TARGET_SELECTION §18 — read-only, sequential, one request at a time.

Every raw response is stored content-addressed under docs/funding/snapshots/openalex_raw/
so a later run can never overwrite the evidence a claim rests on
(EXTERNAL_LEDGER §8: a response hash identifies a DRAW, not a claim).

Usage:
    python docs/funding/enumerate.py seed
    python docs/funding/enumerate.py frame  <topic_id>
    python docs/funding/enumerate.py check  <work_id>
"""
import hashlib
import json
import os
import sys
import time
import urllib.request

RAW = os.path.join(os.path.dirname(__file__), "snapshots", "openalex_raw")
SEED = "benchmark for evaluating language models"  # frozen in TARGET_SELECTION §18.2
POOL = 50                                          # frozen in TARGET_SELECTION §18.2


def draw(url, label):
    """One GET. Saves the raw bytes under sha256[:16]_label.json and returns parsed JSON."""
    os.makedirs(RAW, exist_ok=True)
    with urllib.request.urlopen(url, timeout=60) as r:
        body = r.read()
    h = hashlib.sha256(body).hexdigest()
    path = os.path.join(RAW, f"{h[:16]}_{label}.json")
    if not os.path.exists(path):
        with open(path, "wb") as f:
            f.write(body)
    time.sleep(1.0)  # the survey owns this machine; stay out of its way
    return json.loads(body.decode("utf-8")), h, os.path.basename(path)


def seed():
    url = ("https://api.openalex.org/works?search="
           + urllib.parse.quote(SEED) + "&per-page=50")
    d, h, f = draw(url, "seed_search")
    topics = {}
    for w in d.get("results", []):
        for t in (w.get("topics") or []):
            tid = t["id"].rsplit("/", 1)[-1]
            topics.setdefault(tid, {"name": t["display_name"], "n": 0})
            topics[tid]["n"] += 1
    ranked = sorted(topics.items(), key=lambda kv: -kv[1]["n"])
    print(json.dumps({"draw": f, "sha256": h, "results": d["meta"]["count"],
                      "topics": ranked[:8]}, ensure_ascii=False, indent=1))


def frame(topic_id):
    url = (f"https://api.openalex.org/works?filter=topics.id:{topic_id}"
           f"&sort=cited_by_count:desc&per-page={POOL}")
    d, h, f = draw(url, f"frame_{topic_id}")
    rows = [{"id": w["id"].rsplit("/", 1)[-1],
             "title": (w.get("display_name") or "")[:110],
             "cited_by_count": w.get("cited_by_count"),
             "publication_date": w.get("publication_date"),
             "type": w.get("type")}
            for w in d.get("results", [])]
    print(json.dumps({"draw": f, "sha256": h, "topic": topic_id,
                      "pool": len(rows), "rows": rows}, ensure_ascii=False, indent=1))


def check(work_id):
    """TARGET_SELECTION §16: declared count vs the list the index itself can enumerate."""
    d1, h1, f1 = draw(f"https://api.openalex.org/works/{work_id}", f"work_{work_id}")
    d2, h2, f2 = draw(
        f"https://api.openalex.org/works?filter=cites:{work_id}&per-page=1",
        f"citing_{work_id}")
    declared = d1.get("cited_by_count")
    listed = d2.get("meta", {}).get("count")
    hi, lo = max(declared, listed), max(min(declared, listed), 1)
    print(json.dumps({"id": work_id, "declared": declared, "listed": listed,
                      "factor": round(hi / lo, 2), "flag": (hi / lo) > 10,
                      "publication_date": d1.get("publication_date"),
                      "draws": [f1, f2]}, ensure_ascii=False))


def prior(work_id, name):
    """EXTERNAL_LEDGER §9.3 field 6 — prior art on this instrument's validity.
    Two frozen queries, 50 records each; the scope is part of the finding."""
    import urllib.parse
    out = []
    for tag, url in (
        ("a", f"https://api.openalex.org/works?filter=cites:{work_id}"
              f"&sort=cited_by_count:desc&per-page=50"),
        ("b", "https://api.openalex.org/works?search="
              + urllib.parse.quote(f"{name} validity evaluation")
              + "&sort=cited_by_count:desc&per-page=50"),
    ):
        d, h, f = draw(url, f"prior_{tag}_{work_id}")
        out.append({"query": tag, "url": url, "draw": f, "sha256": h,
                    "read": len(d.get("results", [])),
                    "index_total": d.get("meta", {}).get("count"),
                    "rows": [{"id": w["id"].rsplit("/", 1)[-1],
                              "title": (w.get("display_name") or "")[:120],
                              "year": w.get("publication_year"),
                              "cited_by_count": w.get("cited_by_count")}
                             for w in d.get("results", [])]})
    print(json.dumps(out, ensure_ascii=False))


if __name__ == "__main__":
    import urllib.parse
    {"seed": lambda: seed(),
     "frame": lambda: frame(sys.argv[2]),
     "check": lambda: check(sys.argv[2]),
     "prior": lambda: prior(sys.argv[2], sys.argv[3])}[sys.argv[1]]()
