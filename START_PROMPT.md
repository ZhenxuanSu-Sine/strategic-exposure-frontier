# Codex launch prompt — Network-enabled Strategic Exposure research

You have internet access. Use it.

This repository contains a deterministic seed research program extending the Skill Frontier framework. Your job is to **audit, falsify, formalize, and empirically extend** the proposed Strategic Exposure direction.

## 0. Core inherited framework

The project studies policies `f : S -> Delta(A)` and resource-relative strength frontiers

`R_{G,I,M,C}(x) = sup_{f: c_{I,M}(f) <= x} r_G(f)`

with

`c_{I,M}(f) = inf_{M: Beh(M)=f} C(M)`.

For zero-sum interaction it also studies

`V_G(x,y) = sup_{c(f)<=x} inf_{c(g)<=y} u_G(f,g)`.

Stage 3 established that interface, architecture, resource identity, opponent model and cost parameterization matter. Do not revert to a game-only “intrinsic depth” scalar.

## 1. New research target

Separate four notions:

- **provisioned / peak capability**;
- **realized expected workload** under endogenous occupancy;
- **tail exposure** (quantile / CVaR / worst trajectory workload);
- **opponent-forceable exposure**.

The most important proposed new object is an epsilon-best-response exposure curve. For a focal policy `pi` against a minimizing opponent,

`v(pi) = inf_sigma u(pi,sigma)`

`BR_epsilon(pi) = {sigma : u(pi,sigma) <= v(pi) + epsilon}`

and, for a declared implementation/cost process with trajectory workload `W`,

`F_pi(epsilon) = sup_{sigma in BR_epsilon(pi)} E[W | pi,sigma]`.

Also compute

`L_pi(epsilon) = inf_{sigma in BR_epsilon(pi)} E[W | pi,sigma]`

and exposure leverage

`DeltaF_pi(epsilon) = F_pi(epsilon) - L_pi(epsilon)`.

At epsilon=0, this reduces to payoff-preserving best-response tie-breaking forceability. E21 showed that this effect is absent in the seeded Tic-Tac-Toe setup; E21b showed it can exist in a minimal constructed game.

## 2. First, reproduce; then do a novelty audit

Run:

```bash
python scripts_run_all.py
python selftest.py
```

Do not begin by adding more toy experiments.

Read `NOVELTY_AUDIT.md` and perform a serious internet search. In particular, you MUST read/trace:

- Halpern & Pass on game theory / algorithmic rationality with costly computation;
- Russell & Wefald on metareasoning;
- Russell & Subramanian on bounded optimality;
- Altman on constrained MDPs / occupation measures;
- Shafieepoorfard, Raginsky & Meyn on rationally inattentive Markov control;
- resource-rational analysis;
- worst-case vs average-case / distributional query complexity;
- algorithmic complexity attacks;
- work on adversarial or pathological game-tree search.

Search both backward and forward citations, plus synonymous language such as:

- computational games;
- machine games;
- costly computation;
- resource-bounded extensive-form games;
- metalevel MDP / value of computation;
- adversarial computational burden;
- runtime attack / complexity attack;
- opponent-induced search cost;
- distributional vs worst-case decision-tree complexity;
- risk-sensitive computational cost.

Write `research/ONLINE_NOVELTY_AUDIT.md` before making any novelty statement.

## 3. Decision gate after literature review

Choose one:

### Route A — core framing survives

If the exact epsilon-forceability / exposure-frontier object is not already standard, formalize it and prove basic properties. Then run E23–E28.

### Route B — core framing is largely known, but epsilon-forceability is a useful specialization

Reframe the contribution explicitly as a synthesis / diagnostic framework for game skill and computational exposure. Focus on exact equivalence mappings to prior frameworks and empirical evidence across games/architectures.

### Route C — prior art fully subsumes it

Do not force the project. Pivot to the strongest unresolved subproblem found during the audit. Candidate pivots:

1. risk-sensitive exposure (`mean` vs `CVaR` vs `peak`);
2. epsilon-best-response exposure leverage as an adversarial robustness property;
3. architecture-stability of game rankings under exposure frontiers;
4. empirical human thinking-time comparison in chess, clearly separated from the formal game metric.

Document the pivot and why.

## 4. Required theory tasks

Try to prove or disprove:

1. `F_pi(epsilon)` is monotone nondecreasing in epsilon.
2. `DeltaF_pi(0) > 0` iff payoff-optimal responses contain workload-heterogeneous responses, under a fixed implementation/cost process.
3. A bounded expected workload does not imply a bounded peak/tail capability without additional tail assumptions.
4. Identify sufficient conditions under which mean and peak frontiers coincide or are order-equivalent.
5. Determine whether forceability is invariant under payoff-preserving strategy recodings, and exactly what implementation assumptions break invariance.

Keep the implementation-relative distinction explicit.

## 5. Required external experiments

Use `EXTERNAL_EXPERIMENTS.md` as the default roadmap.

Priority order:

- E23: exact epsilon-forceability in a parameterized synthetic family;
- E24: systematic scan of small perfect-information OpenSpiel games;
- E25: risk-sensitive exposure frontier (mean / quantile / CVaR / peak);
- E26: Stockfish node-budget study on chess positions;
- E27: opponent-selected near-best chess moves maximizing focal solver effort;
- E28: architecture replication (e.g. alpha-beta/minimax vs MCTS, or Stockfish vs another declared engine if feasible).

Ludii is optional for broad game sweeps after exact methodology is stable.

## 6. External engine discipline

For Stockfish/chess:

- never say “chess requires N nodes”;
- say “Stockfish VERSION under OPTIONS/HARDWARE required N searched nodes according to criterion K on position P”;
- use node budgets rather than wall-clock time whenever possible;
- record FEN/PGN, engine binary hash/version, threads/hash size, Syzygy usage, NNUE file/version, MultiPV, and every UCI option that matters;
- define the criterion for “required computation” before collecting data (move stability, score stability, top-k stability, regret vs high-budget reference, etc.).

## 7. Deliverables

Produce:

1. `STAGE_ONLINE_REPORT.md` — results, failures, literature position, conclusions.
2. `research/ONLINE_NOVELTY_AUDIT.md` — citation graph and overlap matrix.
3. `research/THEORY_NOTES.md` — proofs/counterexamples.
4. `research/HYPOTHESIS_STATUS.md` — every hypothesis: supported/rejected/open/superseded.
5. E23+ reproducible code and machine-readable outputs.
6. Updated `results/manifest.json` with versions and hashes.
7. `NEXT_STAGE.md` — only recommendations justified by the evidence.

## 8. Anti-narrative rule

The goal is not to prove that Strategic Exposure Frontier is important. The goal is to determine precisely whether it adds a distinct object, which parts are already known, and whether the object exposes measurable structure that payoff-only and static resource-frontier analyses miss.
