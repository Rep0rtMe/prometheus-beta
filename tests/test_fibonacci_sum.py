import pytest
from src.fibonacci_sum import fibonacci, fibonacciSum

def test_fibonacci_basic():
    """Test basic Fibonacci sequence generation"""
    assert fibonacci(0) == [0]
    assert fibonacci(1) == [0, 1]
    assert fibonacci(2) == [0, 1, 2]
    assert fibonacci(10) == [0, 1, 2, 3, 5, 8]
    assert fibonacci(20) == [0, 1, 2, 3, 5, 8, 13]

def test_fibonacci_error_handling():
    """Test error handling for Fibonacci function"""
    with pytest.raises(ValueError):
        fibonacci(-1)
    with pytest.raises(ValueError):
        fibonacci("not an integer")

def test_fibonacciSum_basic():
    """Test basic Fibonacci sum calculation"""
    assert fibonacciSum([1]) == 1  # 0 + 1
    assert fibonacciSum([2]) == 3  # 0 + 1 + 2
    assert fibonacciSum([3]) == 6  # 0 + 1 + 2 + 3
    assert fibonacciSum([5]) == 16  # 0 + 1 + 2 + 3 + 5 + 5
    assert fibonacciSum([10]) == 33  # 0 + 1 + 2 + 3 + 5 + 8 + 13

def test_fibonacciSum_multiple_nums():
    """Test Fibonacci sum with multiple input numbers"""
    assert fibonacciSum([2, 5]) == 16  # Same as [5]
    assert fibonacciSum([1, 2, 3]) == 6  # Same as [3]
    assert fibonacciSum([10, 20]) == 88  # Sum of Fibonacci up to 20

def test_fibonacciSum_error_handling():
    """Test error handling for Fibonacci sum function"""
    with pytest.raises(ValueError):
        fibonacciSum([])
    with pytest.raises(ValueError):
        fibonacciSum([-1, 2, 3])
    with pytest.raises(ValueError):
        fibonacciSum("not a list")
    with pytest.raises(ValueError):
        fibonacciSum([1, "not an int", 3])