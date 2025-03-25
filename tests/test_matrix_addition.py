import pytest
from src.matrix_addition import add_matrices

def test_basic_matrix_addition():
    # Test basic 2x2 matrix addition
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]
    expected = [[6, 8], [10, 12]]
    assert add_matrices(matrix1, matrix2) == expected

def test_different_number_of_rows():
    # Test error when matrices have different number of rows
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6]]
    with pytest.raises(ValueError, match="Number of rows must match"):
        add_matrices(matrix1, matrix2)

def test_different_row_lengths():
    # Test error when rows have different lengths
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8, 9]]
    with pytest.raises(ValueError, match="Row 1 lengths do not match"):
        add_matrices(matrix1, matrix2)

def test_empty_matrices():
    # Test error when either matrix is empty
    matrix1 = []
    matrix2 = [[1, 2], [3, 4]]
    with pytest.raises(ValueError, match="Matrices cannot be empty"):
        add_matrices(matrix1, matrix2)

def test_single_element_matrices():
    # Test addition of single-element matrices
    matrix1 = [[5]]
    matrix2 = [[3]]
    expected = [[8]]
    assert add_matrices(matrix1, matrix2) == expected

def test_matrix_with_negative_numbers():
    # Test matrix addition with negative numbers
    matrix1 = [[-1, -2], [-3, -4]]
    matrix2 = [[1, 2], [3, 4]]
    expected = [[0, 0], [0, 0]]
    assert add_matrices(matrix1, matrix2) == expected

def test_float_matrices():
    # Test matrix addition with floating-point numbers
    matrix1 = [[1.5, 2.5], [3.5, 4.5]]
    matrix2 = [[0.5, 1.5], [2.5, 3.5]]
    expected = [[2.0, 4.0], [6.0, 8.0]]
    assert add_matrices(matrix1, matrix2) == expected