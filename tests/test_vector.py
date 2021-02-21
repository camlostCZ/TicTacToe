import pytest

from vector import is_vector_equal

TEST_DATA = [
    (['X', 'X', 'X', 'X'], True),  # Equal
    (['X', 'X', 'O'], False),  # Different
    ([], False),  # Empty
    (None, False)  # None
]


@pytest.mark.parametrize("test_vector, output", TEST_DATA)
def test_is_vector_equal(test_vector, output):
    result = is_vector_equal(test_vector, 'X')
    assert result == output
