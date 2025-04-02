import pytest
from src.palindrome_checker import is_palindrome

def test_classic_palindromes():
    """Test well-known palindrome phrases."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False

def test_simple_palindromes():
    """Test simple palindrome strings."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("RaceCar") == True

def test_edge_cases():
    """Test edge cases like empty string and single character."""
    assert is_palindrome("") == True  # Empty string is considered a palindrome
    assert is_palindrome("a") == True
    assert is_palindrome(" ") == True  # Only whitespace

def test_non_palindromes():
    """Test strings that are not palindromes."""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_mixed_case_and_punctuation():
    """Test palindromes with mixed case and punctuation."""
    assert is_palindrome("Madam, I'm Adam.") == True
    assert is_palindrome("Was it a car or a cat I saw?") == True
    assert is_palindrome("No 'x' in Nixon") == True

def test_numeric_palindromes():
    """Test palindromes with numbers."""
    assert is_palindrome("12321") == True
    assert is_palindrome("A1b22b1a") == True
    assert is_palindrome("123 456") == False