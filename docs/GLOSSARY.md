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

> **The granularity trap.** ARI is depressed by a mismatch in group *count* alone,
> independently of whether the partitions describe the same structure. Comparing 84
> official groups against 12 derived ones is therefore not a comparison, and a low
> score from such a pairing must not be reported. This is why
> `partition_stability.py` takes the group count as an argument.

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
*not* the pooling licence, and it is not monotone in $k$: at $k=4$ out of 9 variables
few disjoint splits exist, so draws share composition and $\kappa$ falls.

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

## Standing rule

A quantity computed and not entered here is a quantity that has not been checked.
When a new one is added, the entry lands in the same commit — with its null value
stated, because that is the field this document was created to stop people guessing.
