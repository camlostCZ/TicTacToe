"""
Array2D module

Compatibility: Python 3.9+
"""

from typing import Any


class CoordinateError(Exception):
    """Exception raised in case of wrong coordinates.
    """
    pass


class Array2D:
    """Array2D class is a base class for Board class.
    """

    def __init__(self, size_x: int, size_y: int, empty_field: Any):
        """Class constructor.

        Initialize 2D array with empty values, set sizes.

        Args:
            size_x (int): Width of array (number of columns)
            size_y (int): Height of array (number of rows)
            empty_field (Any): Initial / empty value
        """

        self.size_x = size_x
        self.size_y = size_y
        self._fields = []
        self._empty_field = empty_field
        self.clear()


    def clear(self):
        """Clear array.

        Set all fields to empty value.
        """

        self._fields = []
        for _ in range(self.size_y):
            row = [self._empty_field] * self.size_x
            self._fields.append(row)


    def get_vector(self, x: int, y: int, dx: int, dy: int) -> list[Any]:
        """Get vector.

        Args:
            x (int): Column of starting field
            y (int): Row of starting field
            dx (int): Delta X (usually -1, 0 or 1) used to iterate over fields
            dy (int): Delta Y (usually -1, 0, or 1) used to iterate over fields

        Returns:
            list[Any]: List of fields in the vector
        """

        if x not in range(self.size_x) or y not in range(self.size_y):
            raise CoordinateError(f"Invalid coordinates [{x}, {y}]")

        if dx == 0 and dy == 0:
            raise ValueError("Both steps cannot be 0")

        result = []
        i, j = (x, y)
        while i in range(self.size_x) and j in range(self.size_y):
            result.append(self._fields[j][i])
            i, j = (i + dx, j + dy)
        return result


    def get_column(self, x: int) -> list[Any]:
        """Get fields from column.

        Args:
            x (int): Column of starting field

        Returns:
            list[Any]: List of fields in the column
        """

        return self.get_vector(x, 0, 0, 1)


    def get_row(self, y: int) -> list[Any]:
        """Get fields from row.

        Args:
            y (int): Row of starting field

        Returns:
            list[Any]: List of fields in the row
        """

        return self.get_vector(0, y, 1, 0)
