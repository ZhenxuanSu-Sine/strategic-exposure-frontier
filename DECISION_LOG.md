# Decision log

## D-SE-001 — Do not choose fixed-probe or on-policy as universally correct
They measure different semantics: counterfactual probe workload vs realized workload.

## D-SE-002 — Keep peak capability as a separate axis
Expected workload does not upper-bound peak resource requirements in general.

## D-SE-003 — Use implementation-relative local costs
Local search/query cost is tied to an explicit architecture and interface.

## D-SE-004 — Introduce opponent forceability only after single-agent semantics are clear
Avoid defining a constrained stochastic game before validating the simpler objects.

## D-SE-005 — Tic-Tac-Toe is a solver-relative case study
Naive minimax node exposure is not intrinsic complexity.
