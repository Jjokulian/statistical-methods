# Glossary of computed quantities

**Rule for this project: no number appears anywhere without an entry here.** Each
entry gives the definition in full, the line of code that computes it, its value
under the null (which is not always zero), and what it does **not** license.

The reason is the subject of the project itself. A statistic is an individuation
rule wearing a name — "ICC", "agreement", "worth" — and a name is exactly the thing
that lets a quantity be used for something its definition never supported. Writing
the formula down is the cheapest available defence, and it has already caught one
error in this repository (see [ρ\*](#1-mean-square-ratio-r-reported-as-icc)).

Notation throughout: $n$ observations, indexed $i$; a partition into groups
$g = 1 \dots G$ with $n_g$ members each.

---

## 1. Mean-square ratio $\rho^{*}$ (reported as `icc`)

$$\rho^{*} \;=\; \frac{\mathrm{MS_B}}{\mathrm{MS_B} + \mathrm{MS_W}}$$

with the two mean squares pooled **within month** $t$, so that a season common to
every station cannot be mistaken for a property of the baskets:

$$\mathrm{MS_B}=\frac{\displaystyle\sum_{t}\sum_{g} n_{tg}\,(\bar y_{tg}-\bar y_{t})^{2}}{N_{\text{groups}}-N_{\text{months}}}
\qquad
\mathrm{MS_W}=\frac{\displaystyle\sum_{t}\sum_{g}\sum_{i \in g} (y_{tgi}-\bar y_{tg})^{2}}{N_{\text{obs}}-N_{\text{groups}}}$$

Computed in `methods/partition_score.py`, `icc()`; identically in
`methods/partition_ceiling.py`, `icc()`.

> ### Null value: $0.5$, not $0$
>
> **This is not the ANOVA intraclass correlation**, which is
> $\rho = \dfrac{\mathrm{MS_B}-\mathrm{MS_W}}{\mathrm{MS_B}+(k-1)\mathrm{MS_W}}$ and
> does have null value $0$. The numerator here is not mean-corrected, so under random
> labels — where both mean squares are unbiased for the same $\sigma^{2}$ —
>
> $$\mathbb{E}[\rho^{*}] \;\to\; \frac{\sigma^{2}}{\sigma^{2}+\sigma^{2}} \;=\; \tfrac12 .$$
>
> Simulated at **0.4988** (20 runs, 150 stations, 12 random groups, 60 months, pure
> noise; range 0.474–0.519).
>
> **Consequence.** A raw $\rho^{*}$ near 0.5 means the partition tells you *nothing*,
> and one below 0.5 means members of a basket agree *less* than stations drawn at
> random. Only the **lift** (§2) is readable on its own. The scripts said "0 means it
> tells you nothing"; that was wrong and is corrected in place.
>
> The published headline figures are lifts, which are differences and so unaffected
> by the offset. The `share_of_available_structure` of §4 is also a ratio of
> differences and likewise unaffected.

**Does not license:** any claim about an individual station, and any comparison
across variables measured on different scales without the null run alongside.

> ### Open: the shuffled control does not sit at its null
>
> On real data the label-shuffled control reaches $\rho^{*}=0.859$ for surface oxygen
> saturation and 0.782, 0.658, 0.639 for other variables — far above the simulated
> null of 0.5, for a partition with **no** geographic content. Four candidate
> explanations have been ruled out by simulation, each returning $0.49$–$0.51$:
>
> | tested | result |
> |---|---|
> | group count, 2 → 120 groups over 150 stations | 0.459 – 0.504 |
> | unequal group sizes matched to the official shape | 0.487 |
> | persistent per-station offsets, $\sigma_\mu/\sigma_e$ up to 4 | 0.469 – 0.513 |
> | missing months, 100% / 50% / 20% observed | no effect |
>
> The construction is a genuine permutation (`shuf = real[:]; rng.shuffle(shuf)`), so
> this is not a broken control. **It is unexplained.** The untested cell is the real
> combination — ~119 groups, sizes 1 to 64, at the full station count — which the
> skew simulation could not reach.
>
> **What it does and does not touch.** Published lifts are differences against the
> **compact** null, not against 0.5, so they are unaffected. What is affected is any
> reading of a raw $\rho^{*}$, and any use of the shuffled control as a reference —
> which is a further reason the compact null is the one that is used.

---

## 2. Lift over a shape-matched null

$$\mathrm{lift} \;=\; \rho^{*}_{\text{observed}} \;-\; \frac{1}{S}\sum_{s=1}^{S}\rho^{*}_{\text{null}(s)}$$

`methods/partition_score.py`, `main()`. $S$ null partitions are grown from random
seed stations by nearest-neighbour accretion (`compact_null()`), which reproduces
the observed **size distribution and compactness** while destroying the specific
boundaries.

**Why this null and not the other two.** Shuffled labels keep the sizes and destroy
geography; latitude stripes keep compactness and equalise sizes. Neither varies one
thing at a time, and they disagree about which variables the partition explains. The
compact null is the only one holding size *and* shape fixed, so its lift isolates
what the drawn boundaries know beyond "nearby places are alike".

**Null value:** $0$ by construction. **Range:** $[-0.5, 0.5]$ in practice.

**Does not license:** a causal reading. A positive lift says the boundaries carry
information about the variable, not that the enclosure produces it.

---

## 3. Adjusted Rand index

For two partitions $A$, $B$ of the same $n$ entities with contingency table
$n_{ij}=|A_i \cap B_j|$, and $a_i, b_j$ its margins:

$$\mathrm{ARI} \;=\; \frac{\displaystyle\sum_{ij}\binom{n_{ij}}{2} \;-\; \frac{\sum_i \binom{a_i}{2}\sum_j \binom{b_j}{2}}{\binom{n}{2}}}{\displaystyle\frac{1}{2}\left[\sum_i \binom{a_i}{2}+\sum_j \binom{b_j}{2}\right] \;-\; \frac{\sum_i \binom{a_i}{2}\sum_j \binom{b_j}{2}}{\binom{n}{2}}}$$

`methods/partition_stability.py`, `ari()`.

**Null value:** $0$ (this one *is* chance-corrected). **Max:** $1$. Negative values
occur and mean the two partitions agree less than chance.

> ### The granularity ceiling
>
> The null model holds **only the two group-size vectors** fixed. Two things follow,
> and both bit this project.
>
> **(a) The maximum is not 1 when the margins differ.** $I$ can never exceed
> $\min(P_A,P_B)$, while the denominator uses their mean, so
>
> $$\mathrm{ARI}_{\max} = \frac{\min(P_A,P_B) - \mathbb{E}[I]}{\tfrac12(P_A+P_B) - \mathbb{E}[I]}$$
>
> | comparison | $P_A$ | $P_B$ | $\mathbb{E}[I]$ | $\mathrm{ARI}_{\max}$ |
> |---|---|---|---|---|
> | 12 groups vs 84, $n=150$ | 864 | 66 | 5.10 | **0.132** |
> | 84 vs 84 | 66 | 66 | 0.39 | 1.000 |
>
> An observed 0.117 at 12-vs-84 is therefore **88% of the achievable maximum**, not a
> near-zero. Always compute the ceiling before reading a cross-granularity ARI, or
> match the granularities — which is why `partition_stability.py` takes the group
> count as an argument.
>
> **(b) Chance is only chance for *arbitrary* partitions.** Nothing but the sizes is
> held fixed, so any structural constraint the compared partitions actually obey is
> outside the null. Two contiguity-constrained partitions score **0.337** with no
> shared information at all. See §10.

**Does not license:** reading a low ARI as disagreement without first showing that
the granularities match and that derived-vs-derived agreement survives at that
granularity.

---

## 4. Share of available structure (floor / ceiling)

$$\mathrm{share} \;=\; \frac{\rho^{*}_{\text{official}} - \rho^{*}_{\text{floor}}}{\rho^{*}_{\text{ceiling}} - \rho^{*}_{\text{floor}}}$$

`methods/partition_ceiling.py`, `main()`. The floor is a random partition of matched
granularity; the ceiling is stations clustered on measured similarity. Clusters are
built on **odd** months and every partition is scored on **even** months, so the
ceiling cannot win by memorising.

**Reading:** $1$ = the drawn boundaries recover everything this method could find at
that granularity; $0$ = no better than random groups of the same shape; $>1$ = the
boundaries encode something the clustering could not recover, which is evidence
**for** the partition.

**Does not license:** treating the ceiling as "the right boundaries". It is an upper
bound for *this* method at *this* granularity, nothing more.

---

## 5. Feature-subspace agreement $m$

Draw two disjoint feature subsets $F_1, F_2$ of size $k$; cluster independently from
each; take the ARI. Over $P$ such draws:

$$m(k) \;=\; \frac{1}{P}\sum_{p=1}^{P} \mathrm{ARI}\big(C(F_1^{(p)}),\, C(F_2^{(p)})\big)$$

`methods/partition_stability.py`, `main()`. Clustering is average-linkage
agglomeration on the distance

$$d_{ab} \;=\; 1 - \frac{1}{|V_{ab}|}\sum_{v \in V_{ab}} r_{ab}^{(v)}$$

where $r^{(v)}_{ab}$ is the Pearson correlation of the two stations' month-effect-
removed deviations in variable $v$, over months both observed, and $V_{ab}$ is the
subset of variables with at least `MIN_SHARED` such months. Pairs with no usable
variable take the neutral $d=1$. (`distances()`.)

**Null value:** $0$. **What rising $m(k)$ means:** the derivations are converging on
something in the entities. Flat and near zero means there is nothing to converge on.

**Does not license:** comparison across runs with different $k$, granularity, or
station sets — all three move $m$.

---

## 6. Beta moment-match: $\alpha$, $\beta$, $\kappa$

Given the per-draw agreements $\{s_p\}$ floored at zero, with mean $m$ and sample
variance $v$:

$$\kappa \;=\; \frac{m(1-m)}{v} - 1, \qquad \alpha = m\kappa, \qquad \beta = (1-m)\kappa$$

defined only where $0 < m < 1$ and $0 < v < m(1-m)$; otherwise reported as `null`.
`methods/partition_stability.py`, `beta_fit()`.

**$\kappa = \alpha+\beta$ is how well $m$ itself is pinned down across draws.** It is
*not* the pooling licence, and it is not monotone in $k$.

*Corrected:* an earlier version explained the dip at $k=4$ by saying few disjoint
splits exist there. That is wrong — there are $\binom{9}{4}\binom{5}{4}/2 = 315$
disjoint 4–4 pairs, against only 36 at $k=1$. The real reason is **overlap between
draws**: two random $k$-subsets of $V$ variables share $k^{2}/V$ on average, so at
$k{=}4,V{=}9$ successive draws share 1.8 variables against 0.11 at $k{=}1$. The draws
stop being independent, and $\kappa$ — which assumes they are — falls.

**Why draws are floored rather than rescaled.** ARI runs below zero and the Beta
support does not. A negative and a zero agreement both mean the boundary carries
nothing, and the distance between them is not information about how much.

**Does not license:** a confidence interval on the *pooling* correction. $\kappa$
describes the estimate, not the entity.

---

## 7. Worth per member $n_{\text{eff}}$

$$n_{\text{eff}} \;=\; m \cdot n_g$$

The number of pseudo-observations a basket of $n_g$ members is worth as a
Beta$(\alpha,\beta)$ prior for one of them — where a Beta prior's $\alpha+\beta$ is
what it is worth in observations. Pooling supplies the prior **mean**; nothing in a
membership rule supplies its **concentration**, and $m$ is that missing number.

**Exact only for a proportion-valued functional.** For a continuous one the
corresponding object is the normal–normal shrinkage weight
$\lambda = \tau^{2}/(\tau^{2}+\sigma^{2})$, and $m$ scales a prior *precision* rather
than a count. The structure carries; the conjugacy does not.

**Does not license:** applying a derived-partition $m$ to an official partition. Each
partition needs its own $m$, measured at its own granularity.

---

## 8. Residual growth

For a total $T$ with measured parts $P_1 \dots P_k$, the residual is
$R = T - \sum_j P_j$. It has no independent measurement — that is what makes it a
residual — but moving a part out of it predicts exactly

$$R_{\text{new}} \;=\; R_{\text{old}} - P .$$

- $R$ does not shrink → it was absorbing model error and $P$ was never in it
- $R$ shrinks by less than $P$ → double counting; the account was never a partition
- $T$ moves instead → the total depends on the parts, and is circular

**Does not license:** anything about the *current* residual. The test is over the
sequence of published versions, and is archival rather than statistical.

---

## 9. Neighbour graph and the contiguity constraint

A basket is **contiguous** when you can walk between any two of its stations, stepping
only on stations in the basket and only between graph neighbours. Enforced by
construction: clusters begin as singletons and merge only with an *adjacent* cluster,
so connectedness holds by induction (`methods/partition_contiguous.py`,
`agglomerate_contiguous()`).

Two graphs, because adjacency is a modelling decision and this document may not
pretend otherwise:

$$E_{\text{knn}} = \{(i,j) : j \in \mathrm{NN}_k(i) \ \lor\ i \in \mathrm{NN}_k(j)\}, \quad k=6$$

$$E_{\text{water}} = \{(i,j) \in E_{\text{knn}} : \overline{ij} \cap \text{coastline} = \emptyset\}$$

$E_{\text{water}}$ reads *reachable in a straight line without touching land*. Its
coastline is OSM, **not** the water-body polygons, which would reimport the assumption
under test. Distance is equirectangular, adequate at Danish latitudes.

**Degeneracy to guard.** Agglomeration from $n$ singletons to $k$ groups performs
$n-k$ merges, so $k \ge n$ performs none and every partition is all-singletons with
$\mathrm{ARI} = 0.000$ exactly. A first run asked for 84 groups over 25 stations and
produced a full table of zeros that read as a finding.

**Does not license:** treating either graph as observation. $k$ and the coastline
extent are both choices, and $k$ changes the answer.

---

## 10. Contiguous null and contiguity lift

$$\mathrm{ARI}_{0} = \underset{a<b}{\mathrm{mean}}\ \mathrm{ARI}(N_a, N_b), \qquad \mathrm{lift}_{\text{contig}} = m - \mathrm{ARI}_{0}$$

where each $N_a$ is a random **connected** partition of matched size distribution,
grown by breadth-first accretion from a random seed on the same graph
(`contiguous_null()`).

> **Why raw ARI is unreadable under this constraint.** ARI is chance-corrected against
> *arbitrary* partitions. Two contiguity-constrained partitions of the same points
> agree far above that, for no reason but both being connected blobs of similar size.
> Measured here: $\mathrm{ARI}_{0} = 0.337$ on the national graph — **half** of an
> observed 0.692 is contiguity alone. Report $\mathrm{lift}_{\text{contig}}$, never $m$.

The same structure as the compact null of §2 and the 0.5 offset of §1: a statistic
whose nominal null is not its null under the constraint actually imposed. Three
instances in one project is the argument for computing the null rather than quoting
it.

**Does not license:** comparison of lifts across graphs or group counts. $\mathrm{ARI}_0$
changes with both — it is 0.337 at 150 stations and 0.048 at 25.

---

## 11. Held-out dimension lift

Cluster on a feature subset $F$, then score that partition on a variable it never saw:

$$\mathrm{lift}_{\text{held}}(P_F, v) = \rho^{*}(P_F, v) - \underset{a}{\mathrm{mean}}\ \rho^{*}(N_a, v), \qquad v \notin F$$

averaged over all subsets of each size and all held-out $v$.
`methods/partition_subspace.py`.

**Why this is the load-bearing column.** Agreement between two derived partitions is
stability of the *derivation*, bounded above by how concentrated the space of
derivable partitions is: a procedure rigid enough to map any feature subset onto the
same partition scores well on it while ignoring the data. Held-out lift is a
train/test split **in feature space**, and no such procedure can pass it. Measured
+0.084 → +0.133 rising with $|F|$; on permuted data +0.002 → +0.004.

**Does not license:** reading it as effect size. It is a difference of mean-square
ratios, on a statistic whose own null is 0.5 (§1).

---

## 12. Permutation (procedural) null

Shuffle each variable's values **across stations within month**. Month effects,
marginal distributions, station counts, the neighbour graph, the granularity and the
clustering procedure are all preserved exactly; only the tie between a station and
its values is cut. Rerun the identical enumeration.

**This is the floor for anything the procedure produces**, and it is not
interchangeable with §10:

| quantity | correct floor | wrong floor gives |
|---|---|---|
| derived-vs-derived | permuted run, **0.12** | contiguous null 0.368 → understates lift by ~0.25 |
| derived-vs-**official** | contiguous null 0.368 | — (official is a fixed contiguous partition) |

Permuted derivations agree *less* than random connected partitions because average
linkage on noise chains into unbalanced groups rather than size-matched blobs. Two
constraints, two different reference classes, and using either for the other is wrong
in a direction you cannot guess in advance — here it was biased **against** the
finding.

> **It also confirms §1 empirically.** On permuted data the contiguous nulls score
> $\rho^{*} = 0.47$–$0.51$ — the simulated chance value of 0.5, now measured on real
> station geometry rather than synthetic noise. On unpermuted data the same nulls
> score 0.69–0.72, because spatially compact groups of real stations genuinely are
> more alike.

---

## Standing rule

A quantity computed and not entered here is a quantity that has not been checked.
When a new one is added, the entry lands in the same commit — with its null value
stated, because that is the field this document was created to stop people guessing.
