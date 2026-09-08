# Statistical methods for testing categories

Four related tests, developed while auditing Danish marine monitoring and extracted
here because none of them is about Denmark. They answer one question in increasing
strength:

> **Is this category a property of the things in it, or of the instrument that
> measured them and the person who drew the line?**

Every one of them was written because a claim made without it turned out to be
wrong — including claims made by this author, twice, twenty minutes apart.

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

## Status and honesty

The code here is extracted from a working audit, not from a textbook. Method 4 was
demonstrated on a nine-variable dataset — the bottom of its applicable range — and is
reported there as suggestive rather than established. `../organism` exists to run it
somewhere the feature space is genuinely large.

Origin: [copenhagen-waterways](https://github.com/Jjokulian/copenhagen-waterways),
where each method has a worked example with real numbers, and where the mistakes that
motivated them are left visible in the pages rather than edited out.
