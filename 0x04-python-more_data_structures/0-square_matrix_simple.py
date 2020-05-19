#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n = []
    for i in range(len(matrix)):
        k = []
        for j in range(len(matrix[i])):
            k.append(matrix[i][j] ** 2)
        n.append(k)
    return n
