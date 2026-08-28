# Theory extension: exposure, risk, and epsilon-forceability

This file proposes definitions to test, not conclusions to protect.

## 1. Setup

Consider a two-player zero-sum sequential game. Let `pi` be the focal player's behavioral policy and `sigma` the opponent policy. Let `M` be a declared implementation realizing `pi`.

At each focal decision history `h`, let

`kappa_M(h) >= 0`

be a local implementation-relative resource cost: queries, expanded search nodes, memory accesses, simulated rollouts, etc.

For trajectory `tau`, define cumulative workload

`W_M(tau) = sum_{t: focal acts} kappa_M(h_t)`.

Do not compare different resource types without an explicit conversion.

## 2. Provisioned capability versus exposure

Several non-equivalent objects are useful.

### Local peak capability

`C_local_peak(M) = sup_h kappa_M(h)`

where the domain of `h` must be stated: all legal focal histories, histories reachable under any opponent, or histories under a declared evaluation support.

### Expected realized workload

`C_mean(M; pi,sigma) = E_{tau~P(pi,sigma)}[W_M(tau)]`.

### Tail exposure

For the random variable `W_M`, study upper-tail quantiles and a declared upper-tail CVaR convention. This prevents rare hard trajectories from disappearing inside the mean.

### Trajectory worst case

`C_traj_peak(M; pi,sigma) = ess sup W_M(tau)` under the declared trajectory distribution, or a global worst case if all legal trajectories are included.

These are not interchangeable.

## 3. Opponent exposure set

For fixed `(pi,M)`, define the opponent-achievable set

`A_pi = {(u(pi,sigma), E[W_M|pi,sigma]) : sigma in Sigma}`.

This is the raw payoff-exposure tradeoff controlled by the opponent.

For a minimizing opponent, let

`v(pi) = inf_sigma u(pi,sigma)`.

Define epsilon-best responses

`BR_eps(pi) = {sigma : u(pi,sigma) <= v(pi) + eps}`.

Then define

`F_pi(eps) = sup_{sigma in BR_eps(pi)} E[W_M|pi,sigma]`

`L_pi(eps) = inf_{sigma in BR_eps(pi)} E[W_M|pi,sigma]`

`DeltaF_pi(eps) = F_pi(eps) - L_pi(eps)`.

Interpretation:

- `F_pi(0)`: maximum workload induced by a payoff-optimal opponent response;
- `DeltaF_pi(0)`: exposure leverage available purely through best-response tie-breaking;
- `F_pi(eps)`: maximum workload if the opponent can sacrifice at most `eps` of payoff optimality.

This epsilon form is preferable to relying on exact ties in natural games.

## 4. Immediate propositions to verify

### P-SE-1 Monotonicity

`F_pi(eps)` is nondecreasing in `eps` because `BR_eps1(pi)` is nested inside `BR_eps2(pi)` for `eps1 <= eps2`.

Likewise the feasible set for `L` expands, so `L_pi(eps)` is nonincreasing.

Check sign conventions carefully for maximizing versus minimizing opponents.

### P-SE-2 Tie-breaking characterization

Under a fixed implementation/cost process,

`DeltaF_pi(0) > 0`

exactly when the best-response set contains at least two responses with different expected focal workloads.

This is almost definitional, but useful as a structural diagnostic.

### P-SE-3 Mean does not control peak

The seeded rare-hard-state family gives cost `n` with probability `1/n`, so expected workload is 1 while peak is `n`. Therefore no distribution-free upper bound on peak follows from a bounded mean.

### P-SE-4 Risk hierarchy requires assumptions

Mean, quantiles, CVaR and essential supremum are ordered only under clearly declared conventions/support assumptions. Do not write universal inequalities casually; prove the exact version used.

## 5. Frontier-level objects

For a policy class and declared resource semantics, possible frontiers include:

`R_mean(w) = sup_{pi: C_mean(pi)<=w} r(pi)`

`R_peak(x) = sup_{pi: C_peak(pi)<=x} r(pi)`

and a joint resource surface

`R(x,w) = sup_{pi: C_peak(pi)<=x, C_mean(pi)<=w} r(pi)`.

For strategic exposure, one may instead constrain forceability:

`R_force(z; eps) = sup_{pi: F_pi(eps)<=z} r(pi)`.

Treat this as a candidate object. Audit whether costly-computation game theory or robust/CMDP literature already contains an equivalent formulation.

## 6. Important implementation subtlety

If complexity is defined by `inf_M`, expected runtime can itself depend on the distribution used in the infimum. A machine optimized for frequent states may differ from a worst-case-optimal machine.

Therefore every theorem/experiment must say whether:

1. `M` is fixed first and exposure is measured afterward; or
2. cost is minimized over all implementations realizing `pi` for each evaluation distribution; or
3. one implementation must simultaneously satisfy multiple opponent distributions.

These are distinct problems and may produce different frontiers.

## 7. Candidate new structural question

A useful target is to characterize when opponent forceability vanishes.

Potential sufficient conditions to test:

- all payoff-best-response trajectories induce identical focal decision histories;
- local cost is a function only of payoff-relevant sufficient state that is identical across best responses;
- the opponent's best response is unique;
- the focal implementation has constant local cost across all opponent-reachable histories.

Find weaker/stronger exact statements rather than keeping this list informal.
