# External experiment roadmap (E23+)

These experiments explicitly assume internet access.

## E23 — epsilon-forceability synthetic family

**Question:** Can a nondegenerate finite game exhibit a smooth tradeoff between opponent payoff regret and induced focal computation?

Construct a parameterized game where branches vary in both payoff and focal local cost. Compute exactly:

- opponent payoff regret;
- induced expected workload;
- `F_pi(eps)`, `L_pi(eps)`, `DeltaF_pi(eps)`;
- breakpoints in epsilon.

Goal: move beyond the brittle exact-tie E21b witness.

## E24 — small OpenSpiel game scan

**Question:** Under one declared exact-search architecture, how common is nonzero exposure leverage among small perfect-information games?

Install OpenSpiel and build a generic adapter.

Start with games that are small enough for exact recursion. Do not include a game unless the solver can establish exact values or clearly label approximation.

For each game:

- exact/minimax value where feasible;
- local focal cost = declared node expansions or another explicit cost;
- all/epsilon-best opponent responses;
- exposure leverage curve.

Use the scaffold in `external_experiments/open_spiel_exact_scan.py`.

## E25 — risk-sensitive exposure

**Question:** Do policy rankings change when exposure is measured by mean, upper quantile, CVaR, or worst trajectory?

Use at least:

- the rare-hard-state family;
- E23 synthetic game;
- one OpenSpiel game with stochasticity/chance if exact computation remains manageable.

Search for ranking reversals between risk measures.

## E26 — chess: position-level required nodes

**Question:** Does solver effort vary substantially across positions even when high-budget move quality is similar?

Use Stockfish + python-chess.

Define before data collection a node grid, e.g. logarithmic. For each FEN:

- obtain a high-budget reference move/eval;
- find minimum node budget meeting a stability criterion;
- save full per-budget trace.

Possible criteria:

1. chosen move equals high-budget reference for all larger tested budgets;
2. centipawn error <= delta;
3. top-k set stabilizes.

Treat each as a solver-relative operational proxy.

Use `external_experiments/chess_required_nodes.py` as a scaffold.

## E27 — chess: near-best-response exposure forcing

**Question:** Can an opponent choose a near-best move that materially increases the focal engine's required computation?

For a sampled position with opponent to move:

1. high-budget MultiPV evaluates legal moves;
2. compute opponent regret of each candidate relative to the best move;
3. push each candidate;
4. measure focal required nodes in the child position;
5. compute empirical `F(eps)` over centipawn-regret thresholds.

Important: centipawn score is a proxy for payoff, not exact game-theoretic value. Label this clearly.

Prefer positions where several near-best moves exist; however, corpus selection must not depend on exposure outcomes.

## E28 — architecture replication

**Question:** Is exposure leverage stable across declared solver architectures?

Options:

- exact naive minimax vs alpha-beta with fixed move ordering;
- minimax vs MCTS in OpenSpiel;
- Stockfish vs Leela Chess Zero if available and if a defensible cross-engine cost comparison can be made.

Do not compare raw nodes across engines as though one node were a common physical unit. Compare normalized within-engine ranks/frontier structure unless an external resource unit is available.

## E29 — optional broad Ludii sweep

Only after E24 methodology is validated. Ludii can provide a large traditional-game corpus, but broad quantity is not a substitute for exact definitions.
