import pytest
from src.palindrome_pairs import find_palindrome_pairs

def test_simple_palindrome_pairs():
    """Test basic palindrome pair scenarios."""
    assert sorted(find_palindrome_pairs(["bat", "tab", "cat"])) == [[0, 1], [1, 0]]

def test_complex_palindrome_pairs():
    """Test more complex palindrome pair scenarios."""
    result = find_palindrome_pairs(["abcd", "dcba", "lls", "s", "sssll"])
    expected = sorted([[0, 1], [1, 0], [2, 4], [3, 4], [4, 3]])
    assert sorted(result) == expected

def test_empty_input():
    """Test with an empty input list."""
    assert find_palindrome_pairs([]) == []

def test_single_word():
    """Test with a single word input."""
    assert find_palindrome_pairs(["hello"]) == []

def test_no_palindrome_pairs():
    """Test when no palindrome pairs exist."""
    assert find_palindrome_pairs(["dog", "cat", "bird"]) == []

def test_multiple_identical_words():
    """Test input with multiple identical words."""
    assert sorted(find_palindrome_pairs(["a", "a", "b"])) == [[0, 1], [1, 0]]