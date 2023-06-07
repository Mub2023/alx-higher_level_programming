#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrixD = [[1, 4, 80],[5, 6, 7],[55, 77, 11]]
matrixS = [[1, 4, 80],[5, 2, 5]]
noneL = None
empty = []
empty_matrix = [[], [], []]
not_num = [[10, 'as1', 50],[50, 'ww', 5]]
not_same_len = [[10, 50],[10, 50, 77]]
not_list = [[1, 10, [2, 22]],[10, [55, 1], [11, 2]]]
matrix = [
    [1, 2, 4, 3, -4],
    [4, 5, 5, 6 , -5, 10]
]
noneL = None
print(matrix_divided(matrixS, 20))

print(matrix)
