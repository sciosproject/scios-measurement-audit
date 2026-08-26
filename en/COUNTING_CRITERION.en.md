# The Counting Criterion

> **Translation. The Arabic is authoritative and is the hashed artifact.**
> Source: `COUNTING_CRITERION.md`, sha256 `af87e0bd7215d63d20a2d1854ce0f4e244c8470ae7b3536c7b549656933a9dd3`.
> Sections §1–§10 were frozen on 2026-08-26 before a single case was counted. §11–§14 are
> dated amendments appended afterwards; nothing above an amendment is ever edited.

> **Why it exists.** A prose tally of "17" had been carried in our documents for weeks and
> repeated three times without ever being counted. Two different counters had been merged
> into one series, one arithmetic step did not close, and a seventh entry did not exist.
> **The counting rule had never been written.** This file writes it — *before* counting,
> not after.

---

## 1. What is counted

> **A case = an instrument we built, declared to measure a particular claim, which does
> not reach it — so its output carries no information about that claim, whether it comes
> out as success or as failure.**

"Measuring instrument" is restricted to six kinds: **a test · an attribution or pass
criterion · a survey range or its grid · a positive or negative control · an estimator ·
a sensitivity check**.

**The defect is in the instrument, not in the phenomenon.** A fault in the engine or in
the physics is not part of this portfolio.

## 2. Two gates, applied in order

| | Question | If "no" |
|---|---|---|
| **G1** | Is it a measuring instrument under §1? | Out of scope (an engine defect, not a measurement defect) |
| **G2** | Is the defect provable **by comparing the specification to the object, without looking at any result**? | Excluded under §4(c) |

**G2 is not invented here.** It is the project's existing rule: **"only an error provable
without looking at the result may be corrected"**, together with its structural remedy —
a feasibility check before freezing. What that check catches in seconds is exactly what
this portfolio counts. It is promoted here from a local correction rule to a counting
rule.

## 3. The two classes — and a mechanical separator

> **The separating question:** if the **specification alone** were repaired and the run
> redone **on the same data** — with no longer range, no higher sensitivity, no different
> instrument — would the verdict become meaningful?

| | | Answer | What it is |
|---|---|---|---|
| **A** | **Out of reach** | **No** — a longer or finer range, or a different instrument, is required | The claim lies outside what the instrument can produce at all. Its verdict carries no information either way. |
| **B** | **Aimed elsewhere** | **Yes** — repaired by writing | The instrument can reach, but it was aimed at, scaled to, or labelled for something other than what it names. Its verdict carries information **about something else**. |

Both are "the test does not reach what it claims to measure" in the loose sense our
documents used. **Only A is that literally.**

### 3.1 Governing examples — classified now, before counting

| Case | Source | Class | Why |
|---|---|---|---|
| A critical bound at the **first** measured setting (2¹⁵) | 55 §24.2 | **A** | No method can pass it; the range must move |
| Survey stops at 64, phenomenon at 512 (C2) | 55 §35.1 | **A** | The survey must be extended |
| The null branch is **dead** (`if not claims: return False`) | 55 §24.2 | **A** | N0's success is not representable in the output |
| `0%` of **zero** runs read as `0.0` | 55 §30.2 | **A** | Nothing was measured ⇒ no information |
| **Unit error** in C7/C8 (`b>1` vs `1+b`) | 55 §24.2 | **B** | Fix the exponent in the text and re-read the verdict |
| **Direction label inverted** (C3) | 55 §35.2 | **B** | Relabel and it is correct |
| A world named `power` whose generator is `1000 + …` | 55 §22.1 | **B** | The instrument was aimed at a world other than the one named |

> **Note the consequence.** The last row is the candidate that explains why the source's
> own arithmetic did not close (`4+2=6 ≠ 5`). **Under this criterion it counts — in B.**
> So our count **will differ** from the source's, and the reason is written here in
> advance rather than discovered after the result.

## 4. What is not counted — named, and published as excluded rather than deleted

| | Excluded | Why |
|---|---|---|
| **(a)** | **A limit declared in advance, with no promise broken** | A rule that preceded the result, one of whose branches occurred and was announced. Example: C1 reaching the machine's memory ceiling under the pre-written rule **"extend until the response stops or memory is reached, and announce which occurred."** **A declared limit is not a defect.** |
| **(b)** | A defect in the **guarded** rather than the **guard** | Outside §1 |
| **(c)** | An implementation fault that **cannot be shown except by running** | Fails G2: a name collision, a branch that never executed, a crash |
| **(d)** | A case with **no explicit number in its source** | See §5 |
| **(e)** | The same case recorded in two documents | See §6 |

> **Rule (a) costs us cases, and that is correct.** The decisive contrast: our difference-
> imaging check **counts** because we promised it would go inside the centroid bound and
> it did not; C1 does **not** count because the rule anticipated both branches.

## 5. Mandatory fields — a case missing one is not counted

| # | Field | Condition |
|---|---|---|
| 1 | What the instrument claimed to measure | Quoted or cited |
| 2 | **What it actually reached** | **A number.** Without one ⇒ not counted (§4d) |
| 3 | How it was exposed | Which check caught it, **and whether before or after a verdict was announced** |
| 4 | What would have followed had it not been caught | With a flag: **did it actually reverse an announced verdict? yes/no** |
| 5 | Source | **File and line** |

**Fields 3 and 4 are not decoration.** The difference between "caught before the verdict"
and "reversed an announced verdict" is the difference between discipline working and luck
— and both are published as they are.

## 6. The unit of counting

> **One case = one instrument × one claim it failed to reach.**

Two instruments repaired in one section = **two cases**. One case mentioned in three
documents = **one**.

## 7. Expectation declared before counting — the count is judged against it

Following the project's practice of writing the expectation before the run:

```
A alone   :  12 — 14
A + B     :  16 — 19
```

**I expect the published pair to differ from "17" on at least one side.**

*(This shifts an earlier recorded band of `11–13` / `20–21`, for a stated reason: that
band was estimated before this criterion existed, and clauses (a) and (c) of §4 cut into
its wide end.)*

## 8. Declared contamination — the count is not blind

I read the whole numbering chain and formed an estimate **before** writing this
criterion. So the count **is not blind**, and the criterion was written after seeing the
case texts rather than before. This is declared, not hidden: its only protection is that
§3.1, §4 and §7 are **frozen now**, so any drift in classification shows up when the
count is compared against them.

## 9. The output — what is published, and in what form

1. **Two numbers, not one**: `A` and `A+B`, with the boundary named in the words of §3.
2. **Three exclusion lists published by name**: "declared limit" · "implementation fault"
   · "no number".
3. **No single blended figure, anywhere.** A blended figure with no stated boundary is
   the defect this portfolio exists to document.

> **Publishing the exclusions is what makes the count auditable:** a stranger can disagree
> with one classification and recount. A count that cannot be recounted is another claim.

## 10. Freezing

- **This file is not edited after counting begins.** Any change is a **new dated section
  with its evidence**, and the text above it stays as it was.
- **The hash** is computed on this file at freezing and recorded **outside** it — a file
  cannot contain its own hash.

---

# §11 — Dated amendment: portability · direction of bias · the limit of the expectation

*(2026-08-26, after the owner approved §1–§10 and required three additions. **Not a
letter above is edited.** Everything here was written **before** counting a single case
and before seeing any external target.)*

## 11.1 Portability — the criterion applies **verbatim** to instruments others built

**Why.** §1 restricted the definition to an instrument "**we built**", and the external
step applies the pattern to instruments others built. **A criterion that fits our own
work and is then stretched at the point of application is "adjusted after the result to
fit" by definition.** So it is frozen now.

**Applies unchanged:** both gates (§2) · both classes and their separating question (§3) ·
the exclusions (§4) · the counting unit (§6) · fields 1–4 (§5).

**The ownership condition drops out of G1:** "a measuring instrument **of ours**" ⇒ "**a
measuring instrument**", with the same six kinds. **Ownership is not part of the pattern.**

**Only field 5 changes:**

| | Internal | External |
|---|---|---|
| **5** | File and line | **The public artifact** (paper · repository · leaderboard · commit) **plus an archived copy with its date and hash** |

An external artifact changes or disappears. **A claim without a snapshot is not a claim.**

## 11.2 Three constraints for external application — also frozen now

**1. We do not say "their result is wrong". We say "their instrument carries no
information about their claim."** Class A externally means the measurement does not reach
the claim — **not** that the claim is false. Confusing the two kills the portfolio faster
than any opponent could. *(The analogue of the project's law that a negative from a blind
machine is not evidence of absence.)*

**2. Exclusion (a) applies in the audited party's favour:** a limit they declared in
advance, in their own published material, **is not a defect**, however severe — and we
look for it in their material **before** counting, not after being confronted with it.

**3. G2 externally is our fortress, not our restraint:** what is proved **from their own
published description**, without re-running, **cannot be answered with "you ran it
wrong."** Any claim that requires re-running leaves the portfolio for other work, under
its own name.

## 11.3 Direction of bias — printed in the output, not implied

Exclusions (a), (c) and (d) **cut in one direction only**. ⇒ **The published pair is a
lower bound, not an estimate.** This sentence is printed in the output verbatim:

> **"These two numbers are a lower bound.** The counting criterion excludes in one
> direction only: limits declared in advance, faults detectable only by running, and
> cases with no number in their source. **The true number for the pattern is larger, and
> we do not know by how much."**

## 11.4 The limit of the expectation (§7) — its function corrected

§7 claimed more than it can support. §8 concedes the estimate **preceded** the criterion
⇒ **the expectation is not blind, and can neither falsify nor confirm the count.**

> **Its only function is a tripwire on the author's own classification.** If the count
> lands far from `12–14` / `16–19`, that is **a signal to re-examine the application of
> §3.1** — not evidence that the count is right or wrong. The review is written with its
> result, whatever that turns out to be.

## 11.5 English delta — amends the Appendix, does not replace it

> **Portability.** Gates, classes, exclusions, counting unit, and fields 1–4 apply
> verbatim to instruments built by anyone. Gate 1 carries no ownership condition. Field 5
> becomes the public artifact — paper, repository, leaderboard, commit — **plus an
> archived copy with its date and hash**: an external artifact can change or vanish, and
> a claim without a snapshot is not a claim.
>
> **Class A, applied externally, says the measurement carries no information about the
> claim. It does not say the claim is false.**
>
> **Exclusion (a) applies in the audited party's favour:** a limit they declared in
> advance, in their own published material, is not a defect.
>
> **Both counts are a lower bound, never an estimate.** The criterion excludes in one
> direction only. The true number is larger, and unknown.
>
> **The pre-declared expectation is not blind and cannot falsify the count.** It is a
> tripwire on the author's own classification drift, and nothing more.

## 11.6 Freezing

A new hash is recorded **outside** this file. The previous hash `b172a208…` remains cited
as the state of the file before this section.

---

# §12 — Dated amendment: attribution by line · and the tripwire restated

*(2026-08-26. Under §10: **not a letter above is edited**, including §3.1 and §11.)*

## 12.1 A defect in this very file — **section numbers are not unique**

Field 5 requires **"file and line"**. §3.1 broke its own condition by citing section
numbers. In `docs/plan/55` the section numbers are **duplicated**: `§19.1–19.5` ·
`§20.1–20.6` · `§22.1` · `§23.1` · `§23.2`.

```
"55 §22.1"  →  line 710   (a defect in my design revealed by the curve)
            →  line 1072  (the test battery erred four times)   ← the intended one
```

> **This destroys the promise of §9 itself:** a stranger cannot recount if the reference
> points to two places. **This is not an amendment to the criterion but its enforcement**
> — field 5 already said so.

**Now in force:** every reference in the portfolio and in §3.1 is **a file and a line
number**. The section number remains **for reading, not for attribution**.

## 12.2 §3.1 re-attributed by line — with no change of case or class

| Case | Attribution in force | Section (for reading) | Class |
|---|---|---|---|
| Critical bound at first measured setting (2¹⁵) | `55:1194` | §24.2 | **A** |
| Survey stops at 64, phenomenon at 512 (C2) | `55:1792` | §35.3 (diagnosis at `55:1741`) | **A** |
| The null branch is **dead** | `55:1192` | §24.2 | **A** |
| `0%` of **zero** runs read as `0.0` | `55:1471` | §30.2 | **A** |
| **Unit error** in C7/C8 | `55:1193` | §24.2 | **B** |
| **Direction label inverted** (C3) | `55:1793` | §35.3 | **B** |
| A world named `power` with generator `1000 + …` | `55:1077` | §22.1, **the second one** | **B** |

**Not one classification changed. Only the attribution did.**

## 12.3 A boundary decision confirmed — checked, not assumed

The two errors at `55:1017` (§21.1) appear **merged** into row 3 of the table at
`55:1078`.

> **So they are not counted twice** (§4e), **and they remain two cases** (§6): **the grid
> instrument** (15 points at binary spacing against the catalogue's 40–64 at quarter-
> octave) and **the wiring instrument** (driving the plugin directly, bypassing the
> engine). Two instruments, two claims, two cases.

## 12.4 The duplicated section numbering itself — **not counted as a case**

It fails **G1**: a document's numbering is not one of the six kinds of measuring
instrument. **Published in the exclusions by name**, not deleted.

## 12.5 ⚠️ The tripwire — a wording correction **before** the review is written

I wrote in my report: **"the error is in my estimate, not in the count."** **That announces
the review's result before conducting it** — the pre-registration defect exactly,
committed in a document about pre-registration.

**The honest wording, and the frozen one:**

> **The preliminary `A` (16–20) lies outside the frozen expectation (12–14). The
> explanation is one of two and I do not know which: either my estimate was low, or my
> classification is drifting toward `A`. The review decides — and is written with its
> result, whatever that is, even if it returns `A` to 12.**

## 12.6 Freezing

A new hash outside the file. The previous hashes `b172a208…` then `80e6d80f…` remain
cited as the states before §11 and before §12.

---

# §13 — Dated amendment: the tripwire review — **conducted, and the answer is "both"**

*(2026-08-26, after §12.5 was frozen leaving both explanations open.)*

## 13.1 How it was conducted

Every candidate classified `A` was re-tested **against the separating question of §3
alone** — not against the descriptive sentence beside it. Reason: when the separating
question conflicts with the description, **the separator governs**; it is named as such
in the frozen text.

## 13.2 The result — **my classification was drifting toward `A`; three are corrected**

| Case | Was | Now | Why it drifted |
|---|---|---|---|
| Dead null branch `55:1192` | A | **B** | Reordering two branches is **writing**, and re-evaluating the same runs yields a meaningful verdict |
| Scale-audit key unaware of refinement `62` | A | **B** | Adding `refined` to the key is **writing** |
| R2/H2 demanding `FAR = 0` `64:165` | A | **B** | The instrument **can** produce zero exceedances (probability 0.5472). The defect is in reading the output, not in reaching it |

**One cause in all three:** I weighted the descriptive sentence ("the claim lies outside
what the instrument can produce") over the separating question. **It is broader, so it
swallowed cases that editing repairs.**

**And a fourth case split** (§6): the positive control at `65` = **thresholds set inside
the distribution of the real** (**B**, fixed by recalibration) **+ a residual sensitivity
ceiling at 76.1%** (**A**, which writing cannot fix).

## 13.3 What held as `A` without hesitation

Samples: a bound at the first measured point `55:1194` · a survey stopping at 64 with the
phenomenon at 512 `55:1792` · `0` of **zero** runs `55:1471` (because **no amount of
writing produces information from no measurement**) · a grid that cannot reach `1.68`
`63` · an estimator at `9.52` against a `≤1` requirement `64:126` · difference imaging
that stopped at `1.60–1.83` after a promise to go inside `65`.

## 13.4 The verdict

> **The answer is "both", and neither was known before the review:**
> **my estimate was somewhat low, and my classification was drifting toward `A` more.**
> The correction lowers `A` toward **13–16** — closer to the frozen expectation `12–14`
> than it was, **and still above it.** Nothing else is adjusted to narrow the gap.

**The tripwire did its job exactly:** it did not say the count was right or wrong — **it
pointed at a real classification drift, which was found and corrected.**

---

# §14 — Dated amendment: the suspicious direction, declared · and a number that settles each reclassification

*(2026-08-26.)*

## 14.1 ⚠️ The suspicious direction — I say it about my own work before an opponent does

> **The §13 review moved `A` from `16–20` to `13–16` — that is, toward my own stated
> expectation. This is precisely the direction that adjusting-to-fit produces.**

**I am not asking anyone to credit my intent. These are the reasons it is not an
adjustment, and every one is checkable:**

1. **The corrected wording was frozen before the review** — §12.5, leaving both
   explanations open in the text, after the owner pointed out that I had announced the
   result before conducting it.
2. **Every reclassification is attributed by line, reason and number** (§13.2 and §14.2)
   — **so the reader can re-examine each** and disagree.
3. **The correction did not bring the count inside the expectation.** `13–16` is **still
   above** `12–14`. An adjustment-to-fit would not have stopped short of its target.
4. **All the movement is in one direction: from `A` to `B`** — that is, **into the
   weaker-claiming class.** Adjustment-to-fit embellishes; it does not move cases into a
   less severe box.

**Whoever points at the suspicious direction in their own work first cannot later be
accused of it.**

## 14.2 The settling measure: **how many runs must be regenerated?**

The separating question of §3, restated as a count — **enforcement, not amendment**:

> **`n` = the number of runs that must be regenerated to obtain a meaningful verdict.**
> **`n = 0` ⇒ B** (editing and re-reading suffice). **`n > 0`, or a different instrument,
> ⇒ A.**

| Case | `n` | The settling number |
|---|---|---|
| `FAR = 0` in R2/H2 · `64:165` | **0** | The **same sixty nulls** are re-read; the probability of zero exceedances is `0.99⁶⁰ = 0.5472` — the instrument reaches, the reading is what is broken |
| Dead null branch · `55:1192` | **0** | **3 `N0` worlds, 100% silent** (`55:1921`). The silence is **recorded and complete**: read as `0/3` before the reordering and `3/3` after — **the data sufficed; only the reading was inverted** |
| Scale-audit key · `62:83` | **0** | The key has five components `(grid, comparator, top_m, s_star, epoch_test)`; a **sixth**, `refined=False`, is added. **Zero existing records need regenerating**, because what was written before refinement existed did measure an unrefined machine |

**By contrast, `A` with its numbers:** `64 → 512` requires a setting never measured ·
`15 → 49` points · `2 → 24` settings for C3 · `0` of **zero** runs requires a run on an
idle machine · and difference imaging requires **a different telescope**.

> **So no case is ever reclassified by a sentence — only by a number the reader can
> check.**

## 14.3 Freezing

A new hash outside the file. The previous hashes `b172a208…` · `80e6d80f…` · `c3051c4d…` ·
`6baafbf4…` remain cited as the states before §11, §12, §13 and §14.
