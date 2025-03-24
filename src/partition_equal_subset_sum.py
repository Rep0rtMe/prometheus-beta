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
    
    # Create a set of possible subset sums
    subset_sums = {0}
    
    # Compute all possible subset sums
    for num in nums:
        # Create a new set to store sums to avoid modifying while iterating
        new_subset_sums = subset_sums.copy()
        
        # Add current number to existing subset sums
        for subset_sum in subset_sums:
            new_sum = subset_sum + num
            
            # If we hit the target sum, return True
            if new_sum == target:
                return True
            
            # Only add if new sum is less than target
            if new_sum < target:
                new_subset_sums.add(new_sum)
        
        subset_sums = new_subset_sums
    
    return False