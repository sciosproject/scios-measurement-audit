# What We Excluded, and Why

**A frozen criterion, applied unchanged to five measurement instruments we did not build.**

**This audit was performed by hand under the project's frozen rules. The project's
engines did not perform it, and no claim is made that an automated system produced these
findings.** The rules are the project's; a person applied them to published papers. This
is the first paragraph and not a footnote, because the alternative would be a claim wider
than what was verified — the exact defect this repository documents.

Start with [`REPORT_01_WHAT_WE_EXCLUDED.md`](REPORT_01_WHAT_WE_EXCLUDED.md). Everything
else in this repository exists so that you do not have to believe it.

---

## The one-line version

We wrote down, and hash-froze, a definition of a single defect — *an instrument that
cannot reach what it claims to measure* — **before** we chose anything to point it at.
Then we pointed it at the five most-relied-upon measurement instruments our enumeration
procedure could reach, and **mostly it refused to fire**.

| | Instrument | Outcome |
|---|---|---|
| T-01 | BLEU (2002) | one case |
| T-02 | Microsoft COCO (2014) | one case |
| T-03 | ILSVRC (2015) | clean |
| T-04 | PASCAL VOC (2010) | clean |
| T-05 | Cityscapes (2016) | clean |

**Three whole targets and six individual candidates were excluded for one reason: the
authors had already declared the limit themselves.** That is the finding. The two
surviving cases are secondary to it.

## What this is not

- **Not a claim that these tools are bad.** Three came out clean, and one of them
  (PASCAL VOC) does something our own report argues for and most work omits.
- **Not a claim that anything here is new.** The word "new" appears nowhere in the
  audits. Our search for prior work has a **measured recall of 0.33**; a thing being
  absent from our list is not evidence that it is unpublished, and the report says so
  in its first paragraph rather than its last.
- **Not a claim about a field.** Two findings in five audits is two findings in five
  audits. We computed what it would take to say more — 15 to 26 targets — and stopped.

## How to check us

Nothing here asks for trust. In order of increasing effort:

```bash
python manifest.py verify                    # every artifact against its recorded hash
python quotecheck.py REPORT_01_WHAT_WE_EXCLUDED.md snapshots/*.txt
python case_list_check.py                    # the defect count, re-countable
```

`manifest.py verify` should print `drift 0 | missing 0 | unrecorded 0`.

The five audited papers are **not** redistributed here, and neither is our extracted
text of them — they are not ours to give away. [`SOURCES.md`](SOURCES.md) carries each
paper's URL and the SHA-256 of both the PDF we read and the text we extracted from it,
so you can fetch your own copy and confirm it is byte-identical to ours. That is a
stronger check than accepting our copy would have been.

## Layout

| | |
|---|---|
| `REPORT_01_WHAT_WE_EXCLUDED.md` | the report |
| `COUNTING_CRITERION.md` | the criterion, frozen before anything was counted |
| `en/` | English translations of the Arabic evidence documents (the Arabic is authoritative) |
| `TARGET_SELECTION.md` | the rule for choosing targets, frozen before any target was seen |
| `AUDIT_T01…`, `AUDIT_T02…`, `AUDIT_T03_T05.md` | the five audits |
| `ENUMERATION_ROUND_1.md`, `ENUMERATION_ROUNDS_2_4.md` | how the candidate list was built |
| `COUNT_RESULT.md`, `cases.json` | our own defects, counted under the same criterion |
| `EXTERNAL_LEDGER.md` | defects found outside our own work |
| `snapshots/openalex_raw/` | every index query, saved verbatim, named by its content hash |
| `MANIFEST.json` | every artifact and its hash |

Frozen documents are never edited. Changes are appended as dated sections, and the text
above them stays as it was — including where it turned out to be wrong.

## Things we got wrong, kept in place

We think these are the most useful part of the repository, so they are not buried:

- **Our stopping rule was mathematically wrong.** It assumed we detect every defect that
  exists. We computed the corrected form, found the original was unusable, and left the
  original section unedited with a dated correction below it.
- **Our prior-work search finds one in three.** Measured against a held-out control, then
  a second protocol measured 0.33 and a third 0.00. We publish the number and constrain
  every sentence we are allowed to write because of it.
- **We broke our own text search mid-audit** and were one step from publishing a false
  finding against sound work. Section 7 of the report is about that.
- **Our enumeration was constrained by our own phrasing**, and we had written down the
  opposite diagnosis before a fourth query falsified it.
- **Ordering.** Had enumeration finished before selection, COCO and not BLEU would have
  been audited first. We say so rather than restage it.
- **The repository name says SCIOS; SCIOS did not run.** The name is the project's and
  stays, but a reader could reasonably infer an automated system produced this. It did
  not. What misleads is silence, not the name, so the disclosure is at the top of this
  file and in section 1 of the report.

## License

The text and code we wrote are released under CC BY 4.0 and MIT respectively (see
`LICENSE`). Third-party papers are neither included nor licensed here; see `SOURCES.md`.
