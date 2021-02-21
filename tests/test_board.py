import pytest

from tictactoe.board import Board


def empty_board():
    result = Board()
    return result


def draw_board():
    result = Board()
    result.move('O', 1, 1)
    result.move('X', 0, 2)
    result.move('O', 1, 0)
    result.move('X', 1, 2)
    result.move('O', 2, 2)
    result.move('X', 0, 0)
    result.move('O', 0, 1)
    result.move('X', 2, 1)
    result.move('O', 2, 0)
    return result


def win_board():
    result = Board()
    result.move('X', 0, 0)
    result.move('X', 1, 1)
    result.move('X', 2, 2)
    return result


FULL_DATA = [
    (empty_board(), False),
    (draw_board(), True),
    (win_board(), False)
]


@pytest.mark.parametrize("bd, output", FULL_DATA)
def test_board_is_full(bd, output):
    assert bd.is_full() == output


WIN_DATA = [
    (empty_board(), False),
    (draw_board(), False),
    (win_board(), True)
]

@pytest.mark.parametrize("bd, output", WIN_DATA)
def test_board_is_win(bd, output):
    assert bd.is_win() == output