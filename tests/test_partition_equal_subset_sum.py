import pytest
from src.partition_equal_subset_sum import can_partition

def test_partition_possible():
    """Test cases where partitioning is possible"""
    assert can_partition([1, 5, 11, 5]) == True
    assert can_partition([1, 2, 3, 4, 5, 6, 7]) == True
    assert can_partition([2, 2, 3, 5]) == True

def test_partition_impossible():
    """Test cases where partitioning is impossible"""
    assert can_partition([1, 2, 3, 5]) == False
    assert can_partition([1, 3, 4]) == False
    assert can_partition([1, 1, 1, 1, 1, 1, 1]) == False

def test_edge_cases():
    """Test edge cases"""
    assert can_partition([]) == False
    assert can_partition([1]) == False
    assert can_partition([2, 2]) == True
    assert can_partition([1, 1]) == True

def test_large_numbers():
    """Test with larger numbers"""
    large_test_list = [100, 100, 100, 100, 100, 100, 100, 100]
    assert can_partition(large_test_list) == True

def test_negative_or_zero_cases():
    """Verify behavior with negative or zero values"""
    with pytest.raises(TypeError):
        can_partition([1, -2, 3])
    
    with pytest.raises(TypeError):
        can_partition([0, 1, 2])

def test_type_handling():
    """Ensure function handles incorrect input types"""
    with pytest.raises(TypeError):
        can_partition("not a list")
    
    with pytest.raises(TypeError):
        can_partition(None)