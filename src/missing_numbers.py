def find_missing_numbers(arr):
    """
    Find all missing numbers in a sorted array of positive integers.
    
    Args:
        arr (list): A sorted list of positive integers (ascending or descending).
    
    Returns:
        list: A list of missing numbers in the array.
    
    Raises:
        ValueError: If the input is not a valid sorted list of positive integers.
    """
    # Validate input
    if not arr:
        return []
    
    if not all(isinstance(x, int) and x > 0 for x in arr):
        raise ValueError("Input must be a list of positive integers")
    
    # Determine if the array is ascending or descending
    is_ascending = arr[0] < arr[-1]
    
    # If ascending
    if is_ascending:
        start, end = arr[0], arr[-1]
        return [num for num in range(start + 1, end) if num not in arr]
    
    # If descending
    else:
        start, end = arr[-1], arr[0]
        return [num for num in range(start + 1, end) if num not in arr]