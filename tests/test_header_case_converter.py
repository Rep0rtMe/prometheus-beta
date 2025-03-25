import pytest
from src.header_case_converter import convert_to_header_case

def test_convert_to_header_case_basic():
    """Test basic string conversion to header case."""
    assert convert_to_header_case("hello world") == "Hello World"
    assert convert_to_header_case("snake_case_string") == "Snake Case String"
    assert convert_to_header_case("camelCaseString") == "Camel Case String"

def test_convert_to_header_case_already_header():
    """Test strings that are already in header case."""
    assert convert_to_header_case("Already Header Case") == "Already Header Case"

def test_convert_to_header_case_mixed_separators():
    """Test strings with mixed separators."""
    assert convert_to_header_case("mixed_camelCase-string") == "Mixed Camel Case String"

def test_convert_to_header_case_empty_string():
    """Test empty string conversion."""
    assert convert_to_header_case("") == ""

def test_convert_to_header_case_single_word():
    """Test single word conversion."""
    assert convert_to_header_case("hello") == "Hello"
    assert convert_to_header_case("HELLO") == "Hello"

def test_convert_to_header_case_invalid_input():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        convert_to_header_case(123)
    with pytest.raises(TypeError):
        convert_to_header_case(None)
    with pytest.raises(TypeError):
        convert_to_header_case(["list"])