"""
Helper module used for vector operations.
"""

from typing import Any


def is_vector_equal(vector: list[Any], value: Any) -> bool:
    """Test if all values in vector are equal to a value.

    Args:
        vector (list[Any]): Vector to test
        value (Any): Value used for comparison

    Returns:
        bool: True if all values are equal to the value
    """

    return len([x for x in vector if x == value]) == len(vector)
