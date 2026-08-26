# What We Excluded, and Why

### A frozen criterion applied to the five most-relied-upon measurement instruments we could enumerate

---

> **The limit of this report, stated before its findings.** Our search for prior work has
> a **measured recall of 0.33** against a held-out control, and **0.00** for a second
> route. Any list of prior work below is **certainly incomplete**, and the absence of
> something from it is **not evidence that it is unpublished**. We state this first
> because a report that hides the reach of its own instruments is committing the error
> it documents.

---

## 1. What this is

We froze a criterion for one specific defect — **an instrument that cannot reach what it
claims to measure** — and applied it, unchanged, to five measurement instruments we did
not build.

The criterion was written and hash-frozen **before** any target was seen. Targets were
selected by a mechanical rule over a published, enumerated candidate list, ranked by an
adoption count from a named public index with the query and date published. Every number
here is bound to a file and a line, or to an archived draw with its hash.

**This report is not about the five instruments audited.** It is about what a disciplined
criterion does when pointed at serious work — and mostly what it does is **refuse to
fire**.

**Who performed this audit.** *This audit was performed by hand under the project's
frozen rules. The project's engines did not perform it, and no claim is made that an
automated system produced these findings.* The rules below — the two gates, the two
classes, the exclusion clauses, the target-selection procedure — are the project's, and
they were applied by a person reading published papers. Not one line of the project's
discovery engines ran. We state this in the opening section rather than a footnote
because the alternative is a claim wider than what was verified, which is the exact
defect this report documents. The project's own law is explicit that a hand-built path
which bypasses the engines may not be offered as evidence that the system discovers
anything.

## 2. The result

| # | Instrument | Outcome |
|---|---|---|
| T-01 | **BLEU** (2002) | one case — claimed scope wider than published validation |
| T-02 | **Microsoft COCO** (2014) | one case — three problems named, two measured |
| T-03 | **ILSVRC** (2015) | **clean** |
| T-04 | **PASCAL VOC** (2010) | **clean** |
| T-05 | **Cityscapes** (2016) | **clean** |

**Found in 2 of the 5 most-relied-upon targets.** Not "endemic." Not a statement about
the field. Two findings in five audits is two findings in five audits.

## 3. The headline is the exclusions

**Three whole targets and six individual candidates were excluded for one reason: the
authors had already declared the limit themselves.**

Among the excluded is, in each case, the most quotable number we had:

- **BLEU** — the same human translator scores **0.3468** against four references and
  **0.2571** against two: a 35% relative swing with the measured object unchanged. The
  authors print both numbers and warn the reader. **Declared. Excluded.**
- **COCO** — the abstract says **91 object types**; the 2014 release ships segmentation
  masks for **80**. Appendix II says so. **Declared. Excluded.**
- **ILSVRC** — the celebrated human baseline rests on **one annotator labelling 1,500 of
  100,000 test images (1.5%)**, at **5.1%** error; a second annotator, less trained,
  scored **12.0%**. Both numbers, both sample sizes, and the significance test are in §6.4.1, which reads
  *"comparing the two proportions with a z-test yields a one-sided p-value of
  p = 0.022"* and concludes the result is *"statistically significant at the 95%
  confidence level"*. **Declared. Excluded — and the target came out clean.**
- **Cityscapes** — *"primarily in Germany"*, *"we deliberately did not record in adverse
  weather"*, spring/summer/fall, and the three set sizes printed on the title page.
  **Declared. Clean.**
- **PASCAL VOC** — publishes a statistical-significance analysis of the differences
  between methods (§6.1.2, p = 0.05), and writes that this is *"a question often
  overlooked by the computer vision community."* **Clean, and more than clean.**

A criterion that swallows what its subject already disclosed is not a criterion. It is a
quotation service.

## 4. The method, in one page

**Gate 1.** The defect must be in a measuring instrument: a test, an attribution or pass
criterion, a survey range or grid, a positive or negative control, an estimator, or a
sensitivity check.

**Gate 2.** The defect must be provable by comparing the specification to the object it
names, **without looking at any result** — no re-running, no private data. This is not a
restriction we accepted reluctantly. It is the reason a finding cannot be answered with
**"you ran it wrong."**

**Two classes, never one number.** *Class A* — repairing the specification alone does not
make the verdict meaningful; a longer or finer range, or a different instrument, is
required. *Class B* — repairing the specification alone does.

**Not counted, published as excluded rather than deleted:** a limit the authors declared
in advance; a defect that cannot be shown except by running; a case with no explicit
number in its source.

**A finding is stated as "this instrument carries no information about this claim" —
never as "this result is false."**

## 5. What the two findings have in common

Both are **Class B**, and both have the same shape.

**T-01 · BLEU.** The abstract claims a method *"language-independent, that correlates
highly with human evaluation."* The human evaluation published with it covers **one
language pair**, **5 systems**, **500 sentences**, **two panels of ten judges, none of
them professional translators**, **250 judged pairs**. The paper cites a companion work
covering three language families; a citation to another paper is not validation inside
this one. **This reproduces published work** — re-evaluations of BLEU's validity appeared
in **2006** (623 citations), **2018** (364), and **2020**. We are not first and do not
claim to be.

**T-02 · COCO.** Section 1 names **three** core problems the dataset addresses:
non-iconic views, **contextual reasoning between objects**, and precise 2D localization.
The published baseline covers **two** — bounding-box and segmentation detection, one
model family, 5,000 positive and 10,000 negative images at default settings. **No
published measurement corresponds to contextual reasoning.** The prior work we surfaced
on this dataset concerns a different class — annotation quality, label error rates,
demographic bias. We do not conclude ours is new; our recall is 0.33.

> **Neither finding is an error in a formula or a flaw in a design. Both are a sentence
> in an abstract that reached further than the section which tested it.**

## 6. What this measures — and it is not the quality of these tools

> **The portfolio does not measure how bad an instrument is. It measures the gap between
> what is claimed and what is verified.**
>
> **An instrument whose authors declare its limits closes that gap themselves — and is,
> by construction, nearly immune to us.**

Three of the five most-relied-upon instruments in our enumerated field came out clean
under a criterion that was frozen before we saw them and was never loosened for them.
That is a statement about our machine — that it does not manufacture findings — before it
is a statement about theirs.

## 7. We broke our own tool, mid-audit, and say so

While auditing PASCAL VOC our text extractor returned **zero hits** for the word
*significance*. The word is in the title of §6.1.2 of that paper. The extractor renders
the **fi** ligature as a control byte, so any search for a word containing a ligature
fails silently.

**We were one step from publishing "the abstract promises a significance analysis the
paper does not contain."** That would have been a false finding against sound work,
produced by *a search that could not reach what it claimed to search* — the very pattern
this portfolio documents, committed by us while auditing others.

The tool was fixed and the defect recorded. Then we found three more ways the same
extraction defeats a naive search: **one space inserted between every glyph**
(`T h e  P A S C A L`), **hyphenation across a line break** (`pri- marily`), and **the
decimal point rendered as a colon** (`p = 0 : 022`). Each returns zero hits in silence.

So the rule frozen is not "be careful". Every quotation attributed to a source in this
report is **checked by machine** against the archived text before publication, on a
normalised form that tolerates all four artifacts, with elisions treated as explicit
gaps. Quotations that are our own phrasing are printed as unchecked-by-design rather
than skipped, because a checker that quietly ignores what it cannot classify is the
defect this document is about.

**This report carries 6 attributed quotations and 0 unaccounted.** Two of our internal
working files carry one unaccounted quotation each — in both cases a page footnote or a
figure's axis labels interleave the sentence in the extracted text. Those files say so
in dated sections, and they are not what leaves the repository.

## 8. What we will not say

- **Not "endemic."** Only: *found in 2 of 5 most-relied-upon targets*.
- **Not "new."** The word appears in none of our audit files. It is prohibited unless
  paired with the search scope that failed to find the thing — and our scope's measured
  recall is 0.33.
- **Not "wrong."** Class A and Class B both say the measurement does not bear on the
  claim as stated. Neither says the claim is false.

## 9. Limits of this report

1. **Recall 0.33 / 0.00** on prior work, as stated at the top.
2. **The candidate enumeration reaches what our procedure reaches, not what exists.**
   Our first three seed phrases were all language-oriented and returned the same two
   index topics; we wrote that down as evidence the index constrained us, and a fourth
   seed **falsified our own diagnosis** — the constraint was our phrasing.
3. **Ordering.** Enumeration ran in batches, so the ranking moved underneath us: had all
   four rounds run before selection, COCO — not BLEU — would have been audited first. We
   state this rather than restage the order.
4. **Gate 2 excludes an entire defect class by design**: anything that can only be shown
   by running the instrument. Our counts are a floor, never an estimate.
5. **Five is five audits, not a statistical window.** We computed what it would take to
   falsify the hypothesis that this defect class is general, given our own measured
   detection sensitivity: **15 to 26 targets**. That is beyond our budget, so **we do not
   run a falsification programme and we claim no prevalence.** The number that killed it
   was ours.

---

## 10. The two halves of this release are not equally checkable

**The five audits cite published papers and are checkable in full.** Every quotation in
them is machine-checked against archived text, and you can fetch the same papers, extract
them yourself, and repeat the check without our copy.

**The count of our own defects is not.** Its thirty-one cases cite internal working
documents that are **not published with this release** — they carry unpublished
scientific work — so `case_list_check.py` verifies what it can and **tells you, when you
run it, that it cannot follow the citations.** What is checked there: that the list is
well-formed, that every case carries a number, that no two cases point at the same line,
and that the totals equal what we published. **What is not checked is whether each cited
line says what we say it says — and no tool we can ship will close that gap.**

We say this here rather than leaving the checker to say it alone, because a report that
claims "everything is checkable" while one of its halves is not has made a claim wider
than what it delivers. That is the defect this report is about, and it does not become
acceptable when we are the ones committing it.

---

*Every figure in this report is bound to an archived source. The criterion, the target
rule, the counting result, the case list, the enumeration rounds and all five audits are
hash-frozen; changes are appended as dated sections and nothing above them is edited. A
manifest of every artifact and its hash accompanies this report, with a verifier that
fails on any drift.*
