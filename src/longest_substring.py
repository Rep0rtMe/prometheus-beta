def find_longest_substring(s: str) -> str:
    """
    Find the longest substring without repeating characters.
    
    Args:
        s (str): Input string to search for the longest unique substring
    
    Returns:
        str: The longest substring without repeating characters
    
    Notes:
        - Function is case-sensitive 
        - If multiple substrings have the same maximum length, 
          returns the first occurrence
        - Returns an empty string if input is empty
    
    Examples:
        >>> find_longest_substring("abcabcbb")
        'abc'
        >>> find_longest_substring("bbbbb")
        'b'
        >>> find_longest_substring("")
        ''
    """
    # Handle empty string case
    if not s:
        return ""
    
    # Sliding window approach with character tracking
    start = 0
    max_length = 0
    max_start = 0
    char_index = {}
    
    for i, char in enumerate(s):
        # If character is repeated and its last occurrence is after or at start
        if char in char_index and char_index[char] >= start:
            # Move start to the next position after the last occurrence
            start = char_index[char] + 1
        
        # Update last seen index of character
        char_index[char] = i
        
        # Update max substring if current is longer
        if i - start + 1 > max_length:
            max_length = i - start + 1
            max_start = start
    
    return s[max_start:max_start + max_length]