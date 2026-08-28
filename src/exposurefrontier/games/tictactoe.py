from __future__ import annotations

from functools import lru_cache
from typing import Iterable

EMPTY = "."
X = "X"
O = "O"
WIN_LINES = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
)


def winner(board: str) -> str | None:
    for a, b, c in WIN_LINES:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    return None


def terminal_value(board: str) -> int | None:
    w = winner(board)
    if w == X:
        return 1
    if w == O:
        return -1
    if EMPTY not in board:
        return 0
    return None


def legal_moves(board: str) -> tuple[int, ...]:
    return tuple(i for i, c in enumerate(board) if c == EMPTY)


def apply_move(board: str, move: int, player: str) -> str:
    if board[move] != EMPTY:
        raise ValueError("illegal move")
    return board[:move] + player + board[move + 1:]


def next_player(board: str) -> str:
    nx = board.count(X)
    no = board.count(O)
    if nx == no:
        return X
    if nx == no + 1:
        return O
    raise ValueError("invalid board counts")


@lru_cache(maxsize=None)
def minimax_value(board: str) -> int:
    tv = terminal_value(board)
    if tv is not None:
        return tv
    player = next_player(board)
    values = [minimax_value(apply_move(board, m, player)) for m in legal_moves(board)]
    return max(values) if player == X else min(values)


def minimax_moves(board: str) -> tuple[int, ...]:
    tv = terminal_value(board)
    if tv is not None:
        return ()
    player = next_player(board)
    scored = [(m, minimax_value(apply_move(board, m, player))) for m in legal_moves(board)]
    target = max(v for _, v in scored) if player == X else min(v for _, v in scored)
    return tuple(m for m, v in scored if v == target)


@lru_cache(maxsize=None)
def naive_minimax_node_count(board: str) -> int:
    """Nodes expanded by full minimax from board, no cache/pruning in the modeled solver.

    We memoize this *count calculation* for experiment speed. The modeled invocation
    still corresponds to recursively expanding every descendant node.
    """
    if terminal_value(board) is not None:
        return 1
    player = next_player(board)
    return 1 + sum(
        naive_minimax_node_count(apply_move(board, m, player))
        for m in legal_moves(board)
    )


def x_policy_move(board: str) -> int:
    if next_player(board) != X:
        raise ValueError("not X turn")
    return min(minimax_moves(board))


def o_lex_minimax_move(board: str) -> int:
    if next_player(board) != O:
        raise ValueError("not O turn")
    return min(minimax_moves(board))


@lru_cache(maxsize=None)
def future_x_exposure_under_lex_minimax(board: str) -> float:
    tv = terminal_value(board)
    if tv is not None:
        return 0.0
    player = next_player(board)
    if player == X:
        cost = float(naive_minimax_node_count(board))
        child = apply_move(board, x_policy_move(board), X)
        return cost + future_x_exposure_under_lex_minimax(child)
    move = o_lex_minimax_move(board)
    return future_x_exposure_under_lex_minimax(apply_move(board, move, O))


@lru_cache(maxsize=None)
def future_x_exposure_under_br_force(board: str) -> float:
    """O chooses, among minimax-best moves, the one maximizing future X exposure."""
    tv = terminal_value(board)
    if tv is not None:
        return 0.0
    player = next_player(board)
    if player == X:
        cost = float(naive_minimax_node_count(board))
        child = apply_move(board, x_policy_move(board), X)
        return cost + future_x_exposure_under_br_force(child)
    return max(
        future_x_exposure_under_br_force(apply_move(board, m, O))
        for m in minimax_moves(board)
    )


@lru_cache(maxsize=None)
def future_x_exposure_under_random_o(board: str) -> float:
    tv = terminal_value(board)
    if tv is not None:
        return 0.0
    player = next_player(board)
    if player == X:
        cost = float(naive_minimax_node_count(board))
        child = apply_move(board, x_policy_move(board), X)
        return cost + future_x_exposure_under_random_o(child)
    moves = legal_moves(board)
    return sum(
        future_x_exposure_under_random_o(apply_move(board, m, O))
        for m in moves
    ) / len(moves)


@lru_cache(maxsize=None)
def expected_value_x_vs_random_o(board: str) -> float:
    tv = terminal_value(board)
    if tv is not None:
        return float(tv)
    player = next_player(board)
    if player == X:
        return expected_value_x_vs_random_o(apply_move(board, x_policy_move(board), X))
    moves = legal_moves(board)
    return sum(expected_value_x_vs_random_o(apply_move(board, m, O)) for m in moves) / len(moves)


def trace_o_policy(policy: str) -> tuple[list[dict[str, object]], int]:
    board = EMPTY * 9
    trace: list[dict[str, object]] = []
    while terminal_value(board) is None:
        player = next_player(board)
        if player == X:
            cost = naive_minimax_node_count(board)
            move = x_policy_move(board)
            trace.append({"board": board, "player": X, "move": move, "x_search_nodes": cost})
        else:
            if policy == "lex_minimax":
                move = o_lex_minimax_move(board)
            elif policy == "br_force":
                candidates = minimax_moves(board)
                move = max(
                    candidates,
                    key=lambda m: (future_x_exposure_under_br_force(apply_move(board, m, O)), -m),
                )
            else:
                raise ValueError(policy)
            trace.append({"board": board, "player": O, "move": move, "x_search_nodes": 0})
        board = apply_move(board, move, player)
    return trace, int(terminal_value(board))
