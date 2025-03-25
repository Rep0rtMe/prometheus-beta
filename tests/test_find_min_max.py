import pytest
from src.find_min_max import find_min_max

def test_find_min_max_typical_case():
    """Test finding min and max in a typical numeric list."""
    assert find_min_max([1, 5, 3, 9, 2]) == (1, 9)

def test_find_min_max_with_negative_numbers():
    """Test finding min and max with negative numbers."""
    assert find_min_max([-1, -5, 0, 3, 9]) == (-5, 9)

def test_find_min_max_with_floats():
    """Test finding min and max with floating point numbers."""
    assert find_min_max([1.5, 3.7, -2.1, 0.0]) == (-2.1, 3.7)

def test_find_min_max_single_element():
    """Test finding min and max with a single element."""
    assert find_min_max([42]) == (42, 42)

def test_find_min_max_empty_list_raises_error():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_min_max([])

def test_find_min_max_non_list_input_raises_error():
    """Test that non-list input raises a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_min_max("not a list")

def test_find_min_max_non_numeric_list_raises_error():
    """Test that a list with non-numeric elements raises a TypeError."""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_min_max([1, 2, "3", 4])

def test_find_min_max_mixed_numeric_types():
    """Test finding min and max with mixed numeric types (int and float)."""
    assert find_min_max([1, 2.5, 3, 4.7]) == (1, 4.7)