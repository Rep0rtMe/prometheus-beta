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
    
    # Create a dynamic programming table
    # dp[j] represents whether a subset of sum j can be created
    dp = [False] * (target + 1)
    dp[0] = True
    
    # Compute possible subset sums
    for num in nums:
        # Iterate backwards to avoid using the same element multiple times
        for j in range(target, num - 1, -1):
            dp[j] |= dp[j - num]
    
    return dp[target]