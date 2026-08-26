"""Ligature-tolerant search over PDF-extracted text.

WHY THIS EXISTS. `pdftext.py` reads text operands from a PDF's content streams. Many
papers embed subset fonts in which the ligatures fi / fl / ff / ffi / ffl are single
glyphs mapped to control bytes (0x01-0x1f). The extracted text therefore contains
"classi\x02cation", not "classification", and a plain search for a word containing a
ligature silently returns zero hits.

That is a search that cannot reach what it claims to search. It is documented in
docs/funding/EXTERNAL_LEDGER.md as a defect in our own tooling, found while it was
about to produce a false negative about an audited paper.

    python docs/funding/find.py <file> <query> [<query> ...]
"""
import re
import sys

LIGS = ["ffi", "ffl", "ff", "fi", "fl"]
CTRL = "[\\x00-\\x1f]"


def pattern(q):
    """A regex matching q where any ligature may appear as one control byte."""
    out, i = [], 0
    while i < len(q):
        for lig in LIGS:
            if q.lower().startswith(lig, i):
                out.append("(?:" + re.escape(q[i:i + len(lig)]) + "|" + CTRL + ")")
                i += len(lig)
                break
        else:
            out.append(re.escape(q[i]) + CTRL + "?")
            i += 1
    return "".join(out)


def main(path, queries, width=430, limit=3):
    s = open(path, encoding="utf-8").read()
    for q in queries:
        pat = re.compile(pattern(q), re.I)
        hits = list(pat.finditer(s))
        print("### %s  ->  %d hit(s)" % (q, len(hits)))
        for m in hits[:limit]:
            a, b = max(0, m.start() - width), min(len(s), m.end() + width)
            frag = s[a:b]
            frag = re.sub(CTRL, "~", frag)
            print(frag.encode("ascii", "replace").decode("ascii"))
            print()


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
