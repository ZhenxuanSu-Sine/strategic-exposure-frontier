# Online research protocol

## Phase 0 — baseline integrity

Reproduce E18–E22 unchanged. If any output differs, investigate before proceeding.

Exit condition: baseline results and tests reproduced or discrepancy documented.

## Phase 1 — novelty audit

Use the internet to map at least these literatures:

1. costly-computation / machine games;
2. bounded optimality and metareasoning;
3. constrained MDPs and occupation measures;
4. rationally inattentive / information-constrained control;
5. resource-rational analysis;
6. average-case / distributional decision-tree complexity;
7. algorithmic complexity attacks / adversarial runtime inputs;
8. game-tree pathology and adversarial search;
9. extensive-form games with bounded computation / finite automata / memory constraints.

For each candidate source, record:

- exact citation;
- object being optimized;
- where cost enters (constraint, utility penalty, machine choice, state cost, runtime, prior);
- whether state occupancy is endogenous;
- whether an opponent can influence resource cost;
- whether peak/mean/tail are separated;
- whether a payoff-constrained opponent exposure curve already exists;
- exact relationship to this repo.

Exit condition: a defensible overlap matrix, not a prose-only bibliography.

## Phase 2 — formalization gate

Formalize only the part not already subsumed.

Preferred object if it survives:

`F_pi(eps) = sup_{sigma: u(pi,sigma) <= v(pi)+eps} E[W(pi,sigma)]`.

Also retain `L_pi(eps)` and `DeltaF_pi(eps)`.

Add risk axes only if needed:

- mean workload;
- upper quantile;
- CVaR;
- essential supremum / trajectory peak;
- provisioned local capability.

Exit condition: definitions have declared game, implementation, cost process and opponent semantics.

## Phase 3 — exact finite games

Before chess or broad sweeps, establish the object exactly on finite games.

Required:

- parameterized positive family;
- parameterized null family if possible;
- smallest nondegenerate positive witness;
- sufficient/necessary conditions for zero exposure leverage where tractable;
- epsilon sweep, not only epsilon=0.

Exit condition: at least one theorem/counterexample plus exact numerical verification.

## Phase 4 — OpenSpiel scan

Use official OpenSpiel. Start with small deterministic two-player perfect-information games whose trees can be enumerated or tightly bounded.

Do not blindly run dozens of games. First create a generic adapter that records:

- game name/parameters;
- exact game value if available;
- focal policy and opponent response set;
- local declared solver cost;
- expected/peak/tail workload;
- epsilon-forceability curve.

If exact full-tree enumeration is impossible, label results approximate and provide stopping/error criteria.

Exit condition: cross-game patterns are measured with a common declared architecture, while still being described as architecture-relative.

## Phase 5 — chess engine study

Use Stockfish through python-chess. Prefer node-limited analysis.

Possible operational definition of focal “required nodes” on position `s`:

minimum node budget `n` on a predetermined grid such that the engine's selected move matches the high-budget reference and remains stable for all larger tested budgets; optionally require score error <= delta.

For each opponent legal move, compute:

- opponent high-budget value / regret relative to best move;
- focal player's required nodes in the resulting position.

This yields an empirical `regret -> induced computation` Pareto set and an epsilon-forceability curve.

Use a fixed position corpus selected **before** looking at exposure outcomes. Sources may include public PGNs, tactical suites, endgames, or sampled positions from a declared database.

Exit condition: protocol robustness checks across node grids, engine options, and at least one secondary cost criterion.

## Phase 6 — architecture replication

At least one central result must be repeated under a different explicit architecture.

Candidates:

- exact minimax vs MCTS in OpenSpiel;
- Stockfish vs Leela Chess Zero, if environment permits and the comparison is normalized carefully;
- naive minimax vs alpha-beta with move ordering in a finite game.

Do not compare raw node counts across fundamentally different node semantics without caveats.

## Phase 7 — synthesis

The final report must distinguish:

- already-known theory;
- genuinely new theorem/definition, if any;
- reusable empirical protocol;
- resource-model-specific observations;
- null results;
- failed hypotheses;
- claims that remain unvalidated.
