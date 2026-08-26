"""Print passages around a key from an extracted spec, ASCII-safe for a Windows console."""
import re
import sys


def main(path, keys, width=330, limit=3):
    s = open(path, encoding="utf-8").read()
    for k in keys:
        for m in list(re.finditer(re.escape(k), s, re.I))[:limit]:
            a, b = max(0, m.start() - width), min(len(s), m.end() + width)
            frag = s[a:b].replace("\n", " ")
            frag = frag.encode("ascii", "replace").decode("ascii")
            print("### " + k)
            print(frag[:660])
            print()


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
