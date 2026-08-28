def test_rare_hard_family():
    for n in (2, 8, 64, 1024):
        p = 1.0 / n
        peak = float(n)
        workload = p * peak
        assert workload == 1.0
        assert peak >= workload
