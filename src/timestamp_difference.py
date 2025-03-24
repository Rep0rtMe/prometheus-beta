from datetime import datetime, timedelta

def calculate_timestamp_difference(timestamp1: str, timestamp2: str, format: str = '%Y-%m-%d %H:%M:%S') -> timedelta:
    """
    Calculate the time difference between two timestamps.

    Args:
        timestamp1 (str): The first timestamp as a string.
        timestamp2 (str): The second timestamp as a string.
        format (str, optional): The format of the timestamps. 
                                Defaults to '%Y-%m-%d %H:%M:%S'.

    Returns:
        timedelta: The time difference between the two timestamps.

    Raises:
        ValueError: If timestamps cannot be parsed with the given format.
    """
    try:
        # Convert string timestamps to datetime objects
        dt1 = datetime.strptime(timestamp1, format)
        dt2 = datetime.strptime(timestamp2, format)

        # Calculate and return the time difference
        return abs(dt2 - dt1)
    except ValueError as e:
        raise ValueError(f"Error parsing timestamps: {e}")