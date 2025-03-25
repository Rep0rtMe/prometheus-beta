def radix_sort(arr):
    """
    Implement the radix sort algorithm for non-negative integers.
    
    Radix sort is a non-comparative sorting algorithm that sorts integers 
    by processing individual digits from least significant to most significant.
    
    Args:
        arr (list): A list of non-negative integers to be sorted.
    
    Returns:
        list: A new sorted list of integers.
    
    Raises:
        TypeError: If input is not a list or contains non-integer elements.
        ValueError: If list contains negative numbers.
    
    Time Complexity: O(d * (n + k)), where d is the number of digits, 
    n is the number of elements, and k is the range of input (10 for decimal)
    Space Complexity: O(n + k)
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check if all elements are non-negative integers
    if not all(isinstance(num, int) and num >= 0 for num in arr):
        raise ValueError("List must contain only non-negative integers")
    
    # Handle empty list or single-element list
    if len(arr) <= 1:
        return arr.copy()
    
    # Find the maximum number to know the number of digits
    max_num = max(arr)
    
    # Do counting sort for every digit
    exp = 1
    while max_num // exp > 0:
        # Perform counting sort based on the current digit
        # Initialize output and count arrays
        output = [0] * len(arr)
        count = [0] * 10
        
        # Store count of occurrences in count[]
        for num in arr:
            index = num // exp
            count[index % 10] += 1
        
        # Change count[i] so that count[i] now contains actual
        # position of this digit in output[]
        for i in range(1, 10):
            count[i] += count[i - 1]
        
        # Build the output array
        i = len(arr) - 1
        while i >= 0:
            index = arr[i] // exp
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1
        
        # Copy the output array to arr[], so that arr[] now
        # contains sorted numbers according to current digit
        arr = output.copy()
        
        # Move to next digit
        exp *= 10
    
    return arr