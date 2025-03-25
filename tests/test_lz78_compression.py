"""
Unit tests for LZ78 compression algorithm implementation.
"""

import pytest
from src.lz78_compression import lz78_compress, lz78_decompress


def test_lz78_compress_basic():
    """Test basic compression scenario"""
    text = "TOBEORNOTTOBEORTOBEORNOT"
    compressed = lz78_compress(text)
    decompressed = lz78_decompress(compressed)
    assert decompressed == text


def test_lz78_compress_empty_string():
    """Test compression of an empty string"""
    with pytest.raises(ValueError):
        lz78_compress("")


def test_lz78_compress_invalid_type():
    """Test compression with invalid input type"""
    with pytest.raises(TypeError):
        lz78_compress(123)  # Non-string input


def test_lz78_decompress_basic():
    """Test basic decompression scenario"""
    text = "TOBEORNOTTOBEORTOBEORNOT"
    compressed = lz78_compress(text)
    decompressed = lz78_decompress(compressed)
    assert decompressed == text


def test_lz78_decompress_empty_list():
    """Test decompression of an empty list"""
    assert lz78_decompress([]) == ""


def test_lz78_decompress_invalid_type():
    """Test decompression with invalid input type"""
    with pytest.raises(TypeError):
        lz78_decompress("not a list")


def test_lz78_decompress_invalid_tuple_format():
    """Test decompression with invalid tuple format"""
    with pytest.raises(ValueError):
        lz78_decompress([(1, 2, 3)])  # Invalid tuple


def test_lz78_compress_repeating_pattern():
    """Test compression of a string with repeating patterns"""
    text = "ABABABABAB"
    compressed = lz78_compress(text)
    decompressed = lz78_decompress(compressed)
    assert decompressed == text


def test_lz78_compress_single_character():
    """Test compression of a single character"""
    text = "A"
    compressed = lz78_compress(text)
    decompressed = lz78_decompress(compressed)
    assert decompressed == text


def test_lz78_compression_roundtrip():
    """Test multiple roundtrip compression and decompression scenarios"""
    test_cases = [
        "HELLO WORLD",
        "abcabcabcabc",
        "Mississippi",
        "🌍🌎🌏🌍🌎🌏"  # Unicode characters
    ]
    
    for text in test_cases:
        compressed = lz78_compress(text)
        decompressed = lz78_decompress(compressed)
        assert decompressed == text, f"Failed for text: {text}"