# Problem statement: Write a function that accepts a square matrix (N x N 2D array) and returns the determinant of the matrix.
def determinant(matrix):
    # recursive function
    result = 0
    if not matrix:
        return None
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        for i in matrix:
            sub_matrix = []
            # multiply each sub-determinant by first column
            sub_matrix = [(row[0:i]+row[i+1:]) for row in matrix[1:]] # determinant formula for sub-matrices
        result = sub_matrix = ((-1)**i) * matrix[0][i] * determinant(sub_matrix)
    return result