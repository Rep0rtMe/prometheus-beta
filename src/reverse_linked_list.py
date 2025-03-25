class ListNode:
    """
    A class representing a node in a singly linked list.
    
    Attributes:
        val (int): The value stored in the node.
        next (ListNode, optional): Reference to the next node in the list. Defaults to None.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    """
    Reverses a singly linked list and returns the new head.
    
    Args:
        head (ListNode): The head of the input linked list.
    
    Returns:
        ListNode: The head of the reversed linked list.
    
    Time Complexity: O(n), where n is the number of nodes in the list
    Space Complexity: O(1), as we're doing an in-place reversal
    
    Examples:
        1 -> 2 -> 3 becomes 3 -> 2 -> 1
        None becomes None
    """
    # Handle empty list or single node list
    if not head or not head.next:
        return head
    
    # Initialize pointers for reversal
    prev = None
    current = head
    
    # Traverse and reverse links
    while current:
        # Store next node before changing links
        next_node = current.next
        
        # Reverse the link
        current.next = prev
        
        # Move pointers forward
        prev = current
        current = next_node
    
    # Return the new head (previously the last node)
    return prev