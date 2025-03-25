import pytest
import random
from src.random_case_converter import convert_to_alternating_random_case

def test_convert_to_alternating_random_case_basic():
    """Test basic functionality of the random case converter."""
    # Set a fixed seed for reproducibility
    random.seed(42)
    
    # Test a simple string
    result = convert_to_alternating_random_case("hello")
    assert len(result) == 5
    assert result.lower() == "hello"

def test_convert_to_alternating_random_case_empty_string():
    """Test conversion of an empty string."""
    assert convert_to_alternating_random_case("") == ""

def test_convert_to_alternating_random_case_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        convert_to_alternating_random_case(123)
    
    with pytest.raises(TypeError):
        convert_to_alternating_random_case(None)

def test_convert_to_alternating_random_case_randomness():
    """Verify that the function introduces randomness."""
    # Set a fixed seed for reproducibility
    random.seed(42)
    
    # Run multiple times to check variability
    results = set()
    for _ in range(10):
        result = convert_to_alternating_random_case("hello")
        results.add(result)
    
    # There should be multiple unique results due to randomness
    assert len(results) > 1

def test_convert_to_alternating_random_case_preserves_non_alphabetic():
    """Ensure non-alphabetic characters are preserved."""
    random.seed(42)
    result = convert_to_alternating_random_case("hello123!")
    assert len(result) == 9
    assert result.replace('!', '').replace('1', '').replace('2', '').replace('3', '').lower() == "hello"