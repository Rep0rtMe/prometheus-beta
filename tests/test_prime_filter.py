import pytest
from src.prime_filter import filter_primes

def test_filter_primes_basic():
    """Test basic prime number filtering"""
    assert filter_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 3, 5, 7]

def test_filter_primes_negative_numbers():
    """Test filtering with negative numbers"""
    assert filter_primes([-1, -2, -3, 0, 1, 2, 3, 4, 5]) == [2, 3, 5]

def test_filter_primes_empty_list():
    """Test filtering an empty list"""
    assert filter_primes([]) == []

def test_filter_primes_no_primes():
    """Test list with no prime numbers"""
    assert filter_primes([1, 4, 6, 8, 9, 10]) == []

def test_filter_primes_large_numbers():
    """Test filtering with larger prime and non-prime numbers"""
    assert filter_primes([11, 12, 13, 14, 15, 16, 17, 19, 20, 23, 29]) == [11, 13, 17, 19, 23, 29]

def test_filter_primes_type_error():
    """Test handling of non-integer inputs"""
    with pytest.raises(TypeError):
        filter_primes(['a', 'b', 'c'])

def test_filter_primes_mixed_types():
    """Test handling of mixed type inputs"""
    with pytest.raises(TypeError):
        filter_primes([1, 2, 'three', 4, 5])