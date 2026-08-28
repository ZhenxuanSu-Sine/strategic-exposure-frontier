# Strategic Exposure Frontier — Codex Online Research Pack

Prepared: 2026-08-28

This repository is a **network-enabled research starter** for the next stage of the Skill Frontier / Policy Complexity project.

The new direction is **Strategic Exposure Frontier**: separate

1. capability that must be provisioned,
2. workload actually realized along trajectories,
3. tail / rare-event workload,
4. workload an opponent can force while remaining payoff-rational.

The package intentionally does **not** assume this is novel. A network-enabled agent must first audit adjacent literatures, especially costly-computation games, bounded optimality/metareasoning, CMDPs/occupation measures, rationally inattentive control, and worst-case vs average-case query complexity.

## Most important update versus the offline pack

The offline seed already showed:

- E18: expected workload can stay constant while peak capability diverges;
- E19: peak-budget and expected-workload frontiers can select different strategies;
- E21: Tic-Tac-Toe gave a null payoff-preserving exposure attack under one declared minimax architecture;
- E21b: a minimal game proves the phenomenon can exist.

The online stage should now ask a sharper question:

> **How much extra resource exposure can a strategically rational opponent induce, as a function of how much payoff optimality the opponent is willing to sacrifice?**

For a focal policy `pi`, define an epsilon-best-response exposure curve

`F_pi(epsilon) = sup_{sigma in BR_epsilon(pi)} E[W(pi,sigma)]`.

At `epsilon=0`, this is payoff-preserving tie-breaking forceability. For `epsilon>0`, it becomes a continuous strategic attack surface rather than a brittle tie case.

## Start

1. Read `AGENTS.md`.
2. Give `START_PROMPT.md` to Codex if you are launching it manually.
3. Run the baseline:

```bash
python scripts_run_all.py
python selftest.py
```

4. Then follow the online phase gates in `ONLINE_RESEARCH_PROTOCOL.md`.

## Repository map

- `AGENTS.md` — persistent Codex instructions.
- `START_PROMPT.md` — complete launch prompt.
- `PROJECT_CONTEXT.md` — inherited Stage 1–3 constraints.
- `THEORY.md` — seed definitions.
- `THEORY_ONLINE_EXTENSION.md` — epsilon-forceability and risk-sensitive extension.
- `NOVELTY_AUDIT.md` — mandatory prior-art audit protocol.
- `REFERENCE_SEEDS.md` — verified starting literature/repos/URLs.
- `ONLINE_RESEARCH_PROTOCOL.md` — phased workflow with go/no-go gates.
- `EXTERNAL_EXPERIMENTS.md` — E23+ roadmap using internet-accessible tools.
- `BASELINE_RESULTS.md` — existing E18–E22 seed evidence.
- `experiments/`, `src/`, `tests/` — deterministic baseline code.
- `external_experiments/` — online experiment scaffolds.
- `research_skills/` — reusable research discipline notes.

## Hard rule

A claim about a particular `(G, interface, architecture, cost, opponent/evaluation distribution)` is not automatically a claim about the intrinsic depth of `G`.
