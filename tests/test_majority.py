from exposurefrontier.majority import majority_success_probability


def test_majority_endpoints_and_monotonicity():
    vals = [majority_success_probability(21, q) for q in range(22)]
    assert abs(vals[0] - 0.5) < 1e-12
    assert abs(vals[-1] - 1.0) < 1e-12
    assert all(b + 1e-12 >= a for a, b in zip(vals, vals[1:]))
