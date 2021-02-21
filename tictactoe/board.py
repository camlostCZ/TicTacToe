"""
TicTacToe board module

Compatibility: Python 3.9+

Usage:
    - Create a board by instantiating the Board class.
    - Make moves by calling its move() method repeatedly.
    - After each move, check for win using is_win() and for a draw using is_draw().
      If either of them returns True, game ends.
"""

from .array2d import Array2D, CoordinateError
from .vector import is_vector_equal


DEFAULT_BOARD_SIZE = 3


class BoardError(Exception):
    """BoardError exception.

    Used in case of illegal move.
    """


class Board(Array2D):
    """TicTacToe Board

    Board contains a square array of fields, each of them being empty
    or containing a player's symbol.
    """

    def __init__(self, size: int = DEFAULT_BOARD_SIZE):
        """Constructor.

        Set size and clear board.

        Args:
            size (int): Board size
        """

        super().__init__(size, size, ' ')
        self._moves_left = size ** 2
        self._f_win = False


    def move(self, symbol: str, x: int, y: int):  # pylint: disable=invalid-name
        """Make a move on the board.

        Args:
            symbol (str): Symbol (usually 'X' or 'O')
            x (int): Column coordinate
            y (int): Row coordinate
        """

        if x not in range(self.size_x) or y not in range(self.size_y):
            raise CoordinateError(f"Invalid coordinates [{x}, {y}]")

        if self._fields[x][y] == self._empty_field:
            self._fields[x][y] = symbol
            self._moves_left += -1
            self._f_win = self._check_win(x, y)
        else:
            raise BoardError(f"Field [{x}, {y}] not empty")


    def is_full(self) -> bool:
        """Check if board is full.

        Returns:
            bool: True if board is full, False otherwise
        """

        return self._moves_left == 0


    def is_draw(self) -> bool:
        """Check if current position is a draw.

        Returns:
            bool: True if game is a draw, False owtherwise.
        """

        return self.is_full() and not self.is_win()


    def is_win(self) -> bool:
        """Check if current position is a win.

        Returns:
            bool: True in case of a win, False otherwise
        """

        return self._f_win


    def render(self) -> str:
        """Render board to string.

        Returns:
            str: String representation of current board position
        """

        result = ""
        for row_idx in range(self.size_y):
            result += " | ".join(self.get_row(row_idx)) + "\n"
            result += "-" * (3 * self.size_x) + "\n"
        return result


    def _build_win_vectors(self, x: int, y: int) -> list[list[str]]:  # pylint: disable=invalid-name
        """Build list of vectors used to test for win.

        Args:
            x (int): X coordinate of last move
            y (int): Y coordinate of last move

        Returns:
            list[list[str]]: List of vectors
        """

        vectors: list[list[str]] = [
            self.get_column(x),
            self.get_row(y),
        ]
        if x == y:
            vectors.append(self.get_vector(0, 0, 1, 1))
            vectors.append(self.get_vector(self.size_x - 1, 0, -1, 1))
        return vectors


    def _check_win(self, x: int, y: int) -> bool:  # pylint: disable=invalid-name
        """Check if last move was a winnig one.

        Args:
            x (int): X coordinate of last move
            y (int): Y coordinate of last move

        Returns:
            bool: True if last move was a winning one, False otherwise
        """

        vectors: list[list[str]] = self._build_win_vectors(x, y)
        tests = (is_vector_equal(item, self._fields[x][y]) for item in vectors)
        return self._fields[x][y] != self._empty_field and len([x for x in tests if x]) > 0
