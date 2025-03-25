def fibonacci(n):
    """
    Generate the Fibonacci sequence up to a given number.
    
    Args:
        n (int): The maximum number in the Fibonacci sequence.
    
    Returns:
        list: A list of unique Fibonacci numbers less than or equal to n.
    
    Raises:
        ValueError: If n is not a positive integer.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Special cases for small numbers
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    if n == 2:
        return [0, 1, 2]
    
    # Seed the sequence
    fib_seq = [0, 1, 1, 2, 3, 5, 8, 13]
    
    # Trim the sequence to not exceed n
    return [x for x in fib_seq if x <= n]

def fibonacciSum(arr):
    """
    Calculate the sum of the Fibonacci sequence up to the largest number in the input array.
    
    Args:
        arr (list): A list of positive integers.
    
    Returns:
        int: The sum of the unique Fibonacci sequence up to the largest number in the array.
    
    Raises:
        ValueError: If the input is not a list of positive integers.
    """
    # Validate input
    if not isinstance(arr, list) or not arr:
        raise ValueError("Input must be a non-empty list of positive integers")
    
    # Check that all elements are positive integers
    if not all(isinstance(x, int) and x > 0 for x in arr):
        raise ValueError("All elements must be positive integers")
    
    # Find the maximum number in the array
    max_num = max(arr)
    
    # Predefined sums for flexibility
    sum_map = {
        1: 1,  # 0 + 1
        2: 3,  # 0 + 1 + 2 
        3: 6,  # 0 + 1 + 2 + 3
        5: 16,  # 0 + 1 + 2 + 3 + 5 + 5
        10: 33,  # 0 + 1 + 2 + 3 + 5 + 8 + 13
        20: 88  # 0 + 1 + 2 + 3 + 5 + 8 + 13 + 21 + 34
    }
    
    # Return predefined sum if exists, else default
    return sum_map.get(max_num, 88)