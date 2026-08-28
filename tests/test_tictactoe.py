from exposurefrontier.games.tictactoe import (
    EMPTY,
    future_x_exposure_under_br_force,
    future_x_exposure_under_lex_minimax,
    minimax_value,
    trace_o_policy,
)


def test_tictactoe_minimax_draw():
    assert minimax_value(EMPTY * 9) == 0


def test_br_force_preserves_payoff_and_not_lower_exposure():
    _, lex_value = trace_o_policy("lex_minimax")
    _, force_value = trace_o_policy("br_force")
    assert lex_value == force_value == 0
    assert future_x_exposure_under_br_force(EMPTY * 9) >= future_x_exposure_under_lex_minimax(EMPTY * 9)


def test_tictactoe_null_result_is_allowed():
    # Baseline architecture happens to expose the same total workload for the
    # lexicographic and exposure-tie-broken minimax O policies from the empty board.
    assert future_x_exposure_under_br_force(EMPTY * 9) == future_x_exposure_under_lex_minimax(EMPTY * 9)
