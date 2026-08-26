"""TARGET_SELECTION §22 — split-record guard: identical titles are merged before ranking."""
import hashlib
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

RAW = os.path.join(os.path.dirname(__file__), "snapshots", "openalex_raw")


def norm(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def check(wid, title):
    url = ("https://api.openalex.org/works?filter=title.search:"
           + urllib.parse.quote(title) + "&per-page=25")
    body = urllib.request.urlopen(url, timeout=90).read()
    h = hashlib.sha256(body).hexdigest()
    path = os.path.join(RAW, h[:16] + "_dup_" + wid + ".json")
    if not os.path.exists(path):
        with open(path, "wb") as f:
            f.write(body)
    d = json.loads(body.decode("utf-8"))
    key = norm(title)[:45]
    hits = [w for w in d.get("results", []) if norm(w.get("display_name")).startswith(key)]
    total = sum(w.get("cited_by_count") or 0 for w in hits)
    print(json.dumps({"id": wid, "records": len(hits), "merged": total,
                      "ids": [w["id"].rsplit("/", 1)[-1] for w in hits],
                      "each": [w.get("cited_by_count") for w in hits],
                      "draw": h[:16]}, ensure_ascii=False))
    time.sleep(1.2)


if __name__ == "__main__":
    for pair in sys.argv[1:]:
        wid, title = pair.split("|", 1)
        check(wid, title)
