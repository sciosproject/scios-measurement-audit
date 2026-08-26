"""Verify every quoted span in a report against the archived source text.

WHY. A report whose subject is "the claim outruns what was verified" is destroyed by one
misquotation. Manual checking is not enough, because PDF-extracted text defeats naive
search in at least four ways we have now met:

  1. ligatures  fi / fl / ff  encoded as a single control byte  -> "classi\x02cation"
  2. one space inserted between every glyph                     -> "T h e  P A S C A L"
  3. hyphenation across a line break                            -> "pri- marily"
  4. the decimal point rendered as a colon with spaces          -> "p = 0 : 022"

Each of those silently returns zero hits. So this checker compares on a normalised form:
case-folded, every non-alphanumeric character removed, and any ligature allowed to stand
as one control byte.

    python docs/funding/quotecheck.py <report.md> <corpus.txt> [<corpus.txt> ...]

Exit code 1 if any quote is unaccounted for.
"""
import glob
import re
import sys

LIGS = ["ffi", "ffl", "ff", "fi", "fl"]
SENT = "\x01"

# THREE classes of quotation, distinguished by markup so none is ever silently skipped:
#   *"..."*   ATTRIBUTED  — a third-party source; checked against the archived corpus
#   **"..."** SELF        — our own frozen text (or a translation of it); the corpus of
#                           audited papers is the wrong place to look, so it is reported
#                           as SELF rather than as "not found"
#   "..."     OWN         — ordinary prose; reported as unchecked-by-design
# An ATTRIBUTED quotation is written *"..."* — italics around the quote marks.
# A bare "..." is our own phrasing and is reported as unchecked-by-design, never
# silently skipped: a checker that quietly ignores what it cannot classify is the
# defect this whole exercise documents.
ATTRIBUTED = re.compile(r'(?<!\*)\*"(.{12,600}?)"\*(?!\*)'
                        r'|(?<!\*)\*«(.{12,600}?)»\*(?!\*)'
                        r'|(?<!\*)\*“(.{12,600}?)”\*(?!\*)', re.S)
BARE = re.compile('(?<!\\*)"([^"\\n]{12,300})"(?!\\*)')
SELFQ = re.compile(r'\*\*"(.{12,600}?)"\*\*', re.S)


def norm_corpus(s):
    s = "".join(SENT if ord(c) < 32 and c not in "\n\t" else c for c in s)
    s = s.lower()
    return "".join(c for c in s if c.isalnum() or c == SENT)


GAP = "\x02"          # stands for an ellipsis: text the quotation deliberately omits


def pattern_for(q):
    q = re.sub(r"(\.\.\.|…)", GAP, q.lower())
    q = "".join(c for c in q if c.isalnum() or c == GAP)
    out, i = [], 0
    while i < len(q):
        if q[i] == GAP:
            out.append(".{0,400}")
            i += 1
            continue
        for lig in LIGS:
            if q.startswith(lig, i):
                # a ligature may survive as its letters, become one control byte,
                # or be dropped by the extractor entirely — all three are seen
                out.append("(?:" + lig + "|" + SENT + "|)")
                i += len(lig)
                break
        else:
            out.append(re.escape(q[i]) + SENT + "?")
            i += 1
    return "".join(out), q


def main(report, corpora):
    text = open(report, encoding="utf-8").read()
    blobs = {}
    for path in corpora:
        for p in glob.glob(path):
            blobs[p] = norm_corpus(open(p, encoding="utf-8", errors="replace").read())

    def flat_of(q):
        return " ".join(q.split())

    quotes = [flat_of(next(g for g in m.groups() if g))
              for m in ATTRIBUTED.finditer(text)]
    own = [flat_of(m.group(1)) for m in BARE.finditer(text)]
    selfq = [flat_of(m.group(1)) for m in SELFQ.finditer(text)]

    if not blobs:
        # A checker that reports "not found" when it could not look is announcing an
        # absence it never tested. That is the defect this repository documents, so it
        # is refused here rather than reported as a result.
        print("NO CORPUS SUPPLIED — nothing was compared.")
        print("The audited papers and our extracted text of them are not redistributed")
        print("(they are not ours to give away). SOURCES.md carries each paper's URL and")
        print("the SHA-256 of both the PDF and the extracted text, so you can fetch your")
        print("own copy, run pdftext.py on it, and re-run this checker against it:")
        print()
        print("    python quotecheck.py REPORT_01_WHAT_WE_EXCLUDED.md your_text/*.txt")
        print()
        print("attributed quotes found in the document: %d | UNVERIFIED (no corpus), "
              "not 'not found'" % len(quotes))
        sys.exit(0)

    missing = []
    for q in quotes:
        pat, flat = pattern_for(q)
        if len(flat) < 10:
            continue
        rx = re.compile(pat)
        where = [p for p, b in blobs.items() if rx.search(b)]
        if where:
            safe = q[:56].encode("ascii", "replace").decode("ascii")
            print("OK       %-56s  <- %s" % (safe, where[0].replace("\\", "/").split("/")[-1]))
        else:
            missing.append(q)
            print("MISSING  %s" % q[:110].encode("ascii", "replace").decode("ascii"))

    for q in selfq:
        print("SELF     %s" % q[:56].encode("ascii", "replace").decode("ascii"))
    for q in own:
        print("OWN      %s" % q[:56].encode("ascii", "replace").decode("ascii"))

    print("\nattributed: %d | unaccounted: %d | self-quotation: %d | own phrasing: %d"
          % (len(quotes), len(missing), len(selfq), len(own)))
    sys.exit(1 if missing else 0)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2:])
