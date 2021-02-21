import pytest

from array2d import Array2D, CoordinateError

@pytest.fixture
def new_array():
    empty = ' '
    result = Array2D(4, 3, empty)
    result._fields[0][0] = 'A'
    return result


def test_a2d_clear(new_array):
    """Test if clear replaces all fields with empty value.
    """

    arr = new_array
    arr.clear()

    count = 0
    for row in range(arr.size_y):
        count += len([x for x in arr._fields[row] if x == ' '])

    assert count == arr.size_x * arr.size_y


def test_get_vector(new_array):
    """Test Array2D.get_vector() with various parameters.
    """

    assert "".join(new_array.get_vector(0, 0, 1, 1)) == "A  "
    assert "".join(new_array.get_vector(1, 0, -1, 1)) == "  "
    assert "".join(new_array.get_vector(2, 2, -1, -1)) == "  A"


def test_get_row(new_array):
    """Test Array2D.get_row().
    """

    assert "".join(new_array.get_row(0)) == "A   "


def test_get_column(new_array):
    """Test Array2D.get_column().
    """

    assert "".join(new_array.get_column(0)) == "A  "


def test_coordinate_exception(new_array):
    """Test if invalid coordinates raise an exception.
    """

    with pytest.raises(CoordinateError):
        new_array.get_vector(6, 1, 1, 0)

def test_get_vector_step(new_array):
    """Check if an exception is raised when steps are equal to zero.
    """

    with pytest.raises(ValueError):
        new_array.get_vector(0, 0, 0, 0)
