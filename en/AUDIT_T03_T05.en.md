# Audit of Targets 3, 4 and 5 — ILSVRC · PASCAL VOC · Cityscapes

> **Translation. The Arabic is authoritative and is the hashed artifact.**
> Source: `AUDIT_T03_T05.md`.

> **The limit of this report:** our search for prior work has a measured recall of **0.33**
> against a held-out control and **0.00** for a second route. Any list of prior work here
> is **certainly incomplete**.

> **2026-08-26.** Criterion `COUNTING_CRITERION.md` `af87e0bd…` unchanged. Targets fixed by
> the frozen ranking in `ENUMERATION_ROUNDS_2_4 §7`.
> **Material in all three: the published description alone**, archived by hash, without
> running anything.

---

## ⚠️ 0. Before the results: **a defect in our own tool that nearly produced a false finding**

Our text-extraction tool reads text operands from the PDF's content streams. **Embedded
fonts in many papers encode the ligatures `fi`, `fl`, `ff` as a single glyph in the range
`0x01–0x1f`.** So the extracted text carries `classi\x02cation`, not `classification`.

**The effect:** any search for a word containing a ligature **returns zero in silence**.

```
Searching for "significance" in the PASCAL VOC paper   →   0 hits
It is in the paper, in the title of §6.1.2 itself.
```

> **I was one step from recording: "the abstract promises a statistical significance
> analysis and the paper does not contain the word." That is a grave error, and its source
> was my tool, not the paper.**
> **It is precisely the pattern we document: a search that cannot reach what it claims to
> search — committed by me, while auditing someone else.**

**The fix:** `find.py` — a ligature-tolerant search. **And the rule extracted: no absence
claim may be built on PDF-extracted text except with a ligature-tolerant tool.**

---

## 1. `T-03` — ImageNet Large Scale Visual Recognition Challenge

**Material:** `b8643541df1b287c_arXiv-1409.0575_ILSVRC.pdf`

### 1.1 The claim

> *"…provide a detailed analysis of the current state of the field… and **compare the
> state-of-the-art computer vision accuracy with human accuracy**."*

### 1.2 What is excluded under (a) — and the authors declared all of it in detail

| Declared | Their text |
|---|---|
| **The size of the human sample** | §6.4.1: annotator `A1` trained on **500** and labelled **1,500** test images of **100,000** (**1.5%**) ⇒ error **5.1%** |
| **A second annotator worse by two and a half times** | `A2` trained on **100** and labelled **258** ⇒ error **12.0%**, **and they published it** |
| **Ground-truth error** | *"approximately 5 out of 1500 images (0.3%) were incorrectly annotated in the ground truth"* |
| **Choice of metric** | *"all three measures of error (top-5, top-1, and hierarchical) produced the same ordering of results"* — the reason for using top-5 only is declared |
| **Significance** | *"a z-test yields a one-sided p-value of p = 0.022"* — they declared the test and its number |

### 1.3 Verdict: **clean**

> **No case passes both gates.**

**And I say why explicitly, because the temptation was real:** "human accuracy" in the
abstract is a general phrase, and the basis is **one person on 1.5% of the test set**. But
the abstract's verb is **"compare"** — and they did compare, **declaring every basis of the
comparison numerically in the body**, including the number that hurts them (`12.0%` for the
second annotator).

**The difference from `T-01`:** there the abstract claimed a **property** (language
independence) the body did not test. Here the abstract claimed an **act** (a comparison) and
performed it with full disclosure. **Whoever conflates the two manufactures a scandal, not
an audit.**

---

## 2. `T-04` — The PASCAL Visual Object Classes (VOC) Challenge

**Material:** `bda24d6d51d58815_VOC_ijcv2010.pdf`

### 2.1 The claim

> *"We review the state-of-the-art… **analyse whether the methods are statistically
> different**, **what they are learning from the images (e.g. the object or its
> context)**, and what the methods find easy or confuse."*

### 2.2 Did the paper deliver what it promised? **Yes, and with numbers**

| Promise | What is in the body |
|---|---|
| "are the methods statistically different?" | **§6.1.2 "Statistical significance of results"** · a mean-rank analysis across classes · **Figure 8** connects methods **not significantly different at `p = 0.05`** |
| "what are they learning — the object or its context?" | The correlation between object size and `AP` is **zero or negative for most classes**, from which they conclude the methods **rely on image composition and context** |

**And more than that — the paper says about its own field what we say:**

> *"A question **often overlooked** by the computer vision community when comparing results
> on a given dataset is whether the difference in performance of two methods is
> **statistically significant**."*

### 2.3 Verdict: **clean** — and something more than clean is said with it

> **No case passes both gates.**
> **This instrument does what our portfolio argues for: it declares the extent of what its
> number settles and what it does not.**
> **And that is said about it as a defect would be said.**

---

## 3. `T-05` — The Cityscapes Dataset

**Material:** `56fab90a6cf66d7f_arXiv-1604.01685_Cityscapes.pdf`

### 3.1 What is excluded under (a)

| Declared | Their text |
|---|---|
| **Geography** | *"in 50 cities, **primarily in Germany** but also in neighboring countries"* |
| **Weather** | *"We **deliberately did not record in adverse weather conditions**, such as heavy rain or snow"* — with its reason |
| **Seasons** | *"covering spring, summer, and fall"* |
| **Set sizes** | On the title page: **3,475** finely annotated train/val · **20,000** coarse · **1,525** test |

### 3.2 And their own controls

**§3.2 "Control experiments"** — they run them *"to put our baseline results below into
perspective"*, measuring the effect of downsampling on `IoU` versus `iIoU`, and **inferring
from it the importance of the instance-normalised metric** rather than assuming it.

### 3.3 And the paper's strongest inference — **hedged in its own words**

> *"the relative order of performance… is notably different than on more generic datasets
> such as PASCAL VOC. Our conclusion is that serious progress in urban scene understanding
> **may not** be achievable through such generic datasets."*

**"may not", not "cannot".** ⇒ A hedged claim that does not outrun its evidence.

### 3.4 Verdict: **clean**

> **No case passes both gates.**

---

## 4. Outcome of the five

| # | Instrument | Result | Class |
|---|---|---|---|
| `T-01` | BLEU | **case**: language independence against one language pair | B |
| `T-02` | COCO | **case**: three problems named, measurement for two | B |
| `T-03` | ILSVRC | **clean** | — |
| `T-04` | PASCAL VOC | **clean** — and declares the limits of its own number | — |
| `T-05` | Cityscapes | **clean** — declares its geography, weather and seasons, and hedges its inference | — |

```
Found in 2 of 5 most-relied-upon targets.
```

**And under §10.6: "general in the field" is not said, nor "endemic", nor any verdict about
the field.** The line above is all the five will bear.

## 5. And the real result is not the count

> **Exclusion (a) — "a limit its owner declared is not a defect" — is what governed across
> the five.**
> **It extinguished three whole targets, and three candidates in each of the two
> remaining.**
>
> **And what survived in both cases was not an error in arithmetic or in design, but a
> sentence in an abstract that reached further than the section which tested it.**

**And three of five instruments — the most relied upon in our eligible population — came
out clean under a frozen criterion that was never loosened for them.** That is **a
statement about our machine** — that it does not manufacture findings — **before it is a
statement about theirs.**

---

# §6 — Dated section: automated quote checking

*(2026-08-26. `quotecheck.py` run on this file against the archived texts.)*

**Ten of eleven quotations verified automatically.** The remaining one is the VOC quotation
in §2.2 — **and there is no error in the quotation**: the extracted text **has a figure's
axis labels interleaved** in the middle of the sentence:

```
…whether the difference in performance of two methods is statistically
[16 person 0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1 …]  significant.
```

⇒ The fragment *"A question often overlooked by the computer vision community when
comparing results on a given dataset is whether the difference in performance of two
methods is statistically"* verifies contiguously, and the following word `significant`
comes after the figure labels.

**The same rule applies:** nothing above is edited, the flaw is published with the file,
**and what leaves the repository passes with zero exceptions.**
