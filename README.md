# Statistical methods for testing categories

## Root directive

> **Nothing is given.** Every number presupposes a rule for what counts as *one*.
> Every category presupposes a rule for what its members *share*. Neither rule is in
> the data, and neither is usually stated. **Both are testable by the same operation:
> resample the space and see whether the boundary survives.**

Everything below is that one operation, applied at different levels. The methods were
developed while auditing Danish marine monitoring and extracted here because none of
them is about Denmark. Each was written because a claim made without it turned out to
be wrong — including claims made by this author, twice, twenty minutes apart.

### What is old, and what is not

The observation that counting needs a decision is a century old and is **not claimed
here**. Point at a deck of cards and ask *how many?* — one deck, four suits, fifty-two
cards, about 10²⁴ atoms. There is no answer until somebody has said what a one is.
Frege made this about number and sortals; Quine's slogan is *no entity without
identity*.

**But Quine's version runs the wrong way for our purpose.** There, identity is a
**precondition** — a licence you must already hold before you may quantify at all,
supplied by the language, and not itself an empirical matter. Our version makes it an
**output**:

> **not** *no entity without identity* — but ***a stable boundary is what an entity
> is***.

Identity is not assumed and then used; it is produced, by measurement, in degrees.
The question stops being *is this a thing* (unanswerable, and always answered by
convention) and becomes *how stable is this boundary, and under what*. That has a
number.

### Two stabilities, two products

The same resampling operation yields two entirely different things depending on **what
is varied**, and conflating them is the error this whole document exists to prevent:

| Vary | Hold fixed | Stability yields | Reading |
|---|---|---|---|
| the **metric space** — disjoint halves of the feature space | the target | **entity-identity** | structural: *is there a thing here at all* |
| the **functional of relevance** — the quantities the category is used to predict | the features | **basket-utility** | operational: *is this category good for anything* |

**Entity-identity is a stability coefficient, not a verdict.** A boundary that persists
across independently drawn metric spaces is an entity to that degree; one that appears
only in the space that defined it is a drawing. So entities come in strengths, and the
right report is the coefficient, not the noun.

**Basket-utility is per-functional and never transfers.** A basket is not useful; it is
useful *for* something, and the answer changes with the something. In the origin
project the same 123 official water bodies carried real signal for surface oxygen
saturation (+0.402 over a size-and-shape-matched null) and **negative** signal for
fluorescence (−0.050). One partition, one dataset, one month: useful and useless at
once, depending only on the functional asked.

The two are independent, and the cross terms are where the damage is:

|  | **identity-stable** | **identity-unstable** |
|---|---|---|
| **useful for the functional** | a real thing that also predicts — the only case that licenses the usual language | predicts your one target and dissolves under any other metric space: **a fit to your purpose, not a thing.** The most dangerous cell, because it validates |
| **useless for the functional** | a real thing, wrong tool — say so and pick another partition | a drawing, used as a fact |

The bait-and-switch that motivated all of this lives in the top-right cell: a boundary
earns its name from one sense (a fjord *is* an enclosure — true, and identity-stable
for salinity, which diffusion makes it stable for) and is then spent in the other
(therefore measurements inside it are interchangeable — false, and unrelated to the
first).

### Where the two go in a Bayesian analysis

The split is not just terminological. The two products enter at different points of an
inference, and each fixes a specific thing that is currently done badly.

**Entity-identity sets the prior's strength — not its mean.** A Beta(α, β) prior is
read as pseudo-counts, and α + β is what the prior is *worth* in observations. When a
basket is used as a prior for a new member — the usual, sensible move — the mean comes
from pooling what is already in the basket, but the **concentration has no
justification at all** unless the boundary has been tested. Identity-stability supplies
exactly that missing number:

> A basket of `n` members whose boundary reproduces at agreement `m` across disjoint
> halves of the feature space is worth about **`m·n` pseudo-observations, not `n`**.

At m ≈ 0 a basket is worth nothing and the honest prior is the flat one. This is
Laplace's rule of succession in structure — a correction for not having seen
everything — with the correction estimated rather than set to +1/+2 by convention.

**Measured, on the origin project's 150 fully-observed stations:**

| features per half | agreement `m` | κ | a 4-member basket is worth |
|---|---|---|---|
| 1 | 0.238 | 3.9 | 0.95 observations |
| 2 | 0.333 | 22.4 | 1.33 |
| 3 | 0.359 | 30.3 | 1.44 |
| 4 | **0.462** | 17.8 | **1.85** |

So at the friendliest setting available, four stations pooled are worth **fewer than
two observations**, and the boundary is doing under half the work its use assumes.

Two honesty notes on that table, because they are the kind of thing this document
exists to make people report:

- **κ is not monotone**, and the dip at four is not a finding about the water. Nine
  variables admit few disjoint 4–4 splits, so those draws share composition and the
  spread widens. κ measures how well `m` is pinned, and it is pinned worst where the
  draws are fewest — as at one feature per half, where κ = 3.9 and a single draw ran
  from −0.027 to +0.737 depending only on **which** variable was picked.
- **The official partition's worth was withheld here, and the rerun reversed it.** At
  mismatched granularity it scored 0.117 against the derivations, which over its mean
  1.79 stations per body would have given **0.21 pseudo-observations** — a devastating
  figure, and a false one. Rerun with both sides at 84 groups:

  | features per half | derived-vs-derived | derived-vs-**official** |
  |---|---|---|
  | 1 | 0.309 | 0.313 |
  | 2 | 0.424 | 0.414 |
  | 3 | 0.471 | 0.398 |
  | 4 | **0.576** | **0.436** |

  The official water bodies track independent derivations nearly as closely as the
  derivations track each other — **76% of the achievable agreement** (0.436 / 0.576),
  and at one feature per half they match it exactly. `m = 0.436` puts a 1.79-station
  body at **0.78 pseudo-observations**, not 0.21.

  **This is evidence for the drawn boundaries**, and it is the opposite of what the
  audit expected to find. It exists only because the confounded number was refused:
  0.21 would have been quoted, would have been wrong by a factor of four, and would
  have been wrong in the direction the author was already inclined to believe.

**And it is the non-circular route to a quantity hierarchical models already need.**
Partial pooling estimates a shrinkage weight from the group-level variance τ² — but
from *the same responses being modelled*, which is the ICC circularity in Bayesian
clothing. Feature-subspace stability estimates it from a disjoint half of the feature
space that the target never touched. What a hierarchical prior smuggles in is
**exchangeability within group**, and identity-stability is a direct measurement of it
rather than an assumption about it.

**Basket-utility is the likelihood, and lives in the updating.** Utility is defined
against outcomes, per functional, so each functional the partition is tested on is an
update to the partition's standing *for that functional* — never in general. The prior
is target-blind by construction; the posterior is target-specific by construction; and
they are estimated from disjoint information, which is what makes the update mean
anything.

Which gives the diagnostic the loop exists for. **When a posterior pulls hard against a
strongly-concentrated prior, one of the two is wrong, and which one has a signature:**

- **many functionals contradict the same partition** → the boundary is wrong. The
  stability score was measuring reproducibility of an artifact shared across the
  feature space (a common instrument, a common sampling geometry).
- **one functional contradicts it, the others do not** → the boundary is fine and the
  functional does not live on it. Fjord boundaries are stable and predict salinity;
  fluorescence is not a thing fjord boundaries are about.

**The limit, stated.** The Beta reading is exact when the functional is a proportion.
For a continuous functional the same role is played by the normal-normal shrinkage
weight, and `m·n` becomes a scaling of the prior precision rather than of a count. The
structure carries; the conjugacy does not.

### It is not an exotic problem

- **"Denmark has 123 marine water bodies."** That counts polygons, not waters.
- **"1,527 monitoring stations."** That counts register entries — identity claims about
  positions revisited for forty years through changed instruments and changed water.
- **"About 11,000 bird species."** Under a phylogenetic rather than biological species
  concept the count rises toward 18,000. The birds did not change. **A quantity that
  moves by 60% when the sortal changes is not a measurement of birds.**
- **GDP** counts transactions inside a boundary that excludes household labour.
  **Unemployment** counts by a rule that excludes discouraged workers. **Deaths "with"
  versus "from"** a disease is a sortal dispute conducted as an epidemiological one.
- **This document's origin project enumerates "165 mechanisms in 17 groups."** Those
  count our own decisions about where one mechanism ends. Nobody has tested that
  partition either, and the project says so.

### The practical demand

Parallel to reporting an error bar on a measurement, and just as cheap:

> **Report the count's sensitivity to the individuation rule** — not the number, but
> the range it takes across the reasonable rules. "11,000 to 18,000 species, depending
> on the species concept" is an honest figure. "11,000" is not.
>
> **And report utility per functional, never in general.** "This partition explains X
> for oxygen and nothing for fluorescence" is a result. "This partition is meaningful"
> is not a claim about anything.

Where the rules are few and named, the first is arithmetic. Where they are not, the
stability test estimates it.

## The problem

A categorical column is a model output wearing the clothes of an observation. Every
continuous column in a dataset carries error — a detection limit, a calibration, a
±. No categorical column ever does. Water body, citizenship, sector code, diagnosis,
species, land use: each is the output of a polygon someone drew, a legal test someone
applied, or a classification someone wrote down, printed in the same table and the
same typeface as readings that came off an instrument.

Every basket carries two things that are easy to conflate:

- a **membership rule** — who is in. Usually sound, often a genuine fact.
- an **attribution** — what members are taken to share. A statistical claim that
  nothing in the membership rule establishes.

"Is this a real category?" answers the first and is nearly always yes. The question
with content is whether membership predicts what it is being used to predict.

## Before any of it: the entities are a basket too

Every method below takes a set of entities and asks whether a grouping over them is
real. **The entities themselves are a categorical claim, and assuming them is the same
error one level down.**

A row in a table is an assertion that this is one thing, persisting, distinct from the
next row. That assertion has a membership rule like any other, and the rules disagree:

- **Organism.** Spatial contiguity, genetic identity, reproductive unity and metabolic
  integration give different counts on the same matter. A lichen is one organism, or
  two, or three. A siphonophore is an animal or a colony. *Pando* is one aspen or
  47,000 trees. A human is a human, or a holobiont whose metabolism does not close
  without ~38 trillion bacteria. Mitochondria were free-living; the boundary moved.
- **A monitoring station.** An identity claim about a position visited for forty years.
  The instrument changed, the operator changed, and the water is entirely different
  water. It is one entity because a register gave it one number.
- **A person over time**, a **firm through mergers**, a **household**, a **patient
  episode**: each is a rule about persistence, and each was chosen.

So the honest form of the question is not *which grouping of these entities is real*
but:

> **At which level of organisation does grouping become stable?**

which is the root directive applied one level down: the entity boundary is the first
basket, and it is scored on the same **entity-identity** axis as any other.

That is answerable with the same machinery, applied recursively. Run feature-subspace
stability at several candidate levels — cells, individuals, colonies, holobionts;
casts, stations, sites — and the level where agreement between independent feature
halves is highest is where the entity boundary is doing real work. **The level of
maximal stability is itself the finding**, and it need not be the level the data was
recorded at.

Which means the vocabulary matters. Not "boundaries between organisms" but *boundaries
between stability-preserving units* — because the first phrase imports a model as
though it were a given, which is what all of this exists to prevent.

*This document did exactly that in an earlier draft, and so did the project applying
it.*

## The methods, weakest to strongest

### 1. Variance decomposition — necessary, and circular alone

Intraclass correlation, computed **conditional on whatever every entity shares**
(season, cohort, year — otherwise the common driver lands in the between-group term
and every partition scores well, including an absurd one).

`F_ST` is this statistic in population-genetics clothing, and inherits the same flaw:
it takes the partition as an **input**. `F_ST = (H_T − H_S)/H_T` cannot be computed
until the subpopulations are declared. So citing it as evidence that populations are
distinct is reasoning in a circle. It is also not one statistic — Wright, Nei's
`G_ST`, Weir & Cockerham's θ and Hudson's estimator differ on identical data.

**Never report it alone.**

### 2. Shape-matched nulls — what rescues method 1

A circular statistic compared against a null **that matches the partition's own
shape** stops being circular, because the null partitions were not chosen to be real.
Each number is contaminated by the assumption; the *difference* is not.

Matching matters more than it sounds. Three nulls on one dataset gave three different
rankings of which variables the partition explained:

| null | holds fixed | destroys | verdict |
|---|---|---|---|
| shuffled labels | group sizes | geography | salinity wins |
| equal-count stripes | compactness, equal sizes | hydrography | oxygen wins |
| **size- and shape-matched blobs** | **both** | hydrography only | oxygen wins |

Only the third varies one thing at a time, and it **reversed** the first. A published
conclusion drawn from the first had to be withdrawn.

> A partition's value is not how well it predicts, but **how much better it predicts
> than its own shape alone would**.

### 3. Floor and ceiling — bracketing instead of comparing

A null gives a floor. Clustering the data gives a candidate ceiling. The partition's
position between them is interpretable where a bare number is not:

    share of available structure = (official − floor) / (derived − floor)

Two traps, both hit in practice. The derived partition must be **fitted and scored on
different data**, or it wins by construction. And a weak clustering method can lose to
the real partition, at which point the ratio is undefined rather than large — report
that it lost, not `3.566`.

Watch the floor. If a *random* partition already scores 0.92, the statistic is
saturated and none of the three numbers can be read: the granularity is too fine for
the sample.

### 4. Feature-subspace stability — the strongest, and newly possible

Assumes no partition at all:

> Cluster the entities from a **random subset** of the features.
> Cluster again from a **disjoint** subset.
> Measure agreement (adjusted Rand index). Does it **rise** as subsets grow?

This is the **entity-identity** axis of the root directive: the metric space varies and
the boundary either survives it or does not. Run the same operation over disjoint sets
of *targets* instead of features and it measures **basket-utility** — whether the
grouping that predicts one functional is the grouping that predicts the others, or
whether each functional wants its own baskets.

A grouping that appears only when one measurement is included is an artifact of that
measurement. A grouping that appears whichever features are drawn is a property of the
entities. The candidate partition is scored on the same axis — its agreement with each
derivation — so it is one candidate among them, not the standard they are marked
against.

**This is why nulls became standard, and why that is changing.** When these statistics
were developed a study had three or four measurements, and a feature space that small
cannot be split into disjoint halves — there is nothing to hold out. The null was not
a compromise; it was the only option. Measurement is now automatic and cumulative:
many groups measure many things on the same entities, and columns accumulate
independently of any one question.

**A threshold, not a preference.** Below roughly a dozen independent features, use a
shape-matched null and accept that it cannot separate the entities from the
instrument. Above that, split the feature space, because you can.

### 5. The same move, applied to a number

A residual — `Total − Σ(known parts)` — cannot be checked against an independent
measurement of itself; that is what makes it a residual. But it can be checked against
**what happens when the measured space grows**. Move a part `P` out of the leftover
and the arithmetic predicts exactly `R_new = R_old − P`.

- doesn't shrink → it was absorbing model error, and `P` was never in it
- shrinks by less than `P` → double counting; the account was never a partition
- the *total* moves instead → the total depends on the parts, and it is circular

So the ask is not the current number but **the sequence**: the leftover in each
published version, what was measured in between, and whether the arithmetic closes.
Archival, not fieldwork.

## 6. Thresholds: the same problem, at its highest stakes

A threshold manufactures a category out of a continuum, and inherits every defect
above plus one of its own.

**The feature carrying the threshold is usually itself an estimate.** Gestational age
is not observed; it is inferred from last menstrual period or from ultrasound
biometry, and carries a documented uncertainty of days to weeks that widens with
gestation. Blood alcohol at the roadside is estimated from breath. A disability
percentage is scored. Income for a benefit cutoff is reported and reconciled. Age of
majority rests on a birth record that is occasionally wrong or absent.

In every case the law then treats the resulting category as exact. **Nobody writes
"22 weeks ± 10 days", or "80 mg/100 ml ± 6".** The estimate has an error bar; the
category it produces does not, and the error does not vanish — it is transferred into
a binary outcome, where it becomes a rate of misclassification that nobody reports
because the category is not written as a measurement.

**And a threshold requires selecting one feature from a multi-dimensional process.**
Development, intoxication, capacity and disability are each measured on many axes
that do not move together. Choosing one axis to carry a decision is precisely the
"emphasised feature" problem: the selection is a modelling choice, and the other axes
would place the line elsewhere. Feature-subspace stability (method 4) is the test of
whether a boundary drawn on one axis is recovered by the others, or is an artifact of
which axis was privileged.

**What these methods say, and what they do not.** They speak to two things: how much
measurement error a threshold converts into misclassification, and whether the
boundary is a feature of the process or of the chosen axis. They say **nothing** about
where any line should be drawn, or whether it should exist. Those are moral and legal
questions, and no statistic settles them. A method that pretended otherwise would be
committing the error this whole document is about — attributing to a measurement a
kind of authority that belongs to a different sort of claim entirely.

The narrow, non-partisan demand these methods do license, and it is the same one as
everywhere else here:

> If a categorical outcome is produced by thresholding an estimated quantity, the
> misclassification rate at that threshold is computable from the estimator's own
> published error, and should be stated alongside the rule. Not the number — the rate.

## What to demand of any categorical claim

1. **What is the membership rule?** Legal, geometric, administrative, self-reported?
2. **What is attributed to members?** Is it the same kind of thing as the rule?
3. **What is the lift over a same-shaped null?** Not the raw statistic — it took the
   category as an input and cannot testify about it.
4. **Does the grouping survive being derived from features it was not built on?**
   (entity-identity)
5. **For which functional?** — asked separately for each, never once and generalised
   (basket-utility). A partition that answers 3 and 4 has still not been shown to be
   the right partition for *your* target.
6. **And at which level of organisation?** The entities are a basket too, and the
   level of maximal stability is a finding rather than an input.

## Every number has an entry

**[`docs/GLOSSARY.md`](docs/GLOSSARY.md)** defines every quantity this project
computes — the formula, the line that computes it, its value under the null, and what
it does not license. No number appears anywhere without an entry.

That is not bookkeeping. A statistic is an individuation rule wearing a name, and the
name is exactly what lets a quantity get spent on something its definition never
supported — the same move the rest of this document is about, committed one level up.
Writing the formula down is the cheapest available defence, and it caught a live error
here on the first pass:

> The statistic the scripts report as `icc` is the mean-square ratio
> `MSB / (MSB + MSW)`, **not** the ANOVA intraclass correlation. Its numerator is not
> mean-corrected, so under random labels both mean squares estimate the same variance
> and the ratio tends to **0.5, not 0** — simulated at 0.4988. The scripts described 0
> as "tells you nothing". Corrected in place.
>
> Published figures are **lifts** and **share-of-structure**, both differences, so
> none of them moves. But the raw values were unreadable as written, and nobody would
> have found that without writing the formula next to the code.

## Status and honesty

The code here is extracted from a working audit, not from a textbook. Method 4 was
demonstrated on a nine-variable dataset — the bottom of its applicable range — and is
reported there as suggestive rather than established. `../organism` exists to run it
somewhere the feature space is genuinely large.

Origin: [copenhagen-waterways](https://github.com/Jjokulian/copenhagen-waterways),
where each method has a worked example with real numbers, and where the mistakes that
motivated them are left visible in the pages rather than edited out.
