def convert_to_header_case(input_string):
    """
    Convert a given string to header case.
    
    Header case is a style where the first letter of each word is capitalized,
    and words are separated by a single space.
    
    Args:
        input_string (str): The input string to convert.
    
    Returns:
        str: The string converted to header case.
    
    Raises:
        TypeError: If the input is not a string.
    
    Examples:
        >>> convert_to_header_case("hello world")
        'Hello World'
        >>> convert_to_header_case("snake_case_string")
        'Snake Case String'
        >>> convert_to_header_case("camelCaseString")
        'Camel Case String'
        >>> convert_to_header_case("already Header Case")
        'Already Header Case'
    """
    # Validate input
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string")
    
    # If input is empty, return empty string
    if not input_string:
        return ""
    
    # Split the string into words considering multiple separators and camelCase
    words = []
    current_word = ""
    for i, char in enumerate(input_string):
        # Detect word boundaries
        if char.isupper() and current_word and not input_string[i-1].isupper():
            words.append(current_word)
            current_word = char
        elif char in ['-', '_', ' '] and current_word:
            words.append(current_word)
            current_word = ""
        elif not char.isspace():
            current_word += char
    
    # Append the last word
    if current_word:
        words.append(current_word)
    
    # Capitalize each word and remove any empty strings
    capitalized_words = [word.capitalize() for word in words if word]
    
    # Join the words
    return ' '.join(capitalized_words)