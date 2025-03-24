def swap_numbers(a, b):
    """
    Swap two numbers without using a temporary variable.
    
    Uses bitwise XOR operation to swap values efficiently.
    
    Args:
        a (int): First number to be swapped
        b (int): Second number to be swapped
    
    Returns:
        tuple: A tuple containing the swapped numbers (b, a)
    
    Raises:
        TypeError: If inputs are not of type int
    """
    # Validate input types
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Both inputs must be integers")
    
    # Swap numbers using bitwise XOR operation
    a = a ^ b
    b = a ^ b
    a = a ^ b
    
    return b, a