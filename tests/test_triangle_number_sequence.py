import pytest
from src.triangle_number_sequence import generate_triangle_numbers

def test_generate_triangle_numbers_basic():
    """Test basic functionality of triangle number generation"""
    assert generate_triangle_numbers(0) == []
    assert generate_triangle_numbers(1) == [0]
    assert generate_triangle_numbers(5) == [0, 1, 3, 6, 10]

def test_generate_triangle_numbers_length():
    """Test that the function returns the correct number of triangle numbers"""
    for i in range(10):
        assert len(generate_triangle_numbers(i)) == i

def test_generate_triangle_numbers_values():
    """Verify specific triangle number calculations"""
    # Manually calculated triangle numbers to verify
    expected = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
    assert generate_triangle_numbers(10) == expected

def test_generate_triangle_numbers_error_handling():
    """Test error handling for invalid inputs"""
    # Test negative input
    with pytest.raises(ValueError, match="Number of triangle numbers must be non-negative"):
        generate_triangle_numbers(-1)
    
    # Test non-integer input
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_triangle_numbers(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_triangle_numbers("5")
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        generate_triangle_numbers(None)