import pytest
from src.parentheses_balance import is_balanced_parentheses

def test_basic_balanced_cases():
    """Test basic balanced parentheses scenarios."""
    assert is_balanced_parentheses("()") == True
    assert is_balanced_parentheses("(())") == True
    assert is_balanced_parentheses("((()))") == True

def test_unbalanced_cases():
    """Test unbalanced parentheses scenarios."""
    assert is_balanced_parentheses("(") == False
    assert is_balanced_parentheses(")") == False
    assert is_balanced_parentheses("((") == False
    assert is_balanced_parentheses("))") == False
    assert is_balanced_parentheses(")(") == False

def test_complex_balanced_cases():
    """Test more complex balanced parentheses scenarios."""
    assert is_balanced_parentheses("()()") == True
    assert is_balanced_parentheses("(()())") == True
    assert is_balanced_parentheses("((()()))") == True

def test_empty_string():
    """Test empty string case."""
    assert is_balanced_parentheses("") == True

def test_only_parentheses():
    """Ensure function only works with parentheses."""
    with pytest.raises(TypeError):
        is_balanced_parentheses(123)
    with pytest.raises(TypeError):
        is_balanced_parentheses(None)
    with pytest.raises(TypeError):
        is_balanced_parentheses(["(", ")"])

def test_mixed_characters():
    """Test function with non-parentheses characters."""
    with pytest.raises(ValueError):
        is_balanced_parentheses("(a)")
        is_balanced_parentheses("test(")
        is_balanced_parentheses(")test(")