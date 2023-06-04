#!/usr/bin/python3
"""
 divides all elements of a matrix.
 must be a list of lists of integers or floats.matrix must be of the same size.
 div can’t be equal to 0.
"""


def matrix_divided(matrix, div):
    """divides all elements of a matrix.
    Return the new matrix
    """
    ERR = "matrix must be a matrix (list of lists) of integers/floats"
    if matrix is None:
        raise TypeError(ERR)
    if not matrix:
        raise TypeError(ERR)
    if not isinstance(matrix, list):
        raise TypeError(ERR)
    for l in matrix:
        if not isinstance(l, list):
            raise TypeError(ERR)
    if not all(isinstance(e, (int, float)) for row in matrix for e in row):
        raise TypeError(ERR)
    for l in matrix:
        if len(l) == 0:
            raise TypeError(ERR)
    new_matrix = matrix.copy()
    first_row = len(new_matrix[0])
    for row in new_matrix:
        if len(row) != first_row:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(num / div, 2) for num in row] for row in new_matrix]
    return (new_matrix)
