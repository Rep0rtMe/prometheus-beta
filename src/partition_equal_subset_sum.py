def can_partition(nums):
    """
    Determine if a list of integers can be partitioned into two subsets with equal sum.
    
    Args:
        nums (list): A list of positive integers
    
    Returns:
        bool: True if the list can be partitioned into two subsets with equal sum, False otherwise
    
    Time Complexity: O(n * sum(nums))
    Space Complexity: O(sum(nums))
    
    Examples:
        >>> can_partition([1, 5, 11, 5])
        True
        >>> can_partition([1, 2, 3, 5])
        False
    
    Raises:
        TypeError: If input is not a list or contains non-positive numbers
    """
    # Validate input type
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    
    # Check for empty list
    if not nums:
        return False
    
    # Validate all elements are positive integers
    if any(not isinstance(x, int) or x <= 0 for x in nums):
        raise TypeError("All elements must be positive integers")
    
    # Calculate total sum of the array
    total_sum = sum(nums)
    
    # If total sum is odd, we can't divide into two equal subsets
    if total_sum % 2 != 0:
        return False
    
    # Target is half of the total sum
    target = total_sum // 2
    
    # Create a dynamic programming set to track possible subset sums
    possible_sums = set([0])
    
    # Iterate through each number
    for num in nums:
        # Create a copy of current possible sums to avoid modifying during iteration
        current_sums = possible_sums.copy()
        
        # For each existing sum, try adding the current number
        for existing_sum in current_sums:
            new_sum = existing_sum + num
            
            # If we find a sum exactly matching the target, we found a valid partition
            if new_sum == target:
                return True
            
            # If the new sum is less than target, add it to possible sums
            if new_sum < target:
                possible_sums.add(new_sum)
    
    return False