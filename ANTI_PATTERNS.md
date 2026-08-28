# Anti-patterns / forbidden shortcuts

1. **Do not say a game is intrinsically deep/shallow** from one frontier. Always name `(G, interface, architecture, cost, opponent/evaluation distribution)`.
2. **Do not revive `I(S;A)` or normalized NPIC as universal complexity.** It remains a rejected baseline/diagnostic.
3. **Do not call on-policy workload "capability".** E18 exists specifically to test the separation.
4. **Do not call fixed-probe workload "realized effort".** It is counterfactual under declared `μ`.
5. **Do not treat minimax search depth/nodes as a property of the game.** It is relative to a declared solver architecture.
6. **Do not scalarize peak and workload without an externally justified exchange rate.** Report the 2D frontier first.
7. **Do not delete failed hypotheses or negative results.** Mark them `rejected`, `superseded`, or `inconclusive`.
8. **Do not use Monte Carlo for a tiny game when exact enumeration is practical.** Exact first, approximation later.
9. **Do not infer human cognitive difficulty from synthetic resource costs.** That is a later empirical validation question.
10. **Do not optimize the experiment to support the narrative.** Parameter sweeps and counterexamples must be retained.
