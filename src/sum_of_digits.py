def sum_of_digits(number: int) -> int:
    """
    Calculate the sum of digits for a positive integer.

    Args:
        number (int): A positive integer to sum the digits of.

    Returns:
        int: The sum of all digits in the input number.

    Raises:
        ValueError: If the input is not a positive integer.
    """
    # Validate input is a positive integer
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")
    
    if number < 0:
        raise ValueError("Input must be a positive integer")
    
    # Special case for 0
    if number == 0:
        return 0
    
    # Sum the digits
    digit_sum = 0
    while number > 0:
        digit_sum += number % 10  # Get the last digit
        number //= 10  # Remove the last digit
    
    return digit_sum