import pytest
from src.lcm import calculate_lcm

def test_lcm_basic_cases():
    """Test basic LCM calculations"""
    assert calculate_lcm(4, 6) == 12
    assert calculate_lcm(21, 6) == 42
    assert calculate_lcm(17, 5) == 85

def test_lcm_same_number():
    """Test LCM when both numbers are the same"""
    assert calculate_lcm(7, 7) == 7

def test_lcm_one_is_multiple():
    """Test LCM when one number is a multiple of the other"""
    assert calculate_lcm(3, 9) == 9
    assert calculate_lcm(9, 3) == 9

def test_lcm_coprime_numbers():
    """Test LCM of coprime numbers"""
    assert calculate_lcm(5, 7) == 35

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Inputs must be integers"):
        calculate_lcm(3.14, 5)
    
    with pytest.raises(ValueError, match="Inputs must be integers"):
        calculate_lcm("5", 10)

def test_non_positive_inputs():
    """Test error handling for non-positive inputs"""
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        calculate_lcm(0, 5)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        calculate_lcm(5, -3)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        calculate_lcm(-5, -3)