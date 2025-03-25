import pytest
from src.reverse_linked_list import ListNode, reverse_linked_list

def create_linked_list(values):
    """
    Helper function to create a linked list from a list of values.
    
    Args:
        values (list): List of values to create the linked list from.
    
    Returns:
        ListNode: Head of the created linked list.
    """
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

def linked_list_to_list(head):
    """
    Convert a linked list to a regular list for easy comparison.
    
    Args:
        head (ListNode): Head of the linked list.
    
    Returns:
        list: Values of the linked list in order.
    """
    result = []
    current = head
    
    while current:
        result.append(current.val)
        current = current.next
    
    return result

def test_reverse_empty_list():
    """Test reversing an empty list."""
    assert reverse_linked_list(None) is None

def test_reverse_single_node():
    """Test reversing a list with a single node."""
    head = ListNode(1)
    reversed_head = reverse_linked_list(head)
    assert linked_list_to_list(reversed_head) == [1]

def test_reverse_multiple_nodes():
    """Test reversing a list with multiple nodes."""
    head = create_linked_list([1, 2, 3, 4, 5])
    reversed_head = reverse_linked_list(head)
    assert linked_list_to_list(reversed_head) == [5, 4, 3, 2, 1]

def test_reverse_two_nodes():
    """Test reversing a list with two nodes."""
    head = create_linked_list([1, 2])
    reversed_head = reverse_linked_list(head)
    assert linked_list_to_list(reversed_head) == [2, 1]

def test_reverse_preserves_length():
    """Ensure the length of the list remains the same after reversal."""
    original_values = [1, 2, 3, 4, 5]
    head = create_linked_list(original_values)
    reversed_head = reverse_linked_list(head)
    reversed_values = linked_list_to_list(reversed_head)
    
    assert len(original_values) == len(reversed_values)
    assert set(original_values) == set(reversed_values)