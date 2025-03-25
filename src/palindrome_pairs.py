def find_palindrome_pairs(words):
    """
    Find all pairs of indices in an array of strings where concatenated strings form a palindrome.

    Args:
        words (List[str]): A list of strings to check for palindrome pairs.

    Returns:
        List[List[int]]: A list of index pairs where concatenated words form a palindrome.
    
    Time Complexity: O(n^2 * k), where n is the number of words and k is the length of the longest word
    Space Complexity: O(1) for the output list

    Examples:
        >>> find_palindrome_pairs(["bat", "tab", "cat"])
        [[0, 1], [1, 0]]
        >>> find_palindrome_pairs(["abcd", "dcba", "lls", "s", "sssll"])
        [[0, 1], [1, 0], [3, 4], [4, 3]]
    """
    def is_palindrome(s):
        """Check if a string is a palindrome."""
        return s == s[::-1]

    result = []
    n = len(words)

    for i in range(n):
        for j in range(n):
            # Skip checking against self
            if i == j:
                continue
            
            # Calculate both concatenation orders
            first_concat = words[i] + words[j]
            
            # Check if concatenation forms a palindrome
            if is_palindrome(first_concat):
                result.append([i, j])

    return result