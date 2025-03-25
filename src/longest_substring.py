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
    
    # Sliding window approach
    longest_substring = ""
    current_substring = ""
    
    for char in s:
        # If character is already in current substring, 
        # slice from the repeated character's next position
        if char in current_substring:
            # Find the index of the first occurrence of the repeated character
            index = current_substring.index(char)
            current_substring = current_substring[index + 1:] + char
        else:
            current_substring += char
        
        # Update longest substring if current is longer
        if len(current_substring) > len(longest_substring):
            longest_substring = current_substring
    
    return longest_substring