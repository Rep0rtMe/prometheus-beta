import pytest
from src.most_frequent_character import find_most_frequent_character

def test_basic_string():
    """Test basic string with clear most frequent character"""
    assert find_most_frequent_character("hello") == 'l'

def test_multiple_same_frequency():
    """Test string where multiple characters have same frequency"""
    assert find_most_frequent_character("aabbcc") in ['a', 'b', 'c']

def test_empty_string():
    """Test empty string returns None"""
    assert find_most_frequent_character("") is None

def test_single_character():
    """Test string with single character"""
    assert find_most_frequent_character("a") == 'a'

def test_all_unique_characters():
    """Test string where all characters appear once"""
    result = find_most_frequent_character("abcde")
    assert result in list("abcde")

def test_string_with_punctuation():
    """Test string with punctuation and repeated first character"""
    assert find_most_frequent_character("hello, world!") == 'l'

def test_invalid_input_type():
    """Test that TypeError is raised for non-string input"""
    with pytest.raises(TypeError):
        find_most_frequent_character(123)
    with pytest.raises(TypeError):
        find_most_frequent_character(None)
    with pytest.raises(TypeError):
        find_most_frequent_character(["hello"])