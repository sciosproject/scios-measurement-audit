# Audit of Target 2 — `T-02` · Microsoft COCO

> **Translation. The Arabic is authoritative and is the hashed artifact.**
> Source: `AUDIT_T02_COCO.md`.

> **The limit of this report:** our search for prior work has a measured recall of **0.33**
> against a held-out control and **0.00** for a second route. Any list of prior work here
> is **certainly incomplete**, and absence from it is **not evidence** that something is
> unpublished.

> **2026-08-26.** Criterion: `COUNTING_CRITERION.md` `af87e0bd…`, **with no letter
> changed**. The target was fixed by the mechanical ranking in `ENUMERATION_ROUNDS_2_4 §7`
> (merged count **45,804**, the highest in the eligible population).
> **Material:** `snapshots/6aae2fd953d0e833_arXiv-1405.0312.pdf` — **the published
> description alone**, without running anything and without private data.

---

## 1. What the instrument claims to measure — quoted

| Location | Text |
|---|---|
| Abstract | *"a new dataset with the goal of **advancing the state-of-the-art in object recognition** by placing the question of object recognition **in the context of the broader question of scene understanding**"* |
| §1 | *"a new large-scale dataset that addresses **three core research problems in scene understanding**: detecting **non-iconic views**…, **contextual reasoning between objects** and the **precise 2D localization** of objects"* |
| Abstract | *"we provide **baseline performance analysis for bounding box and segmentation detection** results using a Deformable Parts Model"* |

## 2. What I exclude — keeping the rule that cost me in `T-01`

| Excluded | Rule | Their own text declaring it |
|---|---|---|
| **91 categories in the abstract against 80 carrying segmentation masks in the 2014 release** (a 12% gap) | **(a)** | Appendix II: *"Our dataset contains 91 object categories; **the 2014 release contains segmentation masks for 80 of these categories**"* |
| **The `IoU ≥ 0.5` threshold** for a correct detection | **(a)** | Metrics: *"we impose the **standard requirement** that intersection over union … is at least 0.5"* — declared explicitly |
| **"Recognizable by a 4 year old"** without measurement | **(a), partly** | Appendix II records that categories were derived in part from *"a free recall experiment with young children"* — so a basis is stated |

> **Exclusion (a) cuts here as it cut in `T-01`.** And note what that means: **the 91→80
> gap is the first thing that leaps to the eye, and it does not enter our portfolio,
> because the authors wrote it themselves.**

## 3. The case that passes both gates

### `T-02-a` — three problems claimed, published measurement for two

| Field | |
|---|---|
| **1. What the instrument claimed to measure** | Progress on **three** named problems in §1: **non-iconic views** · **contextual reasoning between objects** · **precise 2D localization** |
| **2. What it reached, with the number** | The published baseline analysis covers **two of the three**: bounding box and segmentation, with **one** model family (DPM), trained on **5,000 positives and 10,000 negatives** at "default parameter settings". **And there is no published measurement for contextual reasoning — none** |
| **3. How it was exposed** | By comparing the list of three problems in §1 with the baseline section. **By inspection alone, without running.** Before any verdict |
| **4. Had it not been caught** | The number on this dataset is read as a measurement of **scene understanding** with its three problems, when it is a measurement of two. **It reversed no announced verdict** — we had no prior verdict on it |
| **5. Source** | `6aae2fd953d0e833_arXiv-1405.0312.pdf` — abstract · §1 · the baseline section |
| **6. Prior art** | §4 below |
| **Gates** | **G1 ✅** a pass criterion and an evaluation set · **G2 ✅** from the published description alone |
| **Class** | **B** — `n = 0`: narrowing the claim to what the baseline measures is **editing**, and yields a supported statement |

**And in the binding form (§11.2-1):** we do not say "COCO does not measure scene
understanding". We say: **"the instrument names three problems and publishes measurement
for two."**

## 4. The sixth field — prior art

| Route | What it found |
|---|---|
| The index protocol (100 records · draws `94d1d8760b50a915` · `b62240a6efd610fb`) | **Zero validity critiques** — consistent with its measured recall |
| A general search engine | **Abundant validity critique**: a survey of annotation errors in detection datasets · a report of **273,834 errors ≈ 37%** of annotations · critique for small objects · gender bias in captions · false negatives in image–caption association |

**And that critique is not of our case's class:** it concerns **annotation quality**, while
our case concerns **claimed scope against published measurement**.

> **I do not say our case is new.** I did not find it within the scope described above,
> **and my recall is 0.33 and 0.00**. **The word "new" does not appear in this file.**

## 5. Outcome

```
T-02  ·  COCO  ·  one case passing both gates (B)  ·  three candidates excluded under (a)
Slot 2 / 5 consumed   ·   cases found so far: 2   ·   blind: 0
```

**And under §10.6 we have reached two cases in the five.** That is the threshold at which
anything may be said about the pattern — **and it is said only in its constrained form:**

> **"Found in 2 of 5 most-relied-upon targets"** — not "endemic", and not "the field is
> broken".

**And the pattern shared by the two cases is one, and is named as it is:**

> **In both instruments, the gap is not in the arithmetic but between what is announced in
> the abstract and what is verified in the body.** `T-01`: language independence against a
> single language pair. `T-02`: three problems against measurement for two.

---

# §6 — Dated section: the directed search on `T-02-a` — conducted, and it did not find it

*(2026-08-26, under the ledger's rule on directed search. Draw `54e407a1eb322ae9`.)*

## 6.1 Why direction is permitted here when it is forbidden there

**Direction biases toward finding**, and its effect inverts with what is being established:

| Establishing | Its effect | |
|---|---|---|
| **That a defect exists** in an instrument | makes me find what I expect | ❌ **Forbidden** — G2 alone establishes |
| **That no prior work exists** | makes me find what I expect | ✅ **Required** |

> **A directed search that finds nothing is stronger evidence of absence than a blind
> search that finds nothing:** the first looked where it was likely to be, the second never
> looked where it was likely at all.

## 6.2 The query and the result

```
Directed, not a protocol:
"COCO benchmark claims contextual reasoning but no baseline metric measures
 context scene understanding scope gap"
```

**It produced no published work stating the claim of `T-02-a`.** It produced adjacent work
— out-of-context object detection, contextual reasoning as a research problem, a survey of
multimodal evaluation — **none of which says that the instrument names three problems and
publishes measurement for two.**

## 6.3 And what is not claimed

**This is not a recall measurement.** A directed search has no measured recall, **and
`0.33` is not attributed to it** in either direction. **And the word "new" does not
appear.** The form in force:

> **"We did not find it in: three protocols with measured recall 0.33 and 0.00, and one
> directed search aimed at the content of the claim itself."**
