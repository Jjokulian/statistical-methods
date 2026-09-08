# Statistics without the given

Every number you have ever been shown was preceded by a decision nobody wrote down.

This repository is about that decision: how to find it, how to state it, and — the
part that is new — how to **test** it. The methods came out of an audit of Danish
marine monitoring and are kept here because none of them is about Denmark.

---

## 1. Nothing is given

Point at a deck of cards and ask *how many?* One deck. Four suits. Fifty-two cards.
Around 10²⁴ atoms. The question has no answer until somebody has said what counts as
**one**, and whoever said it is not in the room when the number is quoted.

Call it the **applefication assumption**: the rule that turned a continuous world into
countable things of one kind. It is present in every count, every category, every
average, and every model. It is almost never stated. And by the time the result is
`123`, it is invisible — a number looks like the least theory-laden object in a
dataset, precisely because its theory happened upstream, at counting time, and nothing
in the digit records it.

Three questions, in order, for any quantity:

1. **What is the applefication?** What was treated as one thing, one kind, one member?
2. **Is it reasonable?** Does the rule suit what the number is being used for?
3. **Is it stable?** — and this one has an empirical answer.

The first two are a century old and are not claimed here: Frege on number and sortals,
Quine's *no entity without identity*. **The third is the contribution.** Philosophy
could say the assumption is unavoidable. It had no procedure for asking whether a
particular one holds together.

---

## 2. Identity is an output, not a licence

Quine's slogan runs the wrong way for this purpose. There, identity is a
**precondition** — something you must already possess before you may quantify at all,
supplied by language, not an empirical matter. Invert it:

> **A stable boundary is what an entity is.**

Not assumed and then used. Produced, by measurement, in degrees. The question stops
being *is this a thing* — unanswerable, and always answered by convention — and
becomes *how stable is this boundary, and under what*. That has a number, and the
number can be small.

So entities come in strengths, and the honest report is the coefficient, not the noun.
This applies to the rows of your table before it applies to anything you do with them:
a row asserts that this is one thing, persisting, distinct from the next row. A lichen
is one organism or two or three. *Pando* is one aspen or 47,000 trees. A monitoring
station is one entity because a register gave it one number, though the instrument
changed, the operator changed, and the water is entirely different water.

**Assuming the entities is the same error one level down.** The right question is not
*which grouping of these things is real* but **at which level of organisation does
grouping become stable** — and that is answerable with the same machinery, applied
recursively. The level of maximal stability is itself the finding.

---

## 2b. There is no result, and there cannot be

Everything below is a **procedure**, not a test with an outcome. That distinction is
not modesty; it is structural, and getting it wrong is the most available error here —
the author made it in the session that produced this document, after building the whole
apparatus that forbids it.

**A "result" is constituted by closure.** It is the selection of one state from an
enumerated space; that is what makes a result a result. Entity-identity ranges over the
combinatorial space of boundary-stable groupings. Basket-utility ranges over
functionals, which is unbounded and not enumerable. And a new measure-space does not
*select* among existing possibilities — it **creates** states that were not previously
possibilities at all.

So the condition that makes one meaningful is the negation of the condition defining
the other. This is not a mismatch between neighbouring kinds. It is an inversion:

| | direction |
|---|---|
| a result | **reduces** possibility space to a point |
| this procedure | **generates** possibility space |

To say "the result is in" is to assert contraction of something whose mode of being is
expansion. Which places the error inside §4 rather than beside it:

> **"The result is in" is the mean, applied to the discovery process itself.**

A collapse of an open space to a point — the banned operation, one level up from
numbers — and banned for the same reason. It presupposes the states are one kind,
enumerable and commensurable, which is exactly the applefication that openness refuses.

**The machinery says so everywhere, once you look:**

- `m(t)` carries a time index because each new measure-space is another trial. **A
  quantity with a time index has no final value.**
- The residual test asks for *the sequence* — the leftover in each published version —
  and explicitly not for the current number.
- "At which level of organisation does grouping become stable" has no terminating
  answer; the level is the finding, and the next instrument can move it.
- Basket-utility is per-functional and never transfers, so there is no aggregate over
  functionals that could be "in."

### What this procedure can and cannot emit

**Not a possible output:** *"X is a real category."* *"X is not a real category."*
Any sentence of that form is not false — it has no referent, because the procedure has
no such output slot.

**A possible output:** a stability coefficient, at a stated level of organisation,
against a stated null, for a named functional, at a stated point in the accumulation
of measure-spaces. Five qualifiers, none droppable. Drop them and you have produced a
verdict, which is a different kind of object than anything this can make.

**And the failure has a recognisable shape.** A claim of this form wears the grammar of
a finding while carrying no run, no null and no number — so it cannot be checked, which
is worse than being wrong. Citations make it worse still: they make an uncomputed claim
look sourced, especially when the cited work used methods §8 marks void. That is the
exact move this document exists to catch, performed in prose, where nothing fails
loudly.

## 3. Two stabilities, two products

The same resampling yields two different things depending on **what you vary**, and
conflating them is the error everything here exists to prevent.

| Vary | Hold fixed | Yields | Reading |
|---|---|---|---|
| the **metric space** — disjoint parts of the feature space | the target | **entity-identity** | is there a thing here at all |
| the **functional of relevance** — what the category is used to predict | the features | **basket-utility** | is this category good for anything |

**Utility never transfers.** A basket is not useful; it is useful *for* something. The
same 123 official Danish water bodies carry real signal for surface oxygen saturation
and **negative** signal for fluorescence — useful and useless at once, in one dataset,
in one month, depending only on what was asked.

The cross terms are where the damage is:

|  | **identity-stable** | **identity-unstable** |
|---|---|---|
| **useful** | a real thing that also predicts — the only case that licenses the usual language | predicts your one target, dissolves under any other metric space: **a fit to your purpose, not a thing.** The most dangerous cell, because it validates |
| **useless** | a real thing, wrong tool | a drawing, used as a fact |

### The bait-and-switch

A word earns its meaning in one sense and is spent in another. *Fjord* names an
**enclosure** — true, physical, and identity-stable for salinity, because diffusion
makes it so. It is then spent to mean **homogeneity** — that measurements inside it are
interchangeable. The two are not merely different; restricted exchange **preserves**
gradients, so they are anti-correlated. The word carries the credit from the first
sense into the second, and no statistic in the report ever notices.

Watch for it in: *citizenship*, *race*, *species*, *sector code*, *diagnosis*,
*deprivation by postcode*, *the household*. Each names a real membership rule and is
spent as an attribution about what members share.

### And where they belong in an inference

Entity-identity sets a prior's **strength**, not its mean. A Beta(α, β) prior is
pseudo-counts and α+β is what it is worth in observations; pooling a basket supplies
the mean and **nothing whatever supplies the concentration**. A basket of `n` members
whose boundary reproduces at agreement `m` is worth about **`m·n` pseudo-observations,
not `n`**. Laplace's +1/+2, estimated instead of assumed.

Basket-utility is the **likelihood** — per functional, never in general. Prior
target-blind by construction, posterior target-specific by construction, estimated
from disjoint information. When a posterior fights a concentrated prior, which one is
wrong has a signature: many functionals contradicting means the boundary is wrong; one
means that functional does not live on it.

---

## 4. The ban

> **The mean is the applefication assumption in operational form.**

You can only average what you have already decided are instances of one kind. Every
mean silently asserts exactly the thing that was supposed to be under test. So it is
banned here — and the honest consequence is that **most of statistics goes with it.**

Reduce to primitives and check:

| statistic | primitives | verdict |
|---|---|---|
| mean, variance, standard deviation | sums of magnitudes ÷ count | **void** |
| Pearson correlation | means of x and y, centred products | **void** |
| intraclass correlation, ICC, F<sub>ST</sub>, ρ\* | group means, grand mean, ratio of averages | **void**, at three levels |
| **average** linkage | mean of cross-cluster distances | **void by its own name** |
| adjusted Rand index | pair counts — but its expectation is an ensemble mean and its normaliser is ½(P<sub>A</sub>+P<sub>B</sub>) | **void** |
| regression coefficients, R², t, F, ANOVA | least squares, i.e. distance from a mean | **void** |
| — | | |
| counts | counting | **survives** |
| median, quantiles, min, max, range | order statistics | **survives** |
| Kendall's τ, Spearman, rank tests | concordant vs discordant pairs | **survives** — purely ordinal, no centring |
| single / complete linkage | min, max | **survives** |
| the empirical distribution itself | the data, undigested | **survives** |

**One line of honesty.** A proportion is a mean of indicators, so it is not strictly
innocent. The defensible cut: **counting presumes only that you can tell events apart;
averaging magnitudes presumes they are commensurable**, which is the applefication
assumption proper. Proportions are kept here, with the raw counts printed beside them
so a stricter reader can refuse them.

### What replaces what

| banned | replacement | why it survives |
|---|---|---|
| Pearson r between two series | **Kendall's τ** | counts concordant vs discordant *pairs of observations*; no centre, no magnitude |
| average linkage | **complete linkage** | the max is an order statistic |
| ICC / variance ratio | **AUC**: of all (within-basket, between-basket) comparisons, how many put the within-pair closer | a count of comparisons |
| ARI between two partitions | **per-pair co-membership counts** | how many derivations bundled *this* pair; never collapsed |
| any summary | **the distribution** | it is the answer, not a step towards one |

---

## 5. Do not collapse

A single number is a claim that everything it summarises was one kind of thing. So the
report is the **distribution**, and the ban is what forces this rather than taste.

Worked, on 150 marine stations and every feature subset of size 1–4, each compared
against the basketing built from **every dimension it left out**:

| station pairs bundled together in… | real data | permuted control |
|---|---|---|
| ≥ 90% of trials | **39** | **0** |
| ≥ 70% of trials | **90** | **4** |

Counts. No mean anywhere. And notice what the collapsed version would have hidden:
these 90 pairs are a tiny minority of 11,175, and *that is the finding* — a small
stable core, and 11,000 pairs whose bundling the choice of features decides. An
average over pairs reports "high agreement" and describes neither population.

**The mirror trap.** The *agreement* histogram for the same run looks superb — 98% of
pairs in the top decile — and is worthless, because at 84 groups almost every pair is
apart in everything and agrees trivially. The permuted control reaches 96%. Agreement
inherits the granularity; **bundling** does not. A distribution can be as
uninterpretable as a mean if it is a distribution of the wrong thing.

---

## 6. Compare against what you left out

Two ways to ask whether a basketing is real, and they are not equally good.

**Against another arbitrary subset** — the general form. But an arbitrary other subset
may itself produce a garbage basketing, so agreeing with it establishes nothing. Worse,
averaging over many such comparisons is a **popularity contest among bad baskets**: it
measures what junk has in common, and that looks exactly like agreement.

**Against the complement** — every dimension you did not use, pooled. The strongest
alternative the data can supply. Measured against a permutation control on the marine
data, the distributions do not overlap: the **worst** real subset beats the **best**
permuted one at every size (min +0.369 vs max +0.152 at one feature; +0.472 vs +0.244
at four). So on that data random combinations *do* make baskets that explain their
complements, and any averaging over them is licensed — conditionally, and the
condition is what was tested.

**And it is the part that scales.** Each test costs exactly **two clusterings** — the
subset and its complement — so cost is linear in draws and **independent of the size
of the combinatorial space**. Anything that weighs subsets against each other needs the
whole space to mean anything and is O(2^V): affordable at 9 variables, never at 50.
Four draws per size reproduce the exhaustive medians to within 0.07. **The
enumeration was a convenience, not the method.**

---

## 7. Your null is not the null

A statistic's nominal null is the null of the model it was derived under, not of the
constraint you actually imposed. Four instances, all in one project, all found by
computing the null rather than quoting it:

| statistic | quoted null | actual null | consequence |
|---|---|---|---|
| ρ\* = MSB/(MSB+MSW) | 0 | **0.5** — numerator not mean-corrected | every raw value misread |
| ARI, 12 groups vs 84 | max 1.0 | **max 0.132** — margins cap it | 0.117 read as near-floor; it was 88% of ceiling |
| ARI between contiguous partitions | 0 | **0.337** — contiguity is not in the null | half of any raw figure |
| ARI between *derived* partitions | 0.337 | **0.12** — linkage on noise chains, unlike matched blobs | lift understated by 0.25 |

Note the last one runs **against** the finding. The direction is not guessable in
advance, which is the whole argument for measuring it.

The general rule: **whatever you constrained, the null must be constrained the same
way** — same sizes, same shapes, same connectivity, same procedure. The strongest form
is to permute the data itself and rerun everything: cut the tie between an entity and
its values, keep every other structure exactly, and whatever survives is the procedure
agreeing with itself.

---

## 7b. Rate a data stream by the errors it can contain

Not all errors are the same kind, and the useful ordering is **recoverability** — what
can be undone downstream, which the Data Processing Inequality settles absolutely: no
processing recovers what a channel discarded.

| class | error | recoverable? | detectable from within? |
|---|---|---|---|
| **1. value error** | drift, calibration offset, fouling, noise | **yes** — reference, duplicate, or cross-sensor redundancy | yes, by replication |
| **2. quantisation** | rounding, coarse units, `<0.5` censoring | no, but **boundable** — the fiber is uniform and stated | yes |
| **3. aggregation** | depth to two bins, time to month, cast to station | no, but **countable** — you know what was collapsed | yes |
| **4. schema conflation** | one column pooling incommensurables | no, and **not boundable** — the distinguishing field was never recorded | only from outside |
| **5. unfilled field** | column exists, holds a constant or blank | no — but it **names its own gap** | trivially |
| **6. absent dimension** | no column at all | no, not boundable, **not countable** | **no** |
| **7. model-as-datum** | a modelled value in a column shaped like a measured one | no — and it **propagates as confidence** | no |

**Classes 1–6 subtract. Class 7 adds.** Every other class destroys information and
should make you less certain. Model-as-datum manufactures apparent information and
makes downstream estimates *more* confident — the only class whose error travels
forward with a narrower interval than it deserves. It is precision-without-
identification, created at source.

**Class 5 beats class 4, which is counterintuitive and worth internalising.** An empty
column is honest about its emptiness: `SondeNavn = Unknown` on 83% of rows states
exactly what is missing, and you can count it. A column named `Oxygen indhold` pooling
Winkler titration, Clark electrode and optode readings states nothing, because the
field that would distinguish them was never created. **A gap you can name is worth more
than a conflation you cannot see.**

**Worked, on the origin project's streams:**

| stream | classes present |
|---|---|
| CTD sensor values | 1, 2 |
| CTD as the archive records it | + **4** (parameter pooling), **5** (instrument, sampler), **6** (no time of day) |
| this project's own derived products | + **3**, at 3,900:1 |
| the water body column | **7** |
| the headline 69.6% attribution | **7**, with 51% of area modelled |

The sensors carry the benign class. Everything expensive happened at the keyboard —
which is why "better instruments" is the wrong ask and "fill in the field" is the right
one.

---

## 8. The methods, and whether they survive their own audit

| # | method | status |
|---|---|---|
| 1 | variance decomposition (ICC / ρ\*) | **void** — means at three levels. Kept only as the thing to explain to people who quote it |
| 2 | shape-matched nulls | **the idea survives** (reference class), the statistic it corrected does not |
| 3 | floor and ceiling bracketing | **void** — built on ρ\* |
| 4 | feature-subspace stability | **rebuildable** — ARI is void, per-pair co-membership counts are not |
| 5 | complement agreement | **rebuildable**, and the one to carry forward: right comparison, scales, distribution-native |
| 6 | residual growth, `R_new = R_old − P` | **survives** — arithmetic on totals, no mean anywhere |
| 7 | threshold critique | not a statistic; survives |

Only two survive intact. That is the honest yield, and it is the point rather than an
embarrassment: **a method that cannot state its applefication assumption should not
have been trusted, including when it was ours.**

### 6, in full, because it survives

A residual `R = T − Σ P_j` cannot be checked against an independent measurement of
itself. But it can be checked against **what happens when the measured space grows**:
move a part `P` out of the leftover and the arithmetic predicts `R_new = R_old − P`
exactly.

- doesn't shrink → it was absorbing model error, and `P` was never in it
- shrinks by less than `P` → double counting; the account was never a partition
- the *total* moves instead → the total depends on the parts, and is circular

The ask is not the current number but **the sequence** — the leftover in each published
version, what was measured in between, and whether the arithmetic closes. Archival, not
statistical.

---

## 9. What to demand

1. **What is the applefication?** What was treated as one thing, one kind, one member?
2. **What is attributed to members?** Is it the same kind of claim as the membership rule?
3. **Show the distribution**, not the summary — and say what it is a distribution *of*.
4. **What is the null under the constraint you actually imposed?** Computed, not quoted.
5. **Does the grouping survive being derived from what it was not built on?** (entity-identity)
6. **For which functional?** Asked separately each time. (basket-utility)
7. **At which level of organisation?** The entities are a basket too.
8. **Report the count's sensitivity to the individuation rule.** "11,000 to 18,000
   species depending on the species concept" is an honest figure. "11,000" is not.

---

## Status

Written from a working audit, not a textbook. Method 4 was demonstrated on a
nine-variable dataset — the bottom of its applicable range — and is suggestive rather
than established. `../organism` exists to run it where the feature space is large.

Definitions of every computed quantity, with formulas, the line that computes each, its
null value and what it does **not** license: **[`docs/GLOSSARY.md`](docs/GLOSSARY.md)**.
No number appears in this project without an entry there. That rule caught the ρ\*
error on its first pass.

Borrowed and not claimed: Frege on sortals, Quine on identity, the Beta prior's
pseudo-count reading, Kendall's τ, the adjusted Rand index. Claimed: the inversion in
§2, the entity-identity / basket-utility split in §3, the ban in §4 and its
consequences, and the complement form in §6.

Origin: [copenhagen-waterways](https://github.com/Jjokulian/copenhagen-waterways),
where each method has a worked example with real numbers and the mistakes that
motivated them are left visible in the pages rather than edited out.
