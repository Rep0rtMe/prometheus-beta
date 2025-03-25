import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from radix_sort import radix_sort

def test_radix_sort_basic():
    """Test basic sorting of positive integers"""
    assert radix_sort([170, 45, 75, 90, 802, 24, 2, 66]) == [2, 24, 45, 66, 75, 90, 170, 802]

def test_radix_sort_empty_list():
    """Test sorting an empty list"""
    assert radix_sort([]) == []

def test_radix_sort_single_element():
    """Test sorting a list with a single element"""
    assert radix_sort([42]) == [42]

def test_radix_sort_already_sorted():
    """Test sorting an already sorted list"""
    assert radix_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_radix_sort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    assert radix_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_radix_sort_with_zeros():
    """Test sorting with zero values"""
    assert radix_sort([0, 0, 0, 1, 0]) == [0, 0, 0, 0, 1]

def test_radix_sort_large_values():
    """Test sorting with large values"""
    large_list = [1000000, 10, 1000, 100000, 10000]
    assert radix_sort(large_list) == [10, 1000, 10000, 100000, 1000000]

def test_invalid_input_negative_numbers():
    """Test that negative numbers raise a ValueError"""
    with pytest.raises(ValueError, match="List must contain only non-negative integers"):
        radix_sort([-1, 2, 3])

def test_invalid_input_non_integer():
    """Test that non-integer inputs raise a TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        radix_sort("not a list")

def test_invalid_input_mixed_types():
    """Test that mixed type inputs raise a TypeError"""
    with pytest.raises(ValueError, match="List must contain only non-negative integers"):
        radix_sort([1, 2, "3"])