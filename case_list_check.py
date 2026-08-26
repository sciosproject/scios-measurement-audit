"""Is the defect count re-countable by a stranger? — the mechanical half.

WHAT THIS CAN AND CANNOT DECIDE.

The portfolio's counts (A = out of reach, B = aimed elsewhere) are a HUMAN reading
of frozen prose criteria. No program derives them, and this one does not pretend
to: `classification_is_human_judgement` is true in the case list and is checked
here so nobody can quietly flip it later.

What a program CAN decide is whether the count is re-countable — whether a hostile
reader who disagrees with one classification can go to the source, check it, and
redo the arithmetic. That is the whole promise the portfolio rests on, and it is
mechanical: every citation must resolve, every case must carry the number that
field 2 requires, no case may be counted twice, the totals must add up, and the
criterion the list claims to follow must be the criterion actually on disk.

WHY IT IS NOT ENOUGH TO PROMISE THIS.

The number "17" survived for weeks as a prose tally because nothing checked it.
Its replacement must not be trusted for the same reason its predecessor was — that
someone careful said so. The counting window ran these checks itself before
delivering and caught one of its own cases attributed to a line with no number in
it. That is the point: the machine catches what a careful reader misses, twice
over.

The five checks the counting window specified are implemented here verbatim. Six
more are added, and they are marked, because a validator written entirely to its
author's specification only tests what its author already thought of.
"""
import argparse
import hashlib
import json
import os
import re
import sys

#: Works from the working tree and from a published release alike. 2026-08-27:
#: the release README told a reader to run this file and it was not shipped, and
#: when shipped it pointed at an absolute path that exists only on one machine.
#: A checker a reader cannot run is a checker that does not exist.
_HERE = os.path.dirname(os.path.abspath(__file__))
if os.path.exists(os.path.join(_HERE, "cases.json")):
    ROOT, CASES = _HERE, os.path.join(_HERE, "cases.json")
else:
    ROOT = "c:/a"
    CASES = os.path.join(ROOT, "docs", "funding", "cases.json")

#: The exclusion codes frozen in COUNTING_CRITERION §4 and §2. An excluded case
#: citing anything else is using a reason that was invented after the freeze.
FROZEN_RULES = {"a", "b", "c", "d", "e", "gate1", "gate2"}


def _lines(path):
    with open(os.path.join(ROOT, path), encoding="utf-8") as fh:
        return fh.read().splitlines()


def _sha256(path):
    with open(os.path.join(ROOT, path), "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def run(path=CASES):
    with open(path, encoding="utf-8") as fh:
        d = json.load(fh)
    cases, excluded = d["cases"], d.get("excluded", [])
    tot = d["totals"]
    fails, cache = [], {}

    def lines_of(f):
        if f not in cache:
            try:
                cache[f] = _lines(f)
            except Exception:
                cache[f] = None
        return cache[f]

    # 2026-08-27, found in the final pre-publication check. The 31 cases cite
    # this project's internal working documents (docs/plan/*.md), which are NOT
    # published with the release: they contain unpublished scientific work. So a
    # reader outside the project can verify the STRUCTURE and the ARITHMETIC of
    # this count, and cannot resolve its citations.
    #
    # That limitation is stated rather than papered over, and it is stated by the
    # checker itself rather than left in a document a reader may not read. A
    # checker that reported "file not found" 31 times would be describing the
    # reader's situation as if it were our defect; a checker that stayed silent
    # would be claiming a verification it did not perform.
    sources_present = all(lines_of(c["file"]) is not None for c in cases)

    # ---- the five checks the counting window specified -----------------------
    for c in cases:
        ls = lines_of(c["file"])
        if ls is None:
            if not sources_present:
                continue                      # reported once, below, not 31 times
            fails.append("{}: file not found: {}".format(c["id"], c["file"]))
        elif not (1 <= c["line"] <= len(ls)):
            fails.append("{}: line {} outside {} ({} lines)".format(
                c["id"], c["line"], c["file"], len(ls)))

    for c in cases:
        if not re.search(r"\d", str(c.get("metric", ""))):
            fails.append("{}: field 2 carries no numeral: {!r}".format(
                c["id"], c.get("metric")))

    seen = {}
    for c in cases:
        key = (c["file"], c["line"])
        if key in seen:
            fails.append("{} and {} both cite {}:{}".format(
                seen[key], c["id"], c["file"], c["line"]))
        seen[key] = c["id"]

    by_class = {}
    for c in cases:
        by_class[c["class"]] = by_class.get(c["class"], 0) + 1
    for k in ("A", "B"):
        if by_class.get(k, 0) != tot.get(k):
            fails.append("class {} has {} rows but totals say {}".format(
                k, by_class.get(k, 0), tot.get(k)))
    if tot.get("A", 0) + tot.get("B", 0) != tot.get("total"):
        fails.append("totals do not add: {} + {} != {}".format(
            tot.get("A"), tot.get("B"), tot.get("total")))

    cr = d["criterion"]
    try:
        got = _sha256(cr["file"])
    except Exception:
        got = None
    if got is None and not sources_present:
        pass                                  # same reason: the source tree is absent
    elif got != cr["sha256"]:
        fails.append("criterion hash: list claims {} but {} is {}".format(
            cr["sha256"][:16], cr["file"], (got or "unreadable")[:16]))

    # ---- six added here, because a validator written only to its author's ----
    # ---- specification tests only what its author already thought of --------
    if d.get("classification_is_human_judgement") is not True:
        fails.append("ADDED: classification_is_human_judgement is not true. "
                     "The count is a human reading; a list that stops saying so "
                     "is claiming to be a measurement.")

    for c in cases:
        if c.get("class") not in ("A", "B"):
            fails.append("ADDED: {} has class {!r}, not A or B".format(
                c["id"], c.get("class")))

    ids = [c["id"] for c in cases]
    dupe_ids = {i for i in ids if ids.count(i) > 1}
    if dupe_ids:
        fails.append("ADDED: duplicate case ids: {}".format(sorted(dupe_ids)))

    for c in cases:                       # a citation to a blank line is none
        ls = lines_of(c["file"])
        if ls and 1 <= c["line"] <= len(ls) and not ls[c["line"] - 1].strip():
            fails.append("ADDED: {} cites {}:{}, which is a blank line".format(
                c["id"], c["file"], c["line"]))

    for e in excluded:                    # exclusions must be re-checkable too
        if e.get("rule") not in FROZEN_RULES:
            fails.append("ADDED: excluded case {!r} uses rule {!r}, which is not "
                         "in the frozen criterion".format(
                             str(e.get("what"))[:40], e.get("rule")))
        if not e.get("file") or not e.get("line"):
            fails.append("ADDED: excluded case {!r} has no file+line, so nobody "
                         "can check the exclusion".format(str(e.get("what"))[:40]))

    for e in excluded:
        ls = lines_of(e.get("file", ""))
        if ls is not None and e.get("line") and not (1 <= e["line"] <= len(ls)):
            fails.append("ADDED: excluded case {!r} cites {}:{}, outside the file"
                         .format(str(e.get("what"))[:40], e["file"], e["line"]))

    return d, fails, sources_present


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cases", default=CASES)
    args = ap.parse_args()
    d, fails, sources_present = run(args.cases)
    t = d["totals"]
    print("[C] defect case list — {} cases, {} excluded".format(
        len(d["cases"]), len(d.get("excluded", []))))
    print("[C] A = {}   B = {}   A+B = {}   (a LOWER BOUND, by criterion 11.3)"
          .format(t["A"], t["B"], t["total"]))
    print("[C] classification is a human reading of frozen prose: {}".format(
        d.get("classification_is_human_judgement")))
    print("[C] criterion {} @ {}\n".format(
        d["criterion"]["file"], d["criterion"]["sha256"][:16]))
    if not sources_present:
        print("[C] *** THE CITED SOURCES ARE NOT PRESENT HERE. ***")
        print("[C] These cases cite this project's internal working documents,")
        print("[C] which are not published with this release because they contain")
        print("[C] unpublished scientific work. What is checked below is the")
        print("[C] count's STRUCTURE and ARITHMETIC. Its CITATIONS cannot be")
        print("[C] resolved from this release, so this count is NOT independently")
        print("[C] verifiable by you, and it should not be read as if it were.")
        print("[C] The five external audits are a different matter entirely: they")
        print("[C] cite published papers, and SOURCES.md lets you obtain each one")
        print("[C] and confirm it is byte-identical to what we read.\n")
    if fails:
        print("[C] {} PROBLEM(S) — the count is not re-countable as it "
              "stands:".format(len(fails)))
        for f in fails:
            print("     - {}".format(f))
        return 1
    if sources_present:
        print("[C] every citation resolves, every case carries a number, nothing "
              "is counted twice, the totals add up, and the criterion on disk is "
              "the one the list claims.")
        print("[C] This does NOT say the classification is right. It says a "
              "stranger who disagrees with one can check it and redo the "
              "arithmetic — which is the only thing the portfolio ever promised.")
    else:
        print("[C] Every case carries a number, no case is counted twice, the "
              "class totals add up to the published figure, and no exclusion uses "
              "a reason invented after the criterion was frozen.")
        print("[C] Whether each citation points where it says it does is NOT "
              "checked here and CANNOT be, for the reason stated above. Do not "
              "read this result as confirming the count.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
