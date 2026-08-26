# Audit of Target 1 — `T-01` · BLEU

> **Translation. The Arabic is authoritative and is the hashed artifact.**
> Source: `AUDIT_T01_BLEU.md`.

> **2026-08-26.** Criterion applied: `COUNTING_CRITERION.md` `af87e0bd…`, **in its frozen
> state and without a letter changed** (§11.1). The target was fixed by the mechanical
> procedure in `ENUMERATION_ROUND_1.md`, **before its material was examined**.
> **Material audited:** the published description alone —
> `snapshots/c0ee6aedcb674da2_P02-1040.pdf` (`sha256 c0ee6aed…`), its extracted text
> `7e9282f809127dd2`, and its passages `2fa486fbf396dbf2`.
> **Nothing was run, and no unpublished material was used** — G2 as written.

---

## 1. What the instrument claims to measure — quoted, not paraphrased

| Location | Text |
|---|---|
| Abstract | *"a method of automatic machine translation evaluation that is quick, inexpensive, and **language-independent**, that **correlates highly with human evaluation**"* |
| Abstract | *"an automated **understudy to skilled human judges** which **substitutes for them** when there is need for quick or frequent evaluations"* |
| Conclusion | *"BLEU's strength is that it correlates highly with human judgments by averaging out individual sentence judgment errors **over a test corpus**"* |

**And the specification itself** (§2.3): `BLEU = BP · exp(Σ wₙ log pₙ)` · `BP = 1 if c > r`,
`e^(1−r/c) if c ≤ r` · with a baseline of `N = 4` and uniform weights `wₙ = 1/N`.

## 2. ⛔ What I do **not** count — including the most quoted number in the paper

**Exclusion (a) of the criterion applies in the audited party's favour** (§11.2-2): **a
limit they declared in advance in their own material is not a defect.**

| Excluded | Their own text declaring it |
|---|---|
| **The score's dependence on the number of references** — the same human translator records **0.3468** against four references and **0.2571** against two (**a 35% relative gap with the measured object unchanged**) | §3: *"one must be **cautious** making even rough comparisons on evaluations with different numbers of reference translations"* — **with both numbers published** |
| **Single-sentence scores** do not match human judgement | Footnote 4: *"BLEU **only needs to match human judgment when averaged over a test corpus**; scores on individual sentences will **often vary** from human judgments"* |
| **`r`'s sensitivity to the candidate** (the effective reference length is built from the "best match length" for each candidate sentence) | The mechanism is described openly in §2.2 — **and its effect on comparing two systems is not provable by inspection, only by running. So it fails G2** |

> **I say it plainly: the most quoted number against this instrument — `0.3468` versus
> `0.2571` — does not enter our portfolio, because its own authors published it.** And a
> criterion that swallows what its subject disclosed is not a criterion.

## 3. The case that passes both gates

### `T-01-a` — claimed scope wider than published validation

| Field | |
|---|---|
| **1. What the instrument claimed to measure** | High correlation with human judgement, **independently of language** (abstract) |
| **2. What it reached, with the number** | The human validation published in this paper: **one language pair** (Chinese↔English) · **5 systems** · **500 sentences** (40 news stories) · **two judging panels of 10 each**, **not one of them a professional translator** · **250 pairs** judged |
| **3. How it was exposed** | By comparing the abstract's text with §4's text, **without running anything and without unpublished material**. Before any verdict of ours |
| **4. Had it not been caught** | "Language-independent" is read as **verified**, whereas in this paper it is **asserted**. *(The paper cites a companion work covering three language families — **and a citation to another paper is not validation inside this one**, under G2)* |
| **5. Source** | `snapshots/c0ee6aedcb674da2_P02-1040.pdf` — the abstract, and §4 "The Human Evaluation" |
| **6. Prior art** | §4 below |
| **Gates** | **G1 ✅** an estimator · **G2 ✅** provable from the published description alone |
| **Class** | **B** — `n = 0`: narrowing the claim to the scope of its validation is **editing**, requiring no longer range and no different instrument |

**And in the binding form of §11.2-1:** we do not say "BLEU does not measure translation
quality". We say: **"the published claim is wider than the validation published with it in
this paper."**

## 4. The sixth field — and the result is measured against prior art, not against zero

**The validity of this instrument has been published on before us:**

| Work | Year | Citations |
|---|---|---|
| *Re-evaluating the Role of Bleu in Machine Translation Research* (`W1489525520`) | 2006 | 623 |
| *A Structured Review of the Validity of BLEU* (`W2806532810`) | 2018 | 364 |
| *Tangled up in BLEU: Reevaluating the Evaluation…* (`W3034269545`) | 2020 | 13 |

> ## **Verdict: `T-01-a` reproduces what has been published since 2006 and 2018. It is not a discovery.**

**And the list is certainly incomplete:** our search's measured recall is **0.33** against
a held-out control, and **0.00** for a second route. **The word "new" does not appear in
this file and may not.**

## 5. The pre-declared expectation — correct

`TARGET_SELECTION §20` was written **before the material was read**: **"I expect the first
target's result to be of the 'already known' class"**. **That is what happened.**

**And the contamination is declared, not folded away:** this was not a blind finding — **I
was informed that the three reviews existed, by title, before I began**, and I read not a
letter of them. ⇒ **Recorded in the ledger as "not blind" — and only the blind kind is
strong testimony.**

## 6. Slot one of five — consumed

```
Target 1 / 5   ·   BLEU   ·   Result: a defect passing both gates, already published
```

**This does not count as a "clean" target** (a case was found), **and it does not count as
a discovery**. And under §10.6: **one case is not a pattern**, and nothing is said about
the field below two cases in the five.

## 7. What this audit taught us about our own criterion

**Exclusion (a) cut more than I expected.** Three of four candidate defects in this
instrument **were declared by its own authors**, so all three fell. ⇒ **An instrument whose
authors write down its limits honestly is nearly immune to our portfolio** — which is
**correct and intended**, and is declared:

> **Our portfolio does not measure how bad instruments are. It measures the gap between
> what is claimed and what is verified.**
> **And an instrument that declares its limits narrows that gap itself — and we say so
> about it.**

---

# §8 — Dated section: automated quote checking — and one quotation that is not contiguous in the archived text

*(2026-08-26. `quotecheck.py` run on this file against the archived text.)*

## 8.1 Result

**Five of six quotations verified automatically. One is not found contiguously** — the
conclusion quotation in §1 above.

## 8.2 The reason — and it is not in the quotation

The extracted text **has a page footnote interleaved in the middle of the sentence**:

```
…correlates highly with human judg-  [8 Crossing this chasm for Chinese-English
translation appears to be a significant challenge for the current state-of-the-art
systems.]  -ments by averaging out individual sentence judgment errors over a test
corpus…
```

⇒ **The sentence is correct in the paper and interrupted in the extraction.** Both halves
verify separately: *"BLEU's strength is that it correlates highly with human judg"* and
*"ments by averaging out individual sentence judgment errors over a test corpus"*.

## 8.3 The verdict

**§1 is not edited.** And it is said here plainly: **this file does not pass the checker
with zero exceptions, and the cause is an interleaved footnote in the extraction, not an
error in the quotation.**

> **The rule in force: what leaves the repository must pass with zero. `REPORT_01` passes
> with zero. This file is an internal working record, and its flaw is published with it.**
