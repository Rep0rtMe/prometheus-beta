import pytest
from datetime import timedelta
from src.timestamp_difference import calculate_timestamp_difference

def test_calculate_timestamp_difference_basic():
    """Test basic timestamp difference calculation."""
    diff = calculate_timestamp_difference(
        '2023-01-01 10:00:00', 
        '2023-01-01 11:00:00'
    )
    assert diff == timedelta(hours=1)

def test_calculate_timestamp_difference_different_dates():
    """Test timestamp difference across different dates."""
    diff = calculate_timestamp_difference(
        '2023-01-01 00:00:00', 
        '2023-01-02 00:00:00'
    )
    assert diff == timedelta(days=1)

def test_calculate_timestamp_difference_order_independence():
    """Test that order of timestamps doesn't matter."""
    diff1 = calculate_timestamp_difference(
        '2023-01-01 10:00:00', 
        '2023-01-01 11:00:00'
    )
    diff2 = calculate_timestamp_difference(
        '2023-01-01 11:00:00', 
        '2023-01-01 10:00:00'
    )
    assert diff1 == diff2

def test_calculate_timestamp_difference_custom_format():
    """Test timestamp difference with a custom format."""
    diff = calculate_timestamp_difference(
        '01/01/2023 10:00:00', 
        '01/01/2023 11:00:00', 
        format='%m/%d/%Y %H:%M:%S'
    )
    assert diff == timedelta(hours=1)

def test_calculate_timestamp_difference_invalid_format():
    """Test error handling for invalid timestamp format."""
    with pytest.raises(ValueError, match="Error parsing timestamps"):
        calculate_timestamp_difference(
            'invalid-timestamp', 
            '2023-01-01 11:00:00'
        )

def test_calculate_timestamp_difference_microseconds():
    """Test timestamp difference with microsecond precision."""
    diff = calculate_timestamp_difference(
        '2023-01-01 10:00:00.123456', 
        '2023-01-01 10:00:00.987654', 
        format='%Y-%m-%d %H:%M:%S.%f'
    )
    assert diff == timedelta(microseconds=864198)