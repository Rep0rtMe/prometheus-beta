from collections import Counter
from typing import Dict, List, Tuple

def shannon_fano_encode(data: str) -> Tuple[Dict[str, str], str]:
    """
    Implement Shannon-Fano coding for data compression.
    
    Args:
        data (str): Input string to be compressed
    
    Returns:
        Tuple containing:
        - Dictionary of character to binary code mappings
        - Compressed binary string
    
    Raises:
        ValueError: If input data is empty
    """
    # Check for empty input
    if not data:
        raise ValueError("Input data cannot be empty")
    
    # Count frequency of each character
    freq = Counter(data)
    
    # Sort characters by frequency in descending order
    sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    
    # Recursive function to generate Shannon-Fano codes
    def generate_codes(chars: List[Tuple[str, int]]) -> Dict[str, str]:
        # Base case: single character
        if len(chars) <= 1:
            return {chars[0][0]: '0'} if chars else {}
        
        # Find splitting point to balance frequencies
        total_freq = sum(freq for _, freq in chars)
        current_sum = 0
        split_index = 0
        min_diff = float('inf')
        
        for i in range(len(chars)):
            current_sum += chars[i][1]
            left_sum = current_sum
            right_sum = total_freq - left_sum
            
            # Find the split that most evenly divides the frequencies
            diff = abs(left_sum - right_sum)
            if diff < min_diff:
                min_diff = diff
                split_index = i
        
        # Recursively generate codes for left and right groups
        left_chars = chars[:split_index + 1]
        right_chars = chars[split_index + 1:]
        
        # Assign '0' to left group, '1' to right group
        left_codes = generate_codes(left_chars)
        right_codes = generate_codes(right_chars)
        
        # Prepend '0' to left group codes
        for char in left_codes:
            left_codes[char] = '0' + left_codes[char]
        
        # Prepend '1' to right group codes
        for char in right_codes:
            right_codes[char] = '1' + right_codes[char]
        
        # Merge and return codes
        return {**left_codes, **right_codes}
    
    # Generate codes
    codes = generate_codes(sorted_chars)
    
    # Compress the input data
    compressed = ''.join(codes[char] for char in data)
    
    return codes, compressed

def shannon_fano_decode(codes: Dict[str, str], compressed: str) -> str:
    """
    Decode a Shannon-Fano encoded message.
    
    Args:
        codes (Dict[str, str]): Dictionary of character to binary code mappings
        compressed (str): Compressed binary string
    
    Returns:
        str: Decoded original message
    
    Raises:
        ValueError: If compressed string cannot be fully decoded
    """
    # Invert the codes dictionary for decoding
    reverse_codes = {code: char for char, code in codes.items()}
    
    # Decode the compressed string
    decoded = []
    current_code = ''
    remaining = compressed
    
    while remaining:
        current_code += remaining[0]
        remaining = remaining[1:]
        
        # Check if current code matches a known encoding
        if current_code in reverse_codes:
            decoded.append(reverse_codes[current_code])
            current_code = ''
    
    # Ensure entire string was decoded
    if current_code or remaining:
        raise ValueError("Unable to fully decode the compressed string")
    
    return ''.join(decoded)