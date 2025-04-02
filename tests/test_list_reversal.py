import pytest
from src.list_reversal import reverse_list_with_stack, Stack

def test_stack_basics():
    """Test basic Stack operations."""
    stack = Stack()
    assert stack.is_empty() == True
    
    stack.push(1)
    assert stack.is_empty() == False
    
    top_item = stack.pop()
    assert top_item == 1
    assert stack.is_empty() == True

def test_reverse_list_with_stack():
    """Test list reversal with various scenarios."""
    # Test basic reversal
    test_list = [1, 2, 3, 4, 5]
    result = reverse_list_with_stack(test_list)
    assert result == [5, 4, 3, 2, 1]
    
    # Test single element list
    single_list = [42]
    result = reverse_list_with_stack(single_list)
    assert result == [42]
    
    # Test empty list
    empty_list = []
    result = reverse_list_with_stack(empty_list)
    assert result == []
    
    # Test list with mixed positive and negative integers
    mixed_list = [-1, 0, 1, -5, 10]
    result = reverse_list_with_stack(mixed_list)
    assert result == [10, -5, 1, 0, -1]

def test_type_checking():
    """Test input type validation."""
    # Test non-list input raises TypeError
    with pytest.raises(TypeError):
        reverse_list_with_stack("not a list")
    
    with pytest.raises(TypeError):
        reverse_list_with_stack(123)
    
    with pytest.raises(TypeError):
        reverse_list_with_stack(None)

def test_stack_empty_pop():
    """Test popping from an empty stack raises an IndexError."""
    stack = Stack()
    with pytest.raises(IndexError):
        stack.pop()