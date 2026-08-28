# Experiment plan E18–E22

## E18 — Rare-hard-state separation

**Question:** Can expected on-policy workload stay bounded while peak capability diverges?

**Construction:** hard state probability `p_n=1/n`; hard-state local cost `n`.

**Expected result:** workload exactly `1`, peak `n`.

**Role:** sanity theorem/counterexample. If code does not reproduce this, stop and fix accounting.

---

## E19 — Route game: peak vs workload frontiers

A player chooses how often to enter a hard branch (`p`) and how many of `n=21` bits to query there (`q`).

- Safe branch reward: 0.65.
- Hard branch reward: Bayes-optimal accuracy on 21-bit majority after `q` observed bits.
- Peak cost: `q` if the hard solver is used.
- Workload: `p*q`.

Enumerate `(p,q)` exactly on a dense grid and compute:

1. `R_peak(x)`;
2. `R_work(w)`;
3. optimal `(p,q)` along each frontier.

**Key diagnostic:** workload budgets may favor rare use of a high-capability solver; peak budgets forbid this.

---

## E20 — Opponent-controlled exposure

Opponent/challenge process selects the hard branch with probability `θ`.

For a fixed hard-task solver, compare:

- benign/reference exposure (`θ=0.1`);
- neutral exposure (`θ=0.5`);
- forced exposure (`θ=1.0`).

Then compute reward-vs-workload frontiers for each `θ`.

**Question:** does an adaptive environment rotate the frontier simply by changing occupancy?

---

## E21 — Tic-Tac-Toe payoff-preserving complexity attack

Architecture: **explicitly** naive full minimax search without caching or alpha-beta pruning. This is not an intrinsic property of Tic-Tac-Toe.

Player X follows a deterministic minimax policy. At each X move, local cost is the number of nodes a naive minimax invocation would expand from the current state.

Compare opponent O policies:

1. random;
2. lexicographic minimax best response;
3. **minimax-then-exposure**: among O's payoff-optimal moves, choose the move maximizing X's future cumulative search nodes.

Record X game value and cumulative search workload.

**Strong positive result:** policies 2 and 3 have the same game value but policy 3 causes larger X workload.

This would instantiate `c_BR-force` in a real sequential board-game tree.

---

## E22 — Joint `(peak, workload)` surface

Using the E19 strategy set, compute

\[
R(x,w)=\max_{\text{peak}\le x,\,\text{work}\le w} r.
\]

Export a matrix and Pareto-optimal strategies.

**Question:** do scalar frontiers hide strategy classes separated in the 2D resource plane?

---

## Follow-ups only after E18–E22

- repeated / Markov RPS with memory reads as a local cost process;
- query-interface recoding tests to preserve Stage-3 interface discipline;
- directed-information resource axis;
- Chess prototype using Stockfish node budgets, with architecture explicitly declared;
- human/agent learning trajectories plotted inside the `(peak, workload, reward)` space.

## E21b — Minimal payoff-preserving exposure witness

A deliberately minimal two-branch zero-sum game verifies existence of a best-response tie in which payoff is unchanged but player resource exposure differs. Treat this only as an existence witness. The scientifically interesting task is to characterize non-degenerate/natural conditions for the effect.
