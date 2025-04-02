import pytest
from src.library_sort import library_sort

def test_library_sort_basic():
    """Test basic sorting functionality."""
    arr = [5, 2, 9, 1, 7, 6]
    assert library_sort(arr) == [1, 2, 5, 6, 7, 9]

def test_library_sort_already_sorted():
    """Test sorting an already sorted list."""
    arr = [1, 2, 3, 4, 5]
    assert library_sort(arr) == [1, 2, 3, 4, 5]

def test_library_sort_reverse_sorted():
    """Test sorting a reverse-sorted list."""
    arr = [5, 4, 3, 2, 1]
    assert library_sort(arr) == [1, 2, 3, 4, 5]

def test_library_sort_duplicates():
    """Test sorting a list with duplicate elements."""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    assert library_sort(arr) == [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

def test_library_sort_empty_list():
    """Test sorting an empty list."""
    arr = []
    assert library_sort(arr) == []

def test_library_sort_single_element():
    """Test sorting a list with a single element."""
    arr = [42]
    assert library_sort(arr) == [42]

def test_library_sort_invalid_input():
    """Test that an error is raised for non-list input."""
    with pytest.raises(TypeError):
        library_sort("not a list")

def test_library_sort_mixed_types():
    """Test sorting a list with mixed comparable types."""
    arr = [5, 2, 'a', 'c', 'b', 1]
    assert library_sort(arr) == [1, 2, 5, 'a', 'b', 'c']

def test_library_sort_negative_numbers():
    """Test sorting a list with negative numbers."""
    arr = [-5, -2, -9, -1, -7, -6]
    assert library_sort(arr) == [-9, -7, -6, -5, -2, -1]

def test_library_sort_large_list():
    """Test sorting a larger list."""
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3]
    assert library_sort(arr) == [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]