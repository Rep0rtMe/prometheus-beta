def library_sort(arr):
    """
    Implement the Library Sort algorithm (also known as Insertion Sort with Binary Search).
    
    Library Sort is an optimized version of Insertion Sort that uses binary search 
    to find the correct insertion point for each element, reducing the number of 
    comparisons needed.
    
    Args:
        arr (list): The input list to be sorted in-place.
    
    Returns:
        list: The sorted list.
    
    Raises:
        TypeError: If the input is not a list or contains non-comparable elements.
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Handle empty or single-element lists
    if len(arr) <= 1:
        return arr
    
    # Perform library sort
    for i in range(1, len(arr)):
        # Use binary search to find the insertion point
        key = arr[i]
        
        # Binary search to find the correct insertion point
        left, right = 0, i
        while left < right:
            mid = (left + right) // 2
            if arr[mid] <= key:
                left = mid + 1
            else:
                right = mid
        
        # Shift elements to make space for insertion
        j = i
        while j > left:
            arr[j] = arr[j-1]
            j -= 1
        
        # Insert the key at the correct position
        arr[left] = key
    
    return arr