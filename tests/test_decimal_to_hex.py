import pytest
from src.decimal_to_hex import decimal_to_hex

def test_decimal_to_hex_zero():
    """Test conversion of zero"""
    assert decimal_to_hex(0) == "0"

def test_decimal_to_hex_small_numbers():
    """Test conversion of small decimal numbers"""
    assert decimal_to_hex(10) == "A"
    assert decimal_to_hex(15) == "F"
    assert decimal_to_hex(16) == "10"

def test_decimal_to_hex_larger_numbers():
    """Test conversion of larger decimal numbers"""
    assert decimal_to_hex(255) == "FF"
    assert decimal_to_hex(4096) == "1000"
    assert decimal_to_hex(123456) == "1E240"

def test_decimal_to_hex_type_error():
    """Test type error handling"""
    with pytest.raises(TypeError, match="Input must be an integer"):
        decimal_to_hex("123")
    with pytest.raises(TypeError, match="Input must be an integer"):
        decimal_to_hex(3.14)

def test_decimal_to_hex_value_error():
    """Test handling of negative numbers"""
    with pytest.raises(ValueError, match="Input must be a non-negative integer"):
        decimal_to_hex(-10)