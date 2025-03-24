import pytest
from src.find_array_minimum import find_minimum

def test_find_minimum_basic():
    """Test finding minimum in a basic list of integers"""
    assert find_minimum([1, 2, 3, 4, 5]) == 1
    assert find_minimum([5, 4, 3, 2, 1]) == 1
    assert find_minimum([-1, 0, 1]) == -1

def test_find_minimum_float():
    """Test finding minimum in a list with floating-point numbers"""
    assert find_minimum([1.5, 2.3, -0.5, 3.7]) == -0.5

def test_find_minimum_single_element():
    """Test finding minimum in a single-element list"""
    assert find_minimum([42]) == 42

def test_find_minimum_negative_numbers():
    """Test finding minimum with only negative numbers"""
    assert find_minimum([-5, -3, -10, -1]) == -10

def test_empty_array_raises_error():
    """Test that an empty array raises a ValueError"""
    with pytest.raises(ValueError, match="Cannot find minimum of an empty array"):
        find_minimum([])

def test_non_list_input_raises_error():
    """Test that non-list inputs raise a TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_minimum("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        find_minimum(123)

def test_non_numeric_elements_raises_error():
    """Test that lists with non-numeric elements raise a TypeError"""
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_minimum([1, 2, "three"])
    with pytest.raises(TypeError, match="All elements must be numeric"):
        find_minimum([1, 2, None])