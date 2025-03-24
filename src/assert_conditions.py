def check_conditions(*conditions):
    """
    Validate multiple conditions using assert statements.

    This function takes multiple conditions as arguments and uses assert 
    statements to check if all conditions are True. If any condition fails, 
    an AssertionError is raised with a descriptive message.

    Args:
        *conditions (tuple): Variable number of conditions to check.
                             Each condition should be a tuple of (condition, error_message)

    Raises:
        AssertionError: If any of the provided conditions evaluate to False

    Examples:
        >>> check_conditions((5 > 3, "5 is not greater than 3"))
        >>> check_conditions(
        ...     (5 > 3, "5 is greater than 3"),
        ...     (len([1, 2, 3]) == 3, "List has exactly 3 elements")
        ... )
    """
    # Validate input is not empty
    if not conditions:
        raise ValueError("At least one condition must be provided")

    # Check each condition
    for condition, error_message in conditions:
        # Use assert to validate the condition
        assert condition, error_message

    # If all conditions pass, return True
    return True