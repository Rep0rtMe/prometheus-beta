import pytest
from src.shannon_fano_coding import shannon_fano_encode, shannon_fano_decode

def test_basic_encoding_decoding():
    """Test basic encoding and decoding of a simple string"""
    input_data = "hello world"
    codes, compressed = shannon_fano_encode(input_data)
    
    # Verify codes are generated
    assert len(codes) > 0
    assert all(isinstance(code, str) for code in codes.values())
    
    # Verify compression
    assert isinstance(compressed, str)
    assert len(compressed) > 0
    
    # Verify full round-trip encoding and decoding
    decoded = shannon_fano_decode(codes, compressed)
    assert decoded == input_data

def test_empty_input():
    """Test handling of empty input"""
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        shannon_fano_encode("")

def test_single_character_input():
    """Test encoding and decoding of a single character"""
    input_data = "a"
    codes, compressed = shannon_fano_encode(input_data)
    
    assert codes == {'a': '0'}
    assert compressed == '0'
    
    decoded = shannon_fano_decode(codes, compressed)
    assert decoded == input_data

def test_repeated_characters():
    """Test encoding and decoding with repeated characters"""
    input_data = "aaabbbcccddd"
    codes, compressed = shannon_fano_encode(input_data)
    
    # Verify full round-trip encoding and decoding
    decoded = shannon_fano_decode(codes, compressed)
    assert decoded == input_data

def test_complex_input():
    """Test encoding and decoding with more complex input"""
    input_data = "the quick brown fox jumps over the lazy dog"
    codes, compressed = shannon_fano_encode(input_data)
    
    # Verify full round-trip encoding and decoding
    decoded = shannon_fano_decode(codes, compressed)
    assert decoded == input_data

def test_invalid_decoding():
    """Test handling of invalid compressed string"""
    codes = {'a': '0', 'b': '1'}
    
    with pytest.raises(ValueError, match="Unable to fully decode"):
        # Create an invalid compressed string that cannot be fully decoded
        shannon_fano_decode(codes, "01012")  # Invalid sequence with an unrecognized bit

def test_code_uniqueness():
    """Verify that generated codes are unique"""
    input_data = "abracadabra"
    codes, _ = shannon_fano_encode(input_data)
    
    # Check that all codes are unique
    assert len(set(codes.values())) == len(codes)