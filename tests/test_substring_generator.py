import pytest
from src.substring_generator import generate_all_substrings

def test_generate_all_substrings_basic():
    """Test generation of substrings for a simple string."""
    result = generate_all_substrings('abc')
    assert sorted(result) == sorted(['', 'a', 'b', 'c', 'ab', 'bc', 'abc'])
    assert len(result) == 7

def test_generate_all_substrings_empty_string():
    """Test generation of substrings for an empty string."""
    result = generate_all_substrings('')
    assert result == ['']
    assert len(result) == 1

def test_generate_all_substrings_single_char():
    """Test generation of substrings for a single character."""
    result = generate_all_substrings('x')
    assert sorted(result) == sorted(['', 'x'])
    assert len(result) == 2

def test_generate_all_substrings_with_repeated_chars():
    """Test generation of substrings with repeated characters."""
    result = generate_all_substrings('aba')
    assert sorted(result) == sorted(['', 'a', 'b', 'a', 'ab', 'ba', 'aba'])
    assert len(result) == 7

def test_generate_all_substrings_error_handling():
    """Test error handling for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        generate_all_substrings(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        generate_all_substrings(None)

def test_generate_all_substrings_length_preservation():
    """Verify that the generated substrings match the original string length."""
    test_string = 'python'
    result = generate_all_substrings(test_string)
    
    # Check that substrings are indeed from the original string
    for substring in result:
        if substring:  # Skip empty string
            assert all(char in test_string for char in substring)
            assert len(substring) <= len(test_string)