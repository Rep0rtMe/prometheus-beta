import pytest
from src.fibonacci_subsequence import generate_fibonacci_subsequence

def test_generate_fibonacci_subsequence_zero():
    """Test generation of subsequence for n = 0"""
    assert generate_fibonacci_subsequence(0) == [0]

def test_generate_fibonacci_subsequence_non_zero():
    """Test generation of subsequence for various non-zero inputs"""
    # Test cases where even-indexed sum equals input
    test_cases = [
        (1, [0, 1, 1]),
        (2, [0, 1, 1, 2]),
        (3, [0, 1, 1, 2, 3]),
        (4, [0, 1, 1, 2, 3, 5]),
        (5, [0, 1, 1, 2, 3, 5, 8])
    ]
    
    for n, expected in test_cases:
        result = generate_fibonacci_subsequence(n)
        assert result == expected
        
        # Verify the sum of even-indexed numbers
        even_indexed_sum = sum(result[::2])
        assert even_indexed_sum == n

def test_generate_fibonacci_subsequence_negative():
    """Test that negative input raises ValueError"""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        generate_fibonacci_subsequence(-1)

def test_generate_fibonacci_subsequence_impossible():
    """Test that impossible inputs raise ValueError"""
    # A very large number that can't be generated 
    with pytest.raises(ValueError, match="Cannot generate a subsequence"):
        generate_fibonacci_subsequence(10**6)