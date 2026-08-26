"""Pull claim / scope / evaluation-protocol passages from an extracted specification."""
import re
import sys

KEYS = ["goal of", "we present", "baseline", "evaluat", "iconic", "91 object",
        "80 object", "intersection over union", "average precision", "detection",
        "annotat", "crowd", "limitation", "future", "in the context of",
        "state-of-the-art", "DPM", "compare"]


def main(path, out, width=300):
    s = open(path, encoding="utf-8").read()
    s = re.sub(r"(?<=[a-zA-Z]) (?=[a-z] )", "", s)
    seen, blocks = set(), []
    for key in KEYS:
        for m in re.finditer(re.escape(key), s, re.I):
            a, b = max(0, m.start() - width), min(len(s), m.end() + width)
            frag = s[a:b].strip()
            if not re.search(r"[A-Za-z]{4}\s+[A-Za-z]{4}\s+[A-Za-z]{4}", frag):
                continue                      # skip binary/garbled regions
            sig = frag[:70]
            if sig in seen:
                continue
            seen.add(sig)
            blocks.append("--- " + key + " ---\n" + frag + "\n")
            if len(blocks) > 140:
                break
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(blocks))
    print(len(blocks), "passages ->", out)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
