# The code, as it actually ran

These are working scripts lifted from the audit that produced the methods, not a
tidied library. They read that project's data layout and will not run here unchanged.
They are included because the README describes what the methods do and these say what
was actually computed — including the guards that exist only because something went
wrong once.

| file | method | the guard worth reading |
|---|---|---|
| `partition_score.py` | 2 — shape-matched nulls | three nulls side by side; the size-and-shape-matched one exists because the other two disagreed and reversed a published conclusion |
| `partition_ceiling.py` | 3 — floor and ceiling | refuses to report a share when the derived partition loses, instead of printing 3.566; flags a saturated floor |
| `partition_stability.py` | 4 — feature-subspace stability | removes the month effect before clustering, or every pair of entities looks alike |
| `extrapolation.py` | subsampling over entities | states that its target is itself an estimate, so the curves are a lower bound on error |

Porting them means replacing the loaders at the top. The statistics below that are
generic: `icc()`, `ari()`, `agglomerate()` and the null constructions take label
vectors and distance matrices and know nothing about water.
