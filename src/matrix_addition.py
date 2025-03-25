def add_matrices(matrix1, matrix2):
    """
    Add two matrices element-wise, with error checking for compatibility.
    
    Args:
        matrix1 (list of lists): First input matrix 
        matrix2 (list of lists): Second input matrix
    
    Returns:
        list of lists: A new matrix with element-wise addition of input matrices
    
    Raises:
        ValueError: If matrices are not compatible for addition
    """
    # Check if matrices are empty
    if not matrix1 or not matrix2:
        raise ValueError("Matrices cannot be empty")
    
    # Check number of rows
    if len(matrix1) != len(matrix2):
        raise ValueError(f"Number of rows must match. Matrix1 has {len(matrix1)} rows, Matrix2 has {len(matrix2)} rows")
    
    # Check number of columns in each row
    for i in range(len(matrix1)):
        if len(matrix1[i]) != len(matrix2[i]):
            raise ValueError(f"Row {i} lengths do not match. Matrix1 row length: {len(matrix1[i])}, Matrix2 row length: {len(matrix2[i])}")
    
    # Perform element-wise addition
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    
    return result