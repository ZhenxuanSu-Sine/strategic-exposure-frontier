# Project context inherited from Skill Frontier Stages 1–3

## Core object

A policy is `f : S -> Δ(A)`, strength is `r_G(f)`, and a resource-relative frontier is

\[
R_{G,\mathcal I,\mathcal M,C}(x)
= \sup_{f:\,c_{\mathcal I,\mathcal M}(f)\le x} r_G(f),
\]

with implementation-relative complexity

\[
c_{\mathcal I,\mathcal M}(f)
= \inf_{M\in\mathcal M:\mathrm{Beh}(M)=f} C(M).
\]

For zero-sum interaction, Stage 3 introduced

\[
V_G(x,y)=\sup_{c(f)\le x}\inf_{c(g)\le y} u_G(f,g).
\]

## Results that must be treated as constraints, not optional opinions

1. **NPIC/action-MI is rejected as a universal policy-complexity measure.**
   A deterministic one-bit rule and an n-bit parity rule can have the same normalized action coupling while having radically different query requirements.

2. **Mutual information is not a sufficient statistic for decision value.**
   Different observation channels with the same or even larger MI can produce lower reward; Stage 3 found strict MI/value reversals.

3. **Resource identity matters.**
   Observation, computation, memory, description length, etc. induce different frontiers. Naive scalarization can reverse game rankings.

4. **Complexity is interface/architecture relative.**
   The same parity policy costs 8 bit queries, 1 parity query, or 4 pairwise-XOR queries under different interfaces. Nim is shallow under a compact XOR program but can look deep under depth-limited minimax.

5. **The two-player surface matters.**
   `V(x,y)` can display skill compression and opponent-relative effects invisible in `R(x)` against a fixed weak opponent.

6. **Learning speed is not frontier geometry alone.**
   The project separates frontier slope, acquisition of resources, and distance-to-frontier.

## Open issue motivating this extension

In sequential games, the policy affects which states are reached. A fixed probe distribution measures a counterfactual workload over states chosen externally; an on-policy distribution measures realized workload but can be strategically manipulated by avoiding costly states.

This repository treats that tension as a **semantic split** rather than trying to select one distribution as universally correct.
