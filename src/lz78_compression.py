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
    dictionary = {
        "": 0  # Empty string has index 0
    }
    compressed = []
    current_sequence = ""
    next_index = 1
    
    # Compress the input text
    for char in input_text:
        # Try to extend current sequence
        extended_sequence = current_sequence + char
        
        if extended_sequence in dictionary:
            # If sequence exists, continue building
            current_sequence = extended_sequence
        else:
            # Add new sequence to dictionary and output compression tuple
            compressed.append((dictionary.get(current_sequence, 0), char))
            dictionary[extended_sequence] = next_index
            next_index += 1
            
            # Reset current sequence
            current_sequence = ""
    
    # Handle any remaining sequence
    if current_sequence:
        compressed.append((dictionary.get(current_sequence, 0), ""))
    
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
    decompressed = []
    next_index = 1
    
    # Decompress the data
    for index, char in compressed_data:
        # Retrieve the sequence from dictionary
        prefix = dictionary.get(index, "")
        
        # Build the current sequence
        current_sequence = prefix + char
        decompressed.append(current_sequence)
        
        # Add the new sequence to dictionary
        if index != 0:
            dictionary[next_index] = current_sequence
            next_index += 1
    
    return "".join(decompressed)