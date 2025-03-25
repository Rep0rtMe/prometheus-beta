import pytest
import math
from src.recursive_power import recursive_power

def test_positive_integer_power():
    """Test power calculation with positive integer exponents"""
    assert recursive_power(2, 3) == 8.0
    assert recursive_power(5, 2) == 25.0
    assert recursive_power(10, 1) == 10.0

def test_zero_power():
    """Test power calculation with zero exponent"""
    assert recursive_power(5, 0) == 1.0
    assert recursive_power(-3, 0) == 1.0
    assert recursive_power(0, 0) == 1.0

def test_negative_power():
    """Test power calculation with negative exponents"""
    assert recursive_power(2, -2) == 0.25
    assert recursive_power(10, -1) == 0.1
    assert math.isclose(recursive_power(3, -3), 1/27, rel_tol=1e-10)

def test_float_base():
    """Test power calculation with float bases"""
    assert math.isclose(recursive_power(2.5, 2), 6.25, rel_tol=1e-10)
    assert math.isclose(recursive_power(1.5, 3), 3.375, rel_tol=1e-10)

def test_error_handling():
    """Test error handling for invalid inputs"""
    # Type errors
    with pytest.raises(TypeError, match="Base must be a number"):
        recursive_power("2", 3)
    
    with pytest.raises(TypeError, match="Exponent must be an integer"):
        recursive_power(2, 3.5)
    
    # Zero to negative power
    with pytest.raises(ValueError, match="Cannot raise 0 to a negative power"):
        recursive_power(0, -1)

def test_base_one():
    """Test power calculation with base 1"""
    assert recursive_power(1, 5) == 1.0
    assert recursive_power(1, -3) == 1.0

def test_large_exponent():
    """Test power calculation with relatively large exponents"""
    assert recursive_power(2, 10) == 1024.0
    assert recursive_power(1.5, 8) == 1.5 ** 8