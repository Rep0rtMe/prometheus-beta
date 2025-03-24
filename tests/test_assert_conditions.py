import pytest
from src.assert_conditions import check_conditions

def test_single_true_condition():
    """Test that a single true condition passes"""
    assert check_conditions((5 > 3, "5 should be greater than 3")) is True

def test_multiple_true_conditions():
    """Test that multiple true conditions pass"""
    assert check_conditions(
        (5 > 3, "5 should be greater than 3"),
        (len([1, 2, 3]) == 3, "List should have 3 elements")
    ) is True

def test_false_condition_raises_assertion_error():
    """Test that a false condition raises an AssertionError"""
    with pytest.raises(AssertionError, match="5 is not less than 3"):
        check_conditions((5 < 3, "5 is not less than 3"))

def test_multiple_conditions_first_false():
    """Test that the first false condition stops execution and raises AssertionError"""
    with pytest.raises(AssertionError, match="First condition fails"):
        check_conditions(
            (3 > 5, "First condition fails"),
            (len([1, 2, 3]) == 3, "This condition won't be checked")
        )

def test_empty_conditions_raises_value_error():
    """Test that providing no conditions raises a ValueError"""
    with pytest.raises(ValueError, match="At least one condition must be provided"):
        check_conditions()

def test_complex_conditions():
    """Test more complex conditions"""
    assert check_conditions(
        (isinstance(42, int), "Should be an integer"),
        (42 % 2 == 0, "Should be an even number")
    ) is True

def test_falsy_values():
    """Test conditions with falsy values"""
    with pytest.raises(AssertionError, match="List should not be empty"):
        check_conditions((bool([]), "List should not be empty"))

def test_truthy_values():
    """Test conditions with truthy values"""
    assert check_conditions((bool([1, 2, 3]), "Non-empty list")) is True