#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    for s in range(len(matrix)):
        new_matrix[s] = list(map(lambda x: x**2, matrix[s]))
    return (new_matrix)
