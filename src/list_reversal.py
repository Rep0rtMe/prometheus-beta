class Stack:
    """
    A simple Stack data structure implementation using a list.
    
    This Stack supports basic operations like push, pop, and is used for list reversal.
    """
    def __init__(self):
        """Initialize an empty stack."""
        self._items = []
    
    def push(self, item):
        """
        Add an item to the top of the stack.
        
        Args:
            item: The item to be added to the stack.
        """
        self._items.append(item)
    
    def pop(self):
        """
        Remove and return the top item from the stack.
        
        Returns:
            The top item of the stack.
        
        Raises:
            IndexError: If the stack is empty.
        """
        if not self._items:
            raise IndexError("Cannot pop from an empty stack")
        return self._items.pop()
    
    def is_empty(self):
        """
        Check if the stack is empty.
        
        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self._items) == 0

def reverse_list_with_stack(input_list):
    """
    Reverse a list of integers using a Stack data structure.
    
    This function handles lists of any length efficiently, using O(n) time and space complexity.
    
    Args:
        input_list (list): A list of integers to be reversed.
    
    Returns:
        list: A new list with elements in reversed order.
    
    Raises:
        TypeError: If the input is not a list.
    """
    # Check for valid input
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list")
    
    # Handle empty list case
    if not input_list:
        return []
    
    # Create a stack and push all elements
    stack = Stack()
    for item in input_list:
        stack.push(item)
    
    # Pop elements to create reversed list
    reversed_list = []
    while not stack.is_empty():
        reversed_list.append(stack.pop())
    
    return reversed_list