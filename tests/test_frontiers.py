from exposurefrontier.frontier import upper_envelope
from exposurefrontier.route_game import enumerate_route_strategies


def test_frontiers_are_monotone():
    rows = enumerate_route_strategies(p_steps=31)
    budgets = [float(x) for x in range(22)]
    for key in ("peak_cost", "workload"):
        vals = [p.reward for p in upper_envelope(rows, budgets, key)]
        assert all(b + 1e-12 >= a for a, b in zip(vals, vals[1:]))
