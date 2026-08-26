# The Target-Selection Rule

> **Translation. The Arabic is authoritative and is the hashed artifact.**
> Source: `TARGET_SELECTION.md`, sha256 `e5fca29b1a26dc85effee35f8de57b1f1ce890624eadaaf73a4e214b808b0803`.
> §1–§9 were frozen on 2026-08-26 **before looking at a single candidate**. §10 onward are
> dated amendments; nothing above an amendment is edited.

> **Why frozen first.** Whoever chooses a target **after** seeing it chooses what flatters
> them — **the exact defect the whole portfolio exists to document.** A selection rule
> written after the survey is not a rule but a justification.
> **No target is named in this file.** A name appearing here later would be a broken
> freeze.

---

## 1. Scope — frozen in advance, not widened here

The field is **AI model evaluation**. Count in the first round: **one target**. No basket
of targets from which the best result is picked.

## 2. Eligibility — testable **without** applying any part of the criterion

All are required, and all are checkable from published description alone, so that no
judgement about the outcome leaks into the choice.

| # | Condition | Why |
|---|---|---|
| **E1** | **A publicly published number** with **an explicit claim about what it measures** | Without a stated claim there is nothing for reach to be compared against |
| **E2** | **The specification is published in enough detail to apply G2** — provable from their description without re-running | Our fortress. What cannot be proved by inspection, we do not assert |
| **E3** | **A third party builds a decision on it** — cited or relied upon in a choice or an allocation | Auditing a number nobody uses is work without an audience |
| **E4** | **No connection to us** — no contribution, no benefit, no quarrel | A conflict of interest voids the verdict |

> **Deliberately not a condition: availability of data or code.** Requiring it would make
> us audit **the convenient** rather than **the consequential** — a selection bias dressed
> as rigour. **G2 works from the published description.**

## 3. The selection rule — enumerate first, then choose by a rule fixed in advance

1. **Enumerate the eligible population** (everything satisfying §2) **and publish it in
   full** — before any check.
2. **Rank it by a pre-declared adoption proxy:** the number of independent third parties
   citing or building on the number, **counted from a named public index on a named
   date**, with the count published.
3. **Take the first.** No exceptions, and no "the second suits our tools better".
4. **Exact ties only** are broken by a draw whose seed is announced beforehand.

> **Why the most-adopted rather than the easiest:** because choosing the top is **the
> opposite** of choosing what flatters us. And if it turns out sound, we will have audited
> the field's most relied-upon number and said it is sound — **a more valuable result than
> a defect in a marginal one.**

## 4. Prohibited in selection — by name

- ❌ Looking at any check result before the target is fixed.
- ❌ Choosing because of who owns it — large or small, liked or disliked.
- ❌ Substituting a target after it is fixed because the check came back empty. **An empty
  check is published.**
- ❌ Collecting several targets and publishing the most successful.

## 5. Fixing the target

The chosen target and its specification are written to a separate file **with a hash**,
**before** the two gates are applied. The date of that hash is the "first audit" to which
the funding plan's later triggers are anchored.

## 6. Three outcomes, **all of them published**

| Outcome | What is published |
|---|---|
| **A defect is found** (A or B) | The case with all five fields, **in the binding form: "their instrument carries no information about their claim" — not "their result is wrong"** |
| **None is found** | **"This measurement reaches what it claims, within the limits of what we checked"**, together with the sensitivity of our check |
| **The specification is too thin to apply G2** | Published **as a result**: "the published description does not suffice for verification" — then the next in rank is taken, **and both are published** |

**So no target is dropped in silence.** The third outcome in particular makes obscurity
expensive for its author.

## 7. Our sensitivity is declared **before** the verdict

What our instruments cannot reach is written in the report itself, not an appendix — as
we do to ourselves. **An audit that does not declare its own limit commits what it
documents.**

## 8. An expectation declared now — **a tripwire, not a test**

> **I put it at roughly 2 in 3 that we find at least one case in the first target.**

**This is a subjective prior, not a measurement.** Our own rate in our own work **is not
evidence about anyone else**, and saying otherwise would be the very conflation we
document. The number's function is **to expose the author's own drift in application, not
to judge the result.**

## 9. Freezing

This file is not edited after the enumerated list is published. Any change is a **new
dated section with its evidence**. The hash is recorded outside it.

*(Read together with §20 and §21, dated below.)*

---

## Appendix — selection clauses, for verbatim publication

> **The target is fixed before it is examined.** Eligibility is judged only from publicly
> available description: a published number, an explicit claim about what it measures, a
> specification detailed enough to be checked without re-running it, and a third party who
> builds a decision on it. Availability of data or code is deliberately **not** a condition
> — requiring it would select the convenient over the consequential.
>
> **The eligible set is enumerated and published first.** It is then ranked by a
> pre-declared adoption count from a named public index on a named date, and the
> **top-ranked target is taken**. Exact ties only are broken by a draw whose seed is
> published beforehand.
>
> **All three outcomes are published:** a defect found; the measurement found sound within
> our declared sensitivity; or the published specification found insufficient to check at
> all — reported as a result before moving to the next in rank. No target is dropped in
> silence, and no target is swapped after it is fixed because the check came back empty.
>
> **A defect, when found, is stated as "this instrument carries no information about this
> claim" — never as "this result is false."**

---

# §10 — Dated amendment: **the stopping rule** — when the hypothesis is declared falsified

*(2026-08-26, **before the first target**, after the owner noted that §6 moves to "the
next" without a bound. Setting this number after the third target would be adjusting to
fit; setting it now is pre-registration.)*

## 10.1 The defect it closes

"Move to the next" without a ceiling makes selection **selection by persistence**: anyone
who tries enough targets will find something in one of them — **and that is not evidence
that the pattern is general.** The funding plan's later trigger covers **public silence
after publication**, not **the targets themselves coming back empty**. Two different
defects; the second had no guard until now.

## 10.2 The hypothesis, stated explicitly

> **H:** "The defect we documented in ourselves is **a pattern in the field**, not a
> peculiarity of ours."

## 10.3 The window — **fixed, not consecutive**

> **The verdict is rendered on the first five checkable targets in the frozen ranking.
> Not on "five consecutive" at any point.**

**That difference is the whole point:** "consecutive" resets on the first hit, so the
attempt can be resumed indefinitely. **A fixed window does not reset** — its verdict is
published whatever it is.

## 10.4 The numbers

With the prior declared in §8 (`p = 2/3`), and with a conservative prior we do not hold
(`p = 1/2`):

| Consecutive clean | `P(zero findings \| H)` at `p=2/3` | at `p=1/2` | Verdict |
|---|---|---|---|
| 3 | **0.037** | 0.125 | ⚠️ **A published warning** |
| **5** | **0.0041** | **0.031** | ⛔ **The hypothesis is falsified** |

**Why five:** at five the probability falls below `0.05` **even under the conservative
prior we do not hold**, and below `0.01` under ours. **So the verdict does not depend on
which prior is right** — the condition for a rule that does not bend.

## 10.5 What is announced at each

- **At three clean:** **"Three most-relied-upon targets, zero cases. Our declared prior of
  2 in 3 is not holding."** A warning, not a falsification, and it stops nothing.
- **At five clean:** **H is declared falsified**, verbatim: **"The defect we documented in
  ourselves has not been shown to be a pattern in this field. The portfolio remains a
  statement about our own work, not about others'."** **And the programme stops.**

## 10.6 The affirming direction is bounded too — otherwise the rule is half a rule

**One case is not a pattern.** "The pattern is general in the field" may not be said below
**two cases in the five**. And the result is **always** stated as **"found in `k` of 5
most-relied-upon targets"** — **not "endemic", not "the field is broken".**

## 10.7 The third outcome counts in neither direction

A target whose specification is too thin to apply G2 **does not test H**, so it counts
neither as clean nor as a hit; it is published and replaced until **five checkable**
targets are reached.

> **So this does not become a back door:** if the count of third-outcome targets reaches
> **three**, that is published **as a finding in its own right**: "the published
> description in this field does not suffice for verification in three of its most
> relied-upon targets" — a result no lighter than the first.

## 10.8 The hard stop

**No sixth target is audited under this programme before the verdict on the five is
published.**

## 10.9 English — stopping rule, for verbatim publication

> **The verdict is rendered on the first five checkable targets in the frozen ranking —
> not on "five consecutive" at any point.** A consecutive counter resets on the first hit
> and licenses indefinite retrying; a fixed window does not.
>
> **Five clean targets falsify the hypothesis** that the defect class is a pattern in the
> field rather than a peculiarity of our own work, and it is then announced as falsified
> and the programme stops. Under our declared prior of 2/3 the probability of five clean
> results if the hypothesis held is 0.004; under a conservative 1/2 that we do not hold,
> it is 0.031 — below 0.05 either way, so the verdict does not depend on which prior is
> right. **Three clean targets publish an interim warning**, not a falsification.
>
> **One finding is not a pattern.** No claim that the defect is general is made below two
> findings in the five, and the result is always stated as "found in k of the 5
> most-relied-upon targets" — never as "endemic."
>
> **A target whose published specification is too thin to check counts in neither
> direction**; it is published and replaced. If three such targets accumulate, that is
> published as a finding in its own right.

---

# §11 — Dated amendment: **a positive control for the criterion on external material** — and what it does to §10

*(2026-08-26, before the first target. Born of the owner's observation that "five clean"
has a second explanation I had not ruled out — **that our criterion cannot see through
other people's material**. That is the project's own law on negative evidence, and the
lesson we paid for once already: a vetting tool never tested against a known answer threw
away **45%** of confirmed planets.)*

## 11.1 The design

**Two to three cases from outside where the measurement defect is publicly documented and
already acknowledged** — a published correction, an erratum about a metric, or a result
withdrawn for a measurement reason.

**The criterion is applied to the original published description alone — not to the
correction.**

**Contamination is declared:** I know in advance that a defect exists (that is what a
positive control is), and I must not know **which** defect it is. So before application it
is recorded: **what I knew about each case before reading its original description** — and
that is published with the result.

## 11.2 ⚠️ And what the arithmetic says: **a small control cannot establish high sensitivity**

Lower bound on sensitivity at a perfect score (`k = n`), one-sided at 95%:

| `n` | Lower bound on sensitivity |
|---|---|
| 2 | **0.2236** |
| 3 | **0.3684** |
| 5 | 0.5493 |
| 8 | 0.6877 |

> **Even 3 out of 3 establishes only that our sensitivity is ≥ 0.37.** A small control
> **rules out gross blindness; it does not establish sight.** This is written in the
> report with the number, not hinted at.

## 11.3 ⛔ And the consequence that corrects §10: **its numbers assumed sensitivity = 1**

§10.4 computed `(1−p)^N`, which tacitly assumes **we see every defect that exists**. The
correct form is `(1 − p·s)^N`. With the conservative `p = 1/2`:

| Lower-bound sensitivity `ŝ` | Per-target detection | `N` required to falsify at 0.05 |
|---|---|---|
| 1.0 (assumed in §10) | 0.500 | **5** |
| 0.5493 (from a 5/5 control) | 0.275 | **10** |
| 0.3684 (from a 3/3 control) | 0.184 | **15** |
| 0.2236 (from a 2/2 control) | 0.112 | **26** |

**The rule now frozen — the function fixed before the number is known:**

> **`N` = the smallest integer satisfying `(1 − ½·ŝ)^N ≤ 0.05`, where `ŝ` is the measured
> lower bound from the positive control.**
> **And if `N` exceeds eight, no falsification programme is run at all** — and instead is
> published: **"the reach of our criterion on external material is too weak to carry a
> verdict about the field."**

## 11.4 So what does "five clean" mean — **without ornament**

Five clean bounds the **product** `p·s` at **0.4507** (95%, zero of five). Hence
`p ≤ 0.4507 / ŝ` — **and with `ŝ = 0.37` the bound exceeds one, i.e. it is vacuous.**

> ⇒ **Five clean targets with a small control support no quantitative claim about the
> field whatsoever. They support one sentence: "we looked at the five most-relied-upon and
> found nothing, and this is our measured sensitivity."**

**§10 is not edited.** It stands with its numbers as evidence that it assumed full
sensitivity, and is read together with this section. **The value of the external programme
is the audits themselves, not an estimate of prevalence.**

---

# §12 — Dated amendment: **the adoption proxy** — its source named and recomputable

*(2026-08-26, answering the owner: a proxy that cannot be recomputed is a handle, not a
criterion.)*

**Published with the enumerated list; no ranking is accepted without it:**

| # | Published | Why |
|---|---|---|
| 1 | **The name of the public index** | Without a name there is no recomputation |
| 2 | **The query string verbatim** | A dissenter runs it themselves |
| 3 | **The date of the draw** | Counts move; without a date there is no comparison |
| 4 | **The raw count for every candidate**, not only the ranking | So it can be re-ranked, not merely believed |
| 5 | **An archived copy** with its date and hash | Our field 5, externally |

**And the tie condition is widened, because citation counts are noise, not measurement:**

> **A difference of less than 10% between first and second is a tie**, broken by a draw
> whose seed is announced beforehand.
> *(§3.4 required an exact tie — a condition that never occurs, which would make a noisy
> ranking decisive where it cannot decide.)*

**And a reference without an archived copy does not enter the portfolio.**

---

# §13 — Dated amendment: **`ŝ` is an upper bound, not an estimate** — the control sample is biased by construction

*(2026-08-26. Declared before the first target and before the control was run, not after
seeing its number.)*

## 13.1 The bias

The control is drawn from cases **whose defect is publicly documented and acknowledged**.
A defect that became known is one **somebody was able to prove** — which means **the
published description was rich enough to prove it.**

> **And thin descriptions never become "acknowledged defects", so they never enter the
> sample at all.**

⇒ **The sample is biased toward the detectable, by construction and not by accident.**

## 13.2 The consequence for the numbers

| | |
|---|---|
| `ŝ` measured this way | **An upper bound on our sensitivity, not an estimate of it** |
| The true `s` on a target drawn by rank | **Lower** |
| The true `N` required to falsify | **Larger than §11.3 computed** |

**Whenever `ŝ` is published, this sentence is published with it, not in a footnote:**

> **"`ŝ` is measured on a sample biased toward what can be detected from a published
> description. It is therefore an upper bound, and true sensitivity on an ordinary target
> is lower."**

## 13.3 And this **strengthens** the conclusion of §11.3 rather than weakening it

The ceiling `N ≤ 8` already looked tight with an optimistic `ŝ`. **Read as an upper bound
it is tighter still.**

> ⇒ **The conclusion hardens: no falsification programme is run at all, and the value lies
> in the audits themselves, not in an estimate of prevalence.**

## 13.4 A partial mitigation, applied where the material exists

If a case exists **whose defect was only exposed using unpublished material** (data or
code obtained later), it is evidence that the published description **was not sufficient**
— and our criterion **is expected to fail on it**, since G2 requires proof from the
published description alone.

**So it is included deliberately, and `ŝ` is published twice: with it and without it. The
difference between the two numbers is the measurement of the bias**, not a description of
it.

---

# §14 — Dated amendment: **the tie-breaker** — deterministic, with no hand of ours

*(2026-08-26. §12 widened a tie to "less than 10%" without saying what decides it. A tie
with no announced decider means "we choose" — the handle the whole criterion was built to
close.)*

**A deterministic two-level cascade, applied in order:**

| # | Decider | Why |
|---|---|---|
| **1** | **Earliest public appearance**, by the date in the named index of §12 | The longer a relied-upon number has existed, the longer decisions have been built on it — **so auditing it matters more**. The date is public and checkable |
| **2** | **Smallest identifier** in the index, byte-wise ascending | A final decider admitting neither tie nor interpretation |

## 14.1 And the seeded draw is dropped

§3.4 broke ties **by a draw whose seed is announced beforehand**. **A seed is something we
choose**, and announcing it in advance reduces the risk without removing it.

> **The cascade above leaves us no choice at all: the date and the identifier exist before
> we look, and we cannot change either.** And a decider with no hand of ours is stronger
> than a decider whose fairness we assert.

**§3.4 is not edited.** It stands, read together with this section.

---

# §15 — Dated amendment: **the index named, the query fixed** — before enumeration

*(2026-08-26, before running a single ranking query.)*

## 15.1 The index: **OpenAlex** — `api.openalex.org`

| Condition (§12) | How it is met |
|---|---|
| Named | `OpenAlex`, `https://api.openalex.org` |
| Recomputable | **Open, no account and no key**; any dissenter runs the same URL |
| Gives the adoption proxy | `cited_by_count` |
| Gives tie-decider 1 (§14) | `publication_date` |
| Gives tie-decider 2 (§14) | `id` — a stable identifier, lexicographically orderable |

> ⚠️ **It was chosen on grounds of accessibility, not on what it ranks.** Not one ranking
> query was run before this freeze; the only check performed was that the four fields
> exist (verified: `id` · `display_name` · `publication_date` · `cited_by_count`).

## 15.2 The fixed query

```
GET https://api.openalex.org/works/{openalex_id}
Fields read:  cited_by_count · publication_date · id · display_name
```

For every candidate we publish: **the raw count · the date · the identifier · the date of
the draw · the hash of the archived copy**.

## 15.3 Limits declared now, not after the result

1. **Counts move with time** ⇒ the draw date is part of the number, not a footnote to it.
2. **Index coverage is incomplete**, and this is an adoption proxy **by proxy**, not a
   direct measure of use.
3. **A measurement defined outside the literature** (a repository or a leaderboard) may
   have no index record at all.

## 15.4 And units are never mixed — the rule frozen before we know how much it costs

**`cited_by_count` is never replaced by repository stars or any count in another unit.**
Mixing two units in one ranking produces a meaningless number — **the portfolio's own
defect in a new place.**

⇒ **A candidate with no index record is listed in the published enumeration tagged
"outside the ranking index" with its reason, and is not ranked.**

> **And if the count of "outside the index" exceeds the count of the ranked, that is
> published as a limit on the method, verbatim: "the adoption proxy we chose does not see
> most of this field."** — said, not worked around by switching units after seeing the
> result.

---

# §16 — Dated amendment: **an index-consistency check** enters the rule · and the ranking's tilt declared before it

*(2026-08-26, after the index was probed rather than merely reached: a record in **first
place** contradicts itself — which is exactly the rank our rule takes.)*

## 16.1 The rule is written about the index, **with no record named**

**A rule written to exclude a record you have seen is the defect itself, not its repair.**
So no record, title or year is named here. The rule applies to **every** candidate alike,
and would apply had that record never existed:

> **Before ranking, the index is asked two things about each candidate: the declared
> citation count, and the number of works the index itself can enumerate as citing it.**
> **If they differ by more than the frozen threshold, the candidate is tagged "index
> contradiction", published with its discrepancy, and not ranked.**

**The threshold:** `INCONSISTENCY_FACTOR = 10` — **taken as-is from the probe tool, where
it was frozen in code before the result was known.** No new constant is invented: a
constant frozen in advance is stronger than one written after seeing the table *(and this
is also the project's law against new magic numbers)*.

**It is deliberately lax:** the four sound records agree to within **0.1%**, so "ten times"
does not catch ordinary indexing lag — **it catches only outright contradiction.**

## 16.2 And a limit on the rule itself

**If more than half the candidates are tagged "index contradiction", nothing is ranked and
no target is chosen**; instead is published: **"the index we chose for ranking is
inconsistent with itself across most of our eligible population"** — a result about our own
instrument, said and not worked around by switching indexes.

## 16.3 ⚠️ The ranking's tilt — declared **before** enumeration, not after

`OpenAlex` indexes **scholarly works**. If the most relied-upon numbers in this field live
in **leaderboards, repositories and technical reports** that are poorly indexed, then:

> **Our ranking tilts toward paper-shaped measurements and underweights what industry
> actually relies on — by construction, not by accident.**

§15.4's clause catches this **after it happens**; this section declares **its direction
beforehand**. ⇒ **This sentence is published with any ranking we issue, whether or not the
tilt shows up in the numbers.**

---

# §17 — Dated amendment: the residual bias in `ŝ` — **the class that can never be sampled**

*(2026-08-26. §13.4 proposed a mitigation that measures the bias; it does not remove it.)*

The class **"a defect that exists, that nobody found and nobody acknowledged"** is absent
from **every possible positive control** — not through weakness of design but **by
definition**: what is not known cannot enter a sample of the known.

> ⇒ **`ŝ` remains an upper bound even after the §13.4 mitigation.** The mitigation measures
> **part** of the bias (what required unpublished material to expose) and does not reach
> the part that has no sample.

**This sentence is published wherever `ŝ` is mentioned.** *(It is the project's own law on
negative evidence, applied to ourselves: a negative from a machine whose reach over the
unknown was never measured is not evidence of absence.)*

---

# §18 — Dated amendment: **the enumeration procedure** — declared before it is run

*(2026-08-26. §3.1 required "enumerate the eligible population and publish it" without
saying **how** — a gap in my own criterion, closed before enumeration rather than after.)*

## 18.1 The defect at the entry point

**Every enumeration needs an entry point, and every entry point we choose is a handle.**
There is no escape from that — **what is available is to declare the handle and shrink it**,
not to pretend it is absent.

## 18.2 The procedure — three steps, fixed now

| # | Step | Handle |
|---|---|---|
| **1** | **A verbal seed:** one text query with a phrase **published verbatim** | ✋ **our words** — the largest handle in the procedure, and it is declared |
| **2** | **The frame is handed to the index's classification:** the `topics` the index assigned to the seed's results are read, and **the most frequent** is taken as the frame | ✅ **their taxonomy, not our words** |
| **3** | **The population:** all works in that frame ranked by `cited_by_count` descending, first **50** | ✅ mechanical |

**And the seed is not chosen after seeing its results:** it is fixed here before being run,
and published even if it returns something poor.

```
Seed (verbatim):  benchmark for evaluating language models
```

## 18.3 Then E1–E4 are applied to every candidate, **and every rejection is published with its reason**

Most of the population will fall — **expected and intended**: a **model** paper reports
numbers; a **measurement** paper claims to **measure** something. **E1 separates them**,
and the differences are not folded away in silence.

## 18.4 And the procedure's limits, declared before its result

1. **It inherits the index's coverage** and the tilt declared in §16.3 toward paper shape.
2. **It inherits our verbal seed** — another phrase yields another frame.
3. **`50` is a declared ceiling**, not an exhaustive enumeration. ⇒ **"the eligible
   population" means: what this procedure reached, not what exists in the world.** And it
   is published in those words.

---

# §19 — Dated amendment: **a tie in the frame** — take the union, not one of them

*(2026-08-26. Written **after** running the seed and **before** the frame query. The seed
produced a tie §18.2 had not anticipated: two topics with identical frequency — `T10028`
and `T10181`, each in **31** of 50.)*

## 19.1 The rule

> **On a tie in the frame, take the **union** of the tied topics, not one of them.**

## 19.2 Why §14's decider does not apply here

§14 is built for a tie among **candidates**, and it is a decider that **excludes**. Excluding
half the frame by a lexicographic draw **loses coverage for no methodological reason** —
and this tie is not a competition but an **overlap**: one work carries several topics, so
the two topics describe the same material from two sides.

## 19.3 And why this is not choosing after seeing

**The union widens, and widening is the direction that cannot be gamed:** adding candidates
cannot bring a particular target closer, whereas **exclusion** always can.

> **And I say it plainly:** had I applied "smallest identifier" I would have obtained
> `T10028` (**Topic Modeling**) — a frame **further** from our field than `T10181`. **And
> preferring the second because it suits better is precisely the defect.** So I did not,
> and took both.

## 19.4 The population

`cited_by_count` descending across the union, deduplicated, **first 50**.

---

# §20 — Dated amendment: **my expectation for the first target** — written before reading its material

*(2026-08-26. Written now because an expectation written after reading is not an
expectation.)*

> **I expect the first target's result to be of the "already known" class: a reproduction
> of something published, not a new finding.**

**And the contamination is declared, not hidden:** the working window informed me that
three published reviews of this instrument's validity exist (2006 · 2018 · 2020) with
their citation counts. **So my expectation is not blind**, and rests on that notification.
**I have not read a letter of them, and I will draw and archive them myself** under the
sixth field rather than accept them second-hand.

## 20.1 And this is a legitimate result that consumes one of the five slots

**No rule is softened for it, and no target is swapped because of it.** The procedure is
frozen and produced this target, **and swapping it because it is well known is adjusting to
fit, by definition.**

## 20.2 And if the opposite arrives

Then it arrived **after the expectation was declared against it**, which is stronger
testimony — and it is read only in the binding form: **paired with the search scope that
failed to find it.**

---

# §21 — Dated amendment: **the procedure's yield and the round schedule** — estimated now, not discovered after the third target

*(2026-08-26.)*

## 21.1 The measured yield

```
Round 1:   50 candidates  →  3 eligible      =  6%
Required for the §10 window:  5 checkable targets
Short by:                     2
```

## 21.2 The estimate — with its upper bound declared

At 6% **if rounds were independent**, one further round suffices. **But they are not
independent:** a new seed in the same field yields an overlapping frame, **so the count of
newly unique eligible items is below three.**

⇒ **I estimate two further rounds, and plan for three.**

## 21.3 And a rule frozen now so it is not discovered late

> **If the eligible population has not reached five after three further rounds, that is
> published as a result in its own right:**
> **"our enumeration procedure does not reach five qualifying measurement instruments in
> this field" — a statement about our procedure, not about the field.**

**And five is not reduced to three because three is what is available.** The §10 window is
fixed; **what moves is our admission that we did not reach it.**

## 21.4 And every round under the first round's conditions

A seed **fixed and published before it is run** · every round published **whatever it
yields, even zero** · **and no seed is chosen because its predecessor did not bring what we
wanted.**

---

# §22 — Dated amendment: **§16 is blind to splitting** — the limit declared, the guard added

*(2026-08-26. Measured on the two records found in the external ledger §10.3:
**`W3034269545`** declares 13 and lists 14 (`×0.93`), and **`W4287758755`** declares 3 and
lists 3 (`×1.00`) — the same work, recorded twice. **Both are internally consistent, and
both are wrong.**)*

## 22.1 The limit — published verbatim with any list

> **§16 catches inflation (declared ≫ listed) and is blind to splitting (one work across
> several records, each internally consistent).**

**And the direction of harm is the opposite of what the guard was built for:** inflation
lifts a record to the top **where the guard sees it**; splitting pushes a work **down**, so
**it leaves the population in silence** — untagged, uncounted, unnoticed.

## 22.2 The guard — defined now, not after we see who benefits

> **Before ranking: a work whose title matches another work's title in the index is tagged
> "split record", its counts are summed, and the fact that they were summed is published
> along with which records.**

## 22.3 And it was run on round one's eligible set — with this result

| Candidate | Records with the same title | Count after merging | Draw |
|---|---|---|---|
| `W2101105183` BLEU | **1** | 21,925 (unchanged) | `19665aa6c6feb81c` |
| `W2154652894` ROUGE | **1** | 8,301 (unchanged) | `8285f39f923b21e4` |
| `W2963748441` SQuAD | **2** — with `W2427527485` (823 · 2016) | **7,243** ← was 6,420 | `d7e46d922b718217` |

> **The guard fired on its first run: SQuAD was split, and its true count is 823 higher.**

## 22.4 And its effect on the ranking: **none — and that is said**

```
BLEU 21,925   >   ROUGE 8,301   >   SQuAD 7,243
ROUGE↔SQuAD gap after merging = 12.7%   ⇒  above the 10% tie band, so no tie
```

**The first target did not change.** The guard **moved a number and did not move a verdict**
— and it is published that way, so a silent effect is not read as a check that was skipped.

*(And the guard's own limit is declared: it catches **title matches** only. A work split
under two different titles remains invisible.)*

---

# §23 — Dated amendment: **what "the five" means now** — five audits, not a statistical window

*(2026-08-26. A necessary correction after my own arithmetic killed the falsification
programme.)*

## 23.1 The falsification programme is dead — by our arithmetic, not anyone else's

§10.4 built falsification on `(1−p)^N`, i.e. on sensitivity = 1. §11.3 corrected it to
`(1−p·s)^N`, and §13 measured: **the required `N` falls between 15 and 26 targets**
depending on `ŝ`. **And §11.3's ceiling is eight.**

> ⇒ **No falsification programme is run at all. The verdict is in force and written.**

## 23.2 So what are the five

> **Five audits, not a statistical window.** They carry no `p`, no `α`, and no verdict
> about the field. They carry one thing: **five occasions on which a frozen criterion was
> applied to an instrument we did not build, with the results published whatever they
> were.**

**And §10.6 remains in force:** one case is not a pattern; "general in the field" is not
said below two; and the result is always stated as "`k` of 5 most-relied-upon targets".

## 23.3 And the number is frozen in both directions

| ❌ | Why |
|---|---|
| **Not reduced to three** | because three is what is available — that is tailoring the criterion to the supply |
| **Nor extended to six or more** | because we did not find what we wanted — **that is exactly the persistence §10.3 forbade** |

**Five stays five, and its yield is published as it comes.**

---

# §24 — Dated amendment: **the seeds for rounds 2 and 3** — fixed together before either is run

*(2026-08-26. Written **together** deliberately: had the second been announced alone and
the third chosen after seeing its yield, that would have been choosing after seeing.)*

```
Seed 2 (verbatim):  evaluation metric correlation with human judgment
Seed 3 (verbatim):  benchmark dataset for measuring model performance leaderboard
```

## 24.1 A declared adaptation — and I do not hide it

Round 1 taught me that **E1 drops model papers and keeps measuring instruments** (47 of 50
fell). **The two seeds above are aimed explicitly at measuring instruments because of that
lesson.**

> **So this is not a blind draw, and I say so.** But the bias runs toward **yield**, not
> toward **any particular target**: a seed that surfaces more measuring instruments brings
> no specific instrument closer or further. **And selection after that is entirely
> mechanical.**

## 24.2 The remaining conditions unchanged

Same procedure (§18.2): seed ⇒ index topics ⇒ union on a tie ⇒ first 50 ⇒ E1–E4 ⇒ §16 ⇒
§22 ⇒ ranking. **And every round is published whatever it yields, even zero.**

---

# §25 — Dated amendment: **the fourth seed** — a test of a diagnosis, not a hunt for targets

*(2026-08-26, **after** the yields of rounds 2 and 3 were seen. I declare that first: this
seed was not fixed with its predecessors, and I write it knowing they returned zero.)*

## 25.1 Why it is permissible at all

**The frozen budget of §21.3 is three further rounds, and two have run.** So this round's
authority comes **from the budget written in advance, not from the disappointment of the
yield.**

## 25.2 And what it tests is not "will we find a target" but **a falsifiable diagnosis**

Three verbally different seeds ended at **the same two topics**:

```
Seed 1:  T10028 (31)  ·  T10181 (31)     an exact tie
Seed 2:  T10181 (29)  ·  T10028 (28)
Seed 3:  T10028 (26)  ·  T10181 (20)
```

> **The diagnosis: the constraint is not our phrasing but the index's classification.
> Whatever our phrase, the index returns us to the same two topics.**

**And the fourth seed is aimed deliberately at another region of the taxonomy** — not
because it is more promising in targets, but because it **falsifies the diagnosis or
confirms it**:

```
Seed 4 (verbatim):  image classification benchmark accuracy evaluation dataset
```

| Result | What it means |
|---|---|
| Returns to `T10028/T10181` | **The diagnosis is confirmed**: the index returns us where it pleases |
| Produces other topics | **The diagnosis is falsified**: the constraint was in our seeds, not in the taxonomy |

**In either case the yield is published as it comes, and the verdict on the diagnosis is
part of the report.**
