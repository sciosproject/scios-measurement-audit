"""Pull the claim/scope/limitation passages out of an extracted specification text."""
import re
import sys

KEYS = ["understudy", "test corpus", "corpus", "single sentence", "individual sentence",
        "brevity penalty", "baseline", "four reference", "500 sentences",
        "judgments", "rank", "should be used", "we take", "N = 4", "uniform weights"]


def main(path, out):
    s = open(path, encoding="utf-8").read()
    s = re.sub(r"(?<=[a-zA-Z]) (?=[a-z] )", "", s)
    seen = set()
    blocks = []
    for key in KEYS:
        for m in re.finditer(re.escape(key), s, re.I):
            a, b = max(0, m.start() - 340), min(len(s), m.end() + 340)
            frag = s[a:b].strip()
            sig = frag[:80]
            if sig in seen:
                continue
            seen.add(sig)
            blocks.append("--- " + key + " ---\n" + frag + "\n")
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(blocks))
    print(len(blocks), "passages ->", out)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
