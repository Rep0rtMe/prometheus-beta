import pytest
from src.longest_substring import find_longest_substring

def test_find_longest_substring_basic():
    """Test basic functionality of the longest substring finder"""
    assert find_longest_substring("abcabcbb") == "abc"
    assert find_longest_substring("bbbbb") == "b"
    assert find_longest_substring("pwwkew") == "wke"

def test_find_longest_substring_edge_cases():
    """Test edge cases"""
    assert find_longest_substring("") == ""
    assert find_longest_substring("a") == "a"
    assert find_longest_substring("aab") == "ab"

def test_find_longest_substring_case_sensitivity():
    """Test case-sensitive behavior"""
    assert find_longest_substring("AbcA") == "Abc"
    assert find_longest_substring("aA") == "aA"

def test_find_longest_substring_mixed_chars():
    """Test with mixed characters"""
    assert find_longest_substring("hello world") == "helo wrd"
    assert find_longest_substring("!@#$%^&*()") == "!@#$%^&*()"

def test_find_longest_substring_unicode():
    """Test with Unicode characters"""
    assert find_longest_substring("áéíóú") == "áéíóú"
    assert find_longest_substring("aaáábbbccc") == "áb"