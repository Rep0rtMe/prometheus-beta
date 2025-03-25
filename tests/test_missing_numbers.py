import pytest
from src.missing_numbers import find_missing_numbers

def test_missing_numbers_ascending():
    """Test missing numbers in an ascending sorted array."""
    assert find_missing_numbers([1, 3, 5, 7]) == [2, 4, 6]

def test_missing_numbers_descending():
    """Test missing numbers in a descending sorted array."""
    assert find_missing_numbers([7, 5, 3, 1]) == [6, 4, 2]

def test_no_missing_numbers():
    """Test an array with no missing numbers."""
    assert find_missing_numbers([1, 2, 3, 4, 5]) == []

def test_large_array():
    """Test a larger array with missing numbers."""
    assert find_missing_numbers([2, 4, 6, 8, 10, 12]) == [3, 5, 7, 9, 11]

def test_edge_case_single_element():
    """Test an array with a single element."""
    assert find_missing_numbers([5]) == []

def test_edge_case_empty_array():
    """Test an empty array."""
    assert find_missing_numbers([]) == []

def test_invalid_input_non_positive():
    """Test that non-positive integers raise a ValueError."""
    with pytest.raises(ValueError):
        find_missing_numbers([0, 1, 2])
    
    with pytest.raises(ValueError):
        find_missing_numbers([-1, 1, 2])

def test_invalid_input_non_integer():
    """Test that non-integer inputs raise a ValueError."""
    with pytest.raises(ValueError):
        find_missing_numbers([1, 2, '3'])
    
    with pytest.raises(ValueError):
        find_missing_numbers([1.5, 2, 3])