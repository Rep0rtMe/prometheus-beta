import time
import logging
from functools import wraps

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def log_execution_time(logger=logger):
    """
    A decorator that logs the execution time of a function.
    
    Args:
        logger (logging.Logger, optional): Logger to use for reporting. 
                                           Defaults to the module-level logger.
    
    Returns:
        callable: Decorated function that logs its execution time.
    
    Examples:
        >>> @log_execution_time()
        ... def example_function(x, y):
        ...     time.sleep(1)
        ...     return x + y
        >>> result = example_function(1, 2)
        # This will log the execution time of the function
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Record start time
            start_time = time.time()
            
            try:
                # Execute the original function
                result = func(*args, **kwargs)
                
                # Calculate and log execution time
                end_time = time.time()
                execution_time = end_time - start_time
                
                logger.info(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds")
                
                return result
            
            except Exception as e:
                # Log any exceptions that occur during function execution
                logger.error(f"Error in function '{func.__name__}': {str(e)}")
                raise
        
        return wrapper
    
    return decorator