"""
LZ78 Compression Algorithm Implementation

This module provides functions for LZ78 compression and decompression.
LZ78 is a dictionary-based compression algorithm that builds a dictionary 
of previously seen sequences during compression.
"""

from typing import List, Tuple, Union


def lz78_compress(input_text: str) -> List[Tuple[int, str]]:
    """
    Compress the input text using the LZ78 compression algorithm.
    
    Args:
        input_text (str): The text to be compressed
    
    Returns:
        List[Tuple[int, str]]: A list of (index, character) tuples representing 
        the compressed data, where index is the dictionary reference and 
        character is the next character.
    
    Raises:
        TypeError: If input is not a string
        ValueError: If input is an empty string
    """
    # Input validation
    if not isinstance(input_text, str):
        raise TypeError("Input must be a string")
    
    if not input_text:
        raise ValueError("Input cannot be an empty string")
    
    # Initialize dictionary and compression result
    dictionary = {}
    compressed = []
    next_index = 1
    
    current_prefix = ""
    for i, char in enumerate(input_text):
        # Try to extend current prefix
        current_prefix_extended = current_prefix + char
        
        if current_prefix_extended in dictionary:
            # If the extended prefix exists, update current prefix
            current_prefix = current_prefix_extended
        else:
            # Find the index of current prefix or 0 if not found
            prefix_index = dictionary.get(current_prefix, 0)
            
            # Add the tuple to compressed data
            compressed.append((prefix_index, char))
            
            # Add the extended prefix to dictionary
            dictionary[current_prefix_extended] = next_index
            next_index += 1
            
            # Reset current prefix
            current_prefix = ""
    
    # Handle any remaining prefix
    if current_prefix:
        prefix_index = dictionary.get(current_prefix, 0)
        compressed.append((prefix_index, ""))
    
    return compressed


def lz78_decompress(compressed_data: List[Tuple[int, str]]) -> str:
    """
    Decompress data compressed using the LZ78 algorithm.
    
    Args:
        compressed_data (List[Tuple[int, str]]): Compressed data 
        in the format of (index, character) tuples
    
    Returns:
        str: The decompressed original text
    
    Raises:
        TypeError: If input is not a list of tuples
        ValueError: If input list contains invalid tuples
    """
    # Input validation
    if not isinstance(compressed_data, list):
        raise TypeError("Input must be a list of tuples")
    
    if not compressed_data:
        return ""
    
    # Validate each tuple
    for item in compressed_data:
        if not (isinstance(item, tuple) and len(item) == 2 and 
                isinstance(item[0], int) and isinstance(item[1], str)):
            raise ValueError("Invalid compressed data format")
    
    # Initialize dictionary and decompression
    dictionary = {0: ""}
    next_index = 1
    decompressed = []
    
    # Decompress the data
    for index, new_char in compressed_data:
        # Retrieve the prefix sequence
        prefix_sequence = dictionary.get(index, "")
        
        # Build the current sequence
        current_sequence = prefix_sequence + new_char
        
        # Add the new sequence to dictionary (if index is not 0)
        dictionary[next_index] = current_sequence
        next_index += 1
        
        # Append to decompressed result
        decompressed.append(current_sequence)
    
    return "".join(decompressed)