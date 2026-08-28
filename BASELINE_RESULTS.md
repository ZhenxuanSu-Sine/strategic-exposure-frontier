# Baseline results generated with the starter code

These are **seed results**, not conclusions to protect. The next research agent should reproduce them and then try to break/generalize them.

## E18 — Rare-hard-state separation: positive

For `p_hard=1/n` and hard-state cost `n`, the script verifies exactly up to `n=1024`:

- on-policy expected workload = `1`;
- peak capability = `n`;
- peak/workload ratio grows to `1024` in the baseline sweep.

This is the cleanest reason not to interpret expected on-policy cost as a capability bound.

## E19 — Route-game frontiers: positive separation

Using a 21-bit majority hard branch and safe reward `0.65`, the peak-budget and workload-budget envelopes differ.

Largest baseline reward gap on the sampled grid:

- budget: `16.8`;
- `R_work - R_peak ≈ 0.10129`;
- workload-optimal strategy: `p_hard=0.8`, `q=21`;
- peak-optimal strategy: `p_hard=1.0`, `q=15`.

Interpretation: an average-workload constraint can prefer occasional use of a fully capable solver, whereas a peak constraint limits the solver itself.

## E20 — Opponent/environment exposure: positive but intentionally simple

For a full `q=21` hard solver:

- hard-state frequency `θ=0.1` -> workload `2.1`;
- `θ=0.5` -> workload `10.5`;
- `θ=1.0` -> workload `21`.

Same implementation, same peak capability, different realized workload purely from occupancy.

## E21 — Tic-Tac-Toe BR-force: null result

Declared architecture: naive full minimax, no cache, no alpha-beta.

- empty-board naive minimax invocation: `549,946` nodes;
- X vs lexicographic minimax O: cumulative X workload `557,492` nodes, game value `0`;
- X vs minimax-then-exposure O: cumulative X workload `557,492` nodes, game value `0`.

So the desired payoff-preserving exposure attack **does not appear from the empty Tic-Tac-Toe state under this exact architecture/tie-breaking setup**. Preserve this result.

## E21b — Minimal best-response exposure witness: positive existence example

A deliberately minimal game has two payoff-equivalent O best responses, one exposing X to query cost `1` and the other to cost `16`. This proves the phenomenon is possible in principle, but is not evidence that it is common or natural.

## E22 — Joint frontier: positive structural richness

On a `22 × 22` `(peak, workload)` budget grid, the baseline found `117` distinct optimal `(p_hard, q)` strategies. Scalar projections therefore discard substantial strategy structure in this toy family.
