# Hypotheses

Every hypothesis must be allowed to fail. Do not rename failures into successes.

| ID | Hypothesis | Initial status | Primary test |
|---|---|---|---|
| H-SE-001 | Peak capability and on-policy workload induce non-equivalent frontiers in sequential tasks. | open | E19/E22 |
| H-SE-002 | Expected on-policy workload can remain bounded while required peak capability diverges. | theorem candidate / constructive | E18 |
| H-SE-003 | Strategic routing can create a measurable gap between capability-limited and workload-limited optimal policies. | open | E19 |
| H-SE-004 | Opponent policy materially changes a player's realized workload even when the player's implementation is fixed. | open | E20/E21 |
| H-SE-005 | Among payoff-best-responses, opponents can sometimes select higher-exposure trajectories without changing game value. | open | E21 Tic-Tac-Toe |
| H-SE-006 | A 2D `(peak, workload)` frontier is more stable semantically than either scalar alone, but is still architecture/interface relative. | open | E22 + recoding follow-up |
| H-SE-007 | "Deep states exist" and "deep states are strategically forceable" are empirically distinct properties. | open | E20/E21 |
| H-SE-008 | A large forceability gap predicts brittleness of bounded-resource agents against adaptive opponents. | future empirical | Stage after exact toy games |

## Falsification criteria

- H-SE-001 fails on a studied family if the two frontiers coincide after accounting for units and feasible strategies.
- H-SE-003 fails if every Pareto-optimal workload solution can be matched by an equal-peak solution with identical reward.
- H-SE-004 fails if induced occupancy changes but integrated local resource use does not.
- H-SE-005 fails in Tic-Tac-Toe if all minimax-best responses induce identical X workload.
