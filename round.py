"""One enumeration round, TARGET_SELECTION §18/§19 — read-only, sequential, snapshotting.

    python docs/funding/round.py seed "<seed phrase>" <tag>
    python docs/funding/round.py pool <tag> <topic_id> [<topic_id> ...]
"""
import json
import sys
import urllib.parse

from enumerate import draw, POOL   # same draw(): content-addressed snapshots


def seed(phrase, tag):
    url = ("https://api.openalex.org/works?search="
           + urllib.parse.quote(phrase) + "&per-page=50")
    d, h, f = draw(url, "seed_" + tag)
    topics = {}
    for w in d.get("results", []):
        for t in (w.get("topics") or []):
            tid = t["id"].rsplit("/", 1)[-1]
            topics.setdefault(tid, {"name": t["display_name"], "n": 0})
            topics[tid]["n"] += 1
    ranked = sorted(topics.items(), key=lambda kv: -kv[1]["n"])
    print("draw", f, "| index_total", d["meta"]["count"])
    for tid, v in ranked[:6]:
        print("  ", tid, str(v["n"]).rjust(3), v["name"])


def pool(tag, topic_ids):
    rows = {}
    for tid in topic_ids:
        url = (f"https://api.openalex.org/works?filter=topics.id:{tid}"
               f"&sort=cited_by_count:desc&per-page={POOL}")
        d, h, f = draw(url, f"frame_{tag}_{tid}")
        print("draw", f, "| topic", tid, "| got", len(d.get("results", [])))
        for w in d.get("results", []):
            wid = w["id"].rsplit("/", 1)[-1]
            rows[wid] = {"id": wid,
                         "title": (w.get("display_name") or "")[:100],
                         "cited_by_count": w.get("cited_by_count"),
                         "publication_date": w.get("publication_date"),
                         "type": w.get("type")}
    out = sorted(rows.values(), key=lambda r: -(r["cited_by_count"] or 0))[:POOL]
    path = f"docs/funding/snapshots/pool_{tag}.json"
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    print("union unique", len(rows), "| pool", len(out), "->", path)
    for i, r in enumerate(out, 1):
        print(str(i).rjust(2), r["id"].ljust(12),
              str(r["cited_by_count"]).rjust(7), r["publication_date"], r["title"][:74])


if __name__ == "__main__":
    if sys.argv[1] == "seed":
        seed(sys.argv[2], sys.argv[3])
    else:
        pool(sys.argv[2], sys.argv[3:])
