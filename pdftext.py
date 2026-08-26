"""Minimal PDF text extraction — read-only, no dependencies, negligible CPU.

Used to read a target's PUBLISHED specification so the criterion can be applied to it
by inspection (COUNTING_CRITERION gate 2: proved from the published description alone,
without re-running anything).
"""
import re
import sys
import zlib

TEXT_OPERAND = re.compile(r"\((?:[^()\\]|\\.)*\)")
ESCAPED = re.compile(r"\\([()\\])")
OCTAL = re.compile(r"\\[0-9]{1,3}")


def extract(path):
    data = open(path, "rb").read()
    chunks = []
    for m in re.finditer(rb"stream\r?\n(.*?)endstream", data, re.S):
        try:
            chunks.append(zlib.decompress(m.group(1)))
        except Exception:
            pass
    txt = b"\n".join(chunks).decode("latin-1")

    parts = []
    for frag in TEXT_OPERAND.findall(txt):
        frag = frag[1:-1]
        frag = OCTAL.sub(" ", frag)
        frag = ESCAPED.sub(r"\1", frag)
        parts.append(frag)
    return re.sub(r"\s+", " ", " ".join(parts))


if __name__ == "__main__":
    out = extract(sys.argv[1])
    with open(sys.argv[2], "w", encoding="utf-8") as f:
        f.write(out)
    print(len(out), "chars ->", sys.argv[2])
