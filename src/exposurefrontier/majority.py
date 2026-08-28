from __future__ import annotations

from math import comb


def binom_pmf(k: int, n: int, p: float = 0.5) -> float:
    if k < 0 or k > n:
        return 0.0
    return comb(n, k) * (p ** k) * ((1.0 - p) ** (n - k))


def binom_tail_at_least(threshold: int, n: int, p: float = 0.5) -> float:
    if threshold <= 0:
        return 1.0
    if threshold > n:
        return 0.0
    return sum(binom_pmf(k, n, p) for k in range(threshold, n + 1))


def majority_success_probability(n_bits: int, queries: int) -> float:
    """Bayes-optimal accuracy for odd-n majority after observing `queries` bits.

    Bits are IID Bernoulli(1/2), queried coordinates are arbitrary/distinct, and
    the agent must predict the majority of all n bits after exactly q observations.
    """
    if n_bits <= 0 or n_bits % 2 == 0:
        raise ValueError("n_bits must be a positive odd integer")
    if queries < 0 or queries > n_bits:
        raise ValueError("queries must lie in [0, n_bits]")

    majority_threshold = n_bits // 2 + 1
    remaining = n_bits - queries
    accuracy = 0.0
    for observed_ones in range(queries + 1):
        p_obs = binom_pmf(observed_ones, queries, 0.5)
        need_remaining_ones = majority_threshold - observed_ones
        p_majority_one = binom_tail_at_least(need_remaining_ones, remaining, 0.5)
        accuracy += p_obs * max(p_majority_one, 1.0 - p_majority_one)
    return accuracy
