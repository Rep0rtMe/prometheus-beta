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
            
            # Check both concatenation orders
            concat1 = words[i] + words[j]
            concat2 = words[j] + words[i]
            
            # If either concatenation forms a palindrome, add the pair
            if is_palindrome(concat1):
                result.append([i, j])
            
            if is_palindrome(concat2):
                result.append([j, i])

    # Remove duplicates while preserving order
    unique_result = []
    seen = set()
    for pair in result:
        if tuple(pair) not in seen:
            unique_result.append(pair)
            seen.add(tuple(pair))

    return unique_result