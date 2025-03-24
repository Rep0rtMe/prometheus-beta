import pytest
from src.swap_numbers import swap_numbers

def test_swap_positive_numbers():
    """Test swapping two positive numbers"""
    a, b = 5, 10
    swapped_b, swapped_a = swap_numbers(a, b)
    assert swapped_a == a
    assert swapped_b == b

def test_swap_negative_numbers():
    """Test swapping two negative numbers"""
    a, b = -5, -10
    swapped_b, swapped_a = swap_numbers(a, b)
    assert swapped_a == a
    assert swapped_b == b

def test_swap_zero():
    """Test swapping when one number is zero"""
    a, b = 0, 15
    swapped_b, swapped_a = swap_numbers(a, b)
    assert swapped_a == a
    assert swapped_b == b

def test_swap_same_number():
    """Test swapping identical numbers"""
    a, b = 7, 7
    swapped_b, swapped_a = swap_numbers(a, b)
    assert swapped_a == a
    assert swapped_b == b

def test_invalid_input_type():
    """Test that TypeError is raised for non-integer inputs"""
    with pytest.raises(TypeError):
        swap_numbers(5.5, 10)
    
    with pytest.raises(TypeError):
        swap_numbers("5", "10")
    
    with pytest.raises(TypeError):
        swap_numbers([5], [10])