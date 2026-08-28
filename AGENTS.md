# AGENTS.md — instructions for Codex

You are a research agent continuing an existing project, not a greenfield coding task.

## Mission

Study **Strategic Exposure Frontiers** as an extension of the Skill Frontier framework. The key object is not merely “how costly is a policy?” but how provisioned capability, realized workload, workload tails, and opponent-forceable workload differ in sequential games.

## Mandatory order of work

Before writing new scientific claims:

1. Read `PROJECT_CONTEXT.md`, `BASELINE_RESULTS.md`, `THEORY_ONLINE_EXTENSION.md`, `ANTI_PATTERNS.md`.
2. Reproduce the local baseline with:
   - `python scripts_run_all.py`
   - `python selftest.py`
3. Perform the mandatory novelty audit in `NOVELTY_AUDIT.md` using the internet.
4. Write `research/ONLINE_NOVELTY_AUDIT.md` with citations and a claim-by-claim overlap matrix.
5. Only after the audit, choose one of the routes in `ONLINE_RESEARCH_PROTOCOL.md`.

## Internet usage is expected

Use the web aggressively but critically. Prefer primary sources:

- publisher pages / DOI landing pages;
- arXiv / authors' pages;
- official GitHub repositories;
- official documentation;
- Semantic Scholar / OpenAlex / Crossref for citation discovery, then verify against primary sources.

Follow backward and forward citations. Search synonyms, not only the terminology in this repo.

## Scientific discipline

For every result, state the tuple:

`(game, observation/interface, policy/solver architecture, local cost definition, opponent model, evaluation distribution)`.

Distinguish:

- theorem / proof;
- exact finite computation;
- empirical engine measurement;
- heuristic interpretation;
- speculative connection to human skill.

Do not convert a solver runtime into an intrinsic property of a game.

## Existing conclusions you must not regress from

- Action-side MI / normalized NPIC is rejected as a universal policy complexity measure.
- Mutual information is not a sufficient statistic for decision value and can reverse value rankings.
- Resource identity, interface, architecture, and scalarization matter.
- `V(x,y)` captures strategic structure that a fixed-opponent `R(x)` can miss.
- Learning dynamics are not determined by frontier geometry alone.

## Novelty discipline

The following are **known adjacent ideas**, not new claims:

- agents optimizing under computational constraints;
- utilities that include computation cost;
- bounded optimality and metareasoning;
- expected cumulative resource constraints in MDPs/CMDPs;
- information-constrained Markov control;
- average-case versus worst-case query complexity;
- adversarial inputs that induce worst-case algorithmic complexity.

The likely candidate contribution is narrower: a **frontier geometry that keeps payoff separate from implementation-relative exposure, decomposes peak/mean/tail exposure, and studies opponent-forceable exposure under epsilon-best responses**. Verify whether even this is prior art.

## Coding and experiment rules

- Preserve old outputs and null results.
- New experiments use IDs E23+.
- Every E23+ experiment must have a one-sentence falsifiable question.
- Prefer exact enumeration / dynamic programming for small games.
- For external engines, save version, commit/release, options, hardware, command, seed, and raw logs.
- Save machine-readable results (`json`, `csv`, parquet if genuinely useful).
- Add regression tests for exact invariants.
- Never tune parameters only to create visually dramatic curve separation.

## Deliverables

At the end of the stage create:

- `STAGE_ONLINE_REPORT.md`
- `research/ONLINE_NOVELTY_AUDIT.md`
- `research/THEORY_NOTES.md`
- `research/HYPOTHESIS_STATUS.md`
- new E23+ code/tests/results
- updated `results/manifest.json`
- `NEXT_STAGE.md`

A valid outcome is “the proposed framing is mostly subsumed by prior work.” Do not manufacture novelty.
