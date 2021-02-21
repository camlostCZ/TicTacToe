"""
TicTacToe Game
"""

import sys

from tictactoe.board import Board, BoardError


SYMBOLS = ['X', 'O']

MOVE_CODES = {
    "1": (0, 2),
    "2": (1, 2),
    "3": (2, 2),
    "4": (0, 1),
    "5": (1, 1),
    "6": (2, 1),
    "7": (0, 0),
    "8": (1, 0),
    "9": (2, 0)
}


def input_move(msg: str) -> str:
    """Read move code from user.

    Args:
        msg (str): Message displayed to user

    Returns:
        str: Move code "1" - "9"
    """

    result = ""
    while len(result) != 1 and result not in MOVE_CODES.keys():
        result = input(msg)
    return result


def game():
    """Single game.
    """

    board = Board()
    player_idx = 0
    print(f"\nCurrent position:\n{board.render()}")
    while not board.is_full():
        player_idx = (player_idx + 1) % len(SYMBOLS)
        symbol = SYMBOLS[player_idx]
        code = input_move(f"Enter move code 1 - 9 for '{symbol}': ")
        x, y = MOVE_CODES[code]
        try:
            board.move(symbol, x, y)
            print(f"\nCurrent position:\n{board.render()}")
            if board.is_win():
                print(f"\nPlayer '{symbol}' wins!")
                break
        except BoardError as e:
            # Print error and let player re-enter move
            print(e, file=sys.stderr)
            player_idx = (player_idx + 1) % len(SYMBOLS)

    if board.is_draw():
        print("\nThe game is a draw!")


def main():
    """Main function.

    Repeat the game until player decides to stop.

    """

    try:
        finished = False
        while not finished:
            game()
            finished = input("Do you want to play again? (Y/N)  ").lower() != 'y'
    except KeyboardInterrupt:
        print("Interrupted by user.", file=sys.stderr)

if __name__ == "__main__":
    main()
