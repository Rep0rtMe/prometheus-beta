import pytest
from src.sum_of_digits import sum_of_digits

def test_sum_of_digits_positive_numbers():
    """Test sum of digits for various positive numbers."""
    assert sum_of_digits(123) == 6  # 1 + 2 + 3
    assert sum_of_digits(456) == 15  # 4 + 5 + 6
    assert sum_of_digits(9) == 9
    assert sum_of_digits(0) == 0

def test_sum_of_digits_large_number():
    """Test sum of digits for larger numbers."""
    assert sum_of_digits(1234567) == 28  # 1+2+3+4+5+6+7
    assert sum_of_digits(9999999) == 63  # 9+9+9+9+9+9+9

def test_sum_of_digits_invalid_input():
    """Test error handling for invalid inputs."""
    # Negative number
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        sum_of_digits(-123)
    
    # Non-integer inputs
    with pytest.raises(ValueError, match="Input must be an integer"):
        sum_of_digits(3.14)
    
    with pytest.raises(ValueError, match="Input must be an integer"):
        sum_of_digits("123")
    
    with pytest.raises(ValueError, match="Input must be an integer"):
        sum_of_digits(None)