def swap_numbers(a, b):
    """
    Return two numbers in swapped order without using a temporary variable.
    
    Args:
        a (int): First number
        b (int): Second number
    
    Returns:
        tuple: A tuple containing the numbers in swapped order (b, a)
    
    Raises:
        TypeError: If inputs are not of type int
    """
    # Validate input types
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Both inputs must be integers")
    
    return b, a