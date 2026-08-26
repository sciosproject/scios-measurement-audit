"""Repair PDFs whose text operands put one space between every glyph.

In such extractions a single space separates letters inside a word and a run of two or
more separates words. Collapse accordingly; leave normal text untouched.
"""
import re
import sys


def repair(s):
    singles = len(re.findall(r"(?<=[A-Za-z]) (?=[A-Za-z](?:\s|$))", s))
    if singles < len(s) / 40:
        return s                      # not a letter-spaced extraction
    s = re.sub(r" {2,}", "\x00", s)
    s = s.replace(" ", "")
    return s.replace("\x00", " ")


if __name__ == "__main__":
    text = open(sys.argv[1], encoding="utf-8").read()
    out = repair(text)
    with open(sys.argv[2], "w", encoding="utf-8") as f:
        f.write(out)
    print(len(text), "->", len(out), "chars ->", sys.argv[2])
