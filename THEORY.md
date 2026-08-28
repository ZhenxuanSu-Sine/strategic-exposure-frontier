# Theory: Strategic Exposure Frontiers

## 1. From scalar implementation cost to a cost process

Keep the Stage-3 implementation discipline. An implementation `M` has behavior `Beh(M)=π`, but now resource use can depend on the decision history `h`:

\[
\ell_M(h) \ge 0.
\]

Examples:

- number of state queries made on this decision;
- search nodes expanded at this move;
- memory reads/writes;
- tokens/symbols inspected;
- wall-clock compute under a fixed hardware model.

The same implementation can therefore have a large peak requirement but low average workload.

## 2. Four distinct resource semantics

### 2.1 Peak capability

\[
c_{\mathrm{peak}}(\pi)
= \inf_{M:\mathrm{Beh}(M)=\pi}\sup_{h\in\mathcal H_\pi}\ell_M(h).
\]

Interpretation: the largest local resource burst the player must be capable of handling.

### 2.2 Probe workload

For an externally chosen probe distribution `μ` over histories:

\[
c_\mu(\pi)
= \inf_{M:\mathrm{Beh}(M)=\pi}
\mathbb E_{h\sim\mu}[\ell_M(h)].
\]

Interpretation: counterfactual average resource use under a declared evaluation distribution.

### 2.3 On-policy workload

Let `P^π` be the trajectory distribution induced by `π` in a PVE/MDP setting:

\[
c_{\mathrm{on}}(\pi)
= \inf_{M:\mathrm{Beh}(M)=\pi}
\mathbb E_{\tau\sim P^\pi}
\left[\sum_t \ell_M(H_t)\right].
\]

Interpretation: realized expected resource consumption during actual play.

### 2.4 Opponent-forceable workload

For a two-player game and opponent policy `σ`:

\[
c_{\mathrm{exp}}(\pi;\sigma)
= \inf_{M:\mathrm{Beh}(M)=\pi}
\mathbb E_{\tau\sim P^{\pi,\sigma}}
\left[\sum_t \ell_M(H_t)\right].
\]

Define worst-case exposure

\[
c_{\mathrm{force}}(\pi)
= \inf_{M:\mathrm{Beh}(M)=\pi}
\sup_{\sigma\in\Sigma}
\mathbb E_{\tau\sim P^{\pi,\sigma}}
\left[\sum_t \ell_M(H_t)\right].
\]

A stricter game-theoretic variant restricts the opponent to payoff-best-responses before maximizing exposure:

\[
c_{\mathrm{BR-force}}(\pi)
= \inf_M\sup_{\sigma\in BR(\pi)}
\mathbb E\left[\sum_t\ell_M(H_t)\right].
\]

This asks whether an opponent can increase your workload **without sacrificing strategic value**.

## 3. New frontiers

### Capability frontier

\[
R_{\mathrm{peak}}(x)=\sup_{c_{\mathrm{peak}}(\pi)\le x}J(\pi).
\]

### Workload frontier

\[
R_{\mathrm{on}}(w)=\sup_{c_{\mathrm{on}}(\pi)\le w}J(\pi).
\]

### Joint capability/workload frontier

\[
R(x,w)=\sup_{\substack{c_{\mathrm{peak}}(\pi)\le x\\c_{\mathrm{on}}(\pi)\le w}}J(\pi).
\]

The two-dimensional object is often the safest primary object. A low expected workload does not imply low capability.

## 4. Fundamental counterexample: bounded workload does not bound capability

Consider a family indexed by `n`. A hard decision occurs with probability `1/n`. Solving it requires a burst of `n` queries. Then

\[
c_{\mathrm{on}}=\frac1n\cdot n=1,
\qquad
c_{\mathrm{peak}}=n.
\]

Thus `c_on` remains constant while the required peak capability diverges.

**Consequence:** an on-policy expected-cost budget alone cannot be interpreted as a bound on player capability.

This does *not* make on-policy workload useless. It measures a different object: actual resource consumption.

## 5. Strategic avoidance and forceability

A sequential game may contain costly states that are:

- avoidable by the player;
- encountered only under mistakes;
- induced by a particular opponent;
- forceable by every payoff-optimal opponent;
- forceable only by an opponent willing to sacrifice payoff.

These cases should not be collapsed into one "depth" label.

Define an exposure gap relative to a reference opponent `σ0`:

\[
G_{\mathrm{force}}(\pi;\sigma_0)
= c_{\mathrm{BR-force}}(\pi)-c_{\mathrm{exp}}(\pi;\sigma_0).
\]

Large gap means routine play understates the resource burden a rational opponent can expose.

## 6. Relationship to fixed-probe vs on-policy NPIC

This project does **not** reinstate `I(S;A)` as the complexity measure. The fixed/on-policy distinction is more general than mutual information.

The proposed extension applies to any local cost process tied to an explicit implementation architecture: queries, search, memory, description fragments, or other resource accounting.

## 7. Directed information

Directed/causal information remains relevant if the resource itself is information flow across time. It should be treated as **one candidate sequential information resource**, not as a universal replacement for implementation complexity.

A later stage may compare:

- implementation workload;
- causal/directed information workload;
- memory-state complexity;

under the same trajectory distributions.
