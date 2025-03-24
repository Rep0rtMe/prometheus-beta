import time
import logging
import pytest
from src.execution_timer import log_execution_time

# Create a custom logger for testing
class MockLogger:
    def __init__(self):
        self.logs = []
    
    def info(self, message):
        self.logs.append(('info', message))
    
    def error(self, message):
        self.logs.append(('error', message))

def test_log_execution_time_basic():
    """Test basic logging of function execution time"""
    mock_logger = MockLogger()
    
    @log_execution_time(logger=mock_logger)
    def simple_function():
        time.sleep(0.1)  # Simulate some work
    
    simple_function()
    
    # Check that info log was created
    assert len(mock_logger.logs) == 1
    log_type, log_message = mock_logger.logs[0]
    assert log_type == 'info'
    assert 'simple_function' in log_message
    assert 'executed in' in log_message

def test_log_execution_time_with_arguments():
    """Test logging with functions that have arguments"""
    mock_logger = MockLogger()
    
    @log_execution_time(logger=mock_logger)
    def add_numbers(a, b):
        time.sleep(0.05)  # Simulate some work
        return a + b
    
    result = add_numbers(3, 4)
    
    # Check return value
    assert result == 7
    
    # Check that info log was created
    assert len(mock_logger.logs) == 1
    log_type, log_message = mock_logger.logs[0]
    assert log_type == 'info'
    assert 'add_numbers' in log_message

def test_log_execution_time_exception():
    """Test error logging when an exception occurs"""
    mock_logger = MockLogger()
    
    @log_execution_time(logger=mock_logger)
    def raise_exception():
        raise ValueError("Test exception")
    
    # Expect the original exception to be raised
    with pytest.raises(ValueError, match="Test exception"):
        raise_exception()
    
    # Check that error log was created
    assert len(mock_logger.logs) == 1
    log_type, log_message = mock_logger.logs[0]
    assert log_type == 'error'
    assert 'raise_exception' in log_message

def test_log_execution_time_preserves_metadata():
    """Test that decorator preserves function metadata"""
    @log_execution_time()
    def example_function(x, y):
        """Docstring for example function"""
        return x + y
    
    # Check function name preservation
    assert example_function.__name__ == 'example_function'
    
    # Check docstring preservation
    assert example_function.__doc__ == 'Docstring for example function'

def test_log_execution_time_measures_time_accurately():
    """Test that execution time measurement is reasonably accurate"""
    mock_logger = MockLogger()
    
    @log_execution_time(logger=mock_logger)
    def sleep_function():
        time.sleep(0.2)  # Sleep for 0.2 seconds
    
    sleep_function()
    
    # Check log was created
    assert len(mock_logger.logs) == 1
    log_type, log_message = mock_logger.logs[0]
    assert log_type == 'info'
    
    # Extract execution time from log message
    import re
    match = re.search(r'executed in (\d+\.\d+)', log_message)
    assert match is not None
    execution_time = float(match.group(1))
    
    # Check execution time is close to expected (within 0.05 seconds)
    assert 0.15 < execution_time < 0.25