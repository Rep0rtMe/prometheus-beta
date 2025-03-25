def generate_fibonacci_subsequence(n):
    """
    Generate a Fibonacci subsequence where the sum of even-indexed numbers equals n.
    
    Args:
        n (int): The target sum of even-indexed numbers
    
    Returns:
        list: A Fibonacci subsequence satisfying the constraint
    
    Raises:
        ValueError: If n is negative or cannot be generated
    """
    # Handle special cases
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    
    # Special case for n = 0
    if n == 0:
        return [0]
    
    # Initialize variables for generating subsequence
    subsequence = [0, 1]  # Start with first two Fibonacci numbers
    
    while True:
        # Calculate sum of even-indexed numbers
        even_indexed_sum = subsequence[0] + subsequence[2] if len(subsequence) >= 3 else subsequence[0]
        
        # Check if we've reached the target
        if even_indexed_sum == n:
            return subsequence
        
        # If sum exceeds target, it's impossible to generate
        if even_indexed_sum > n:
            raise ValueError(f"Cannot generate a subsequence with even-indexed sum of {n}")
        
        # Generate next Fibonacci number
        next_num = subsequence[-1] + subsequence[-2]
        subsequence.append(next_num)