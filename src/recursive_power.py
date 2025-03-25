def recursive_power(base: float, exponent: int) -> float:
    """
    Calculate the power of a number using recursion.
    
    Args:
        base (float): The base number to be raised to a power.
        exponent (int): The exponent (power) to raise the base to.
    
    Returns:
        float: The result of base raised to the exponent.
    
    Raises:
        TypeError: If base is not a number or exponent is not an integer.
        ValueError: If exponent is negative and base is zero.
    
    Examples:
        >>> recursive_power(2, 3)
        8.0
        >>> recursive_power(5, 0)
        1.0
        >>> recursive_power(10, -2)
        0.01
    """
    # Type checking
    if not isinstance(base, (int, float)):
        raise TypeError("Base must be a number")
    if not isinstance(exponent, int):
        raise TypeError("Exponent must be an integer")
    
    # Handle special cases
    if exponent == 0:
        return 1.0
    
    # Handle negative exponents
    if exponent < 0:
        if base == 0:
            raise ValueError("Cannot raise 0 to a negative power")
        return 1.0 / recursive_power(base, -exponent)
    
    # Recursive case
    if exponent == 1:
        return float(base)
    
    # Recursive power calculation
    return base * recursive_power(base, exponent - 1)