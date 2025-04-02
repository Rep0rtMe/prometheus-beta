def filter_primes(numbers):
    """
    Filter a list of numbers to return only prime numbers.
    
    Prime numbers are defined as positive integers greater than 1 that have 
    no positive integer divisors other than 1 and themselves. 
    Negative numbers are not considered prime.
    
    Args:
        numbers (list): A list of integers to filter
    
    Returns:
        list: A list of prime numbers from the input list
    
    Examples:
        >>> filter_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        [2, 3, 5, 7]
        >>> filter_primes([-1, -2, -3, 0, 1, 2, 3, 4, 5])
        [2, 3, 5]
    """
    def is_prime(n):
        # Exclude negative numbers, 0, and 1
        if n <= 1:
            return False
        
        # Check for divisibility up to the square root of n
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        
        return True
    
    return [num for num in numbers if is_prime(num)]