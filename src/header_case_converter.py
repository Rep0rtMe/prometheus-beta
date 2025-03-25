def convert_to_header_case(input_string):
    """
    Convert a given string to header case.
    
    Header case is a style where the first letter of each word is capitalized,
    and words are separated by spaces.
    
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
    
    # Replace common separators with space
    separators = ['-', '_']
    for sep in separators:
        input_string = input_string.replace(sep, ' ')
    
    # Handle camelCase or mixedCase
    words = []
    current_word = input_string[0].upper()
    for char in input_string[1:]:
        if char.isupper():
            # If uppercase, start a new word
            words.append(current_word)
            current_word = char
        else:
            current_word += char
    words.append(current_word)
    
    # Capitalize each word and join
    return ' '.join(word.capitalize() for word in words)