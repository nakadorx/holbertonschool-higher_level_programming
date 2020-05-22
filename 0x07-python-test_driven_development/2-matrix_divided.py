#!/usr/bin/python3
"""
Matrix div
"""


def matrix_divided(matrix, div):
    """
    div all elements of the mat
    """
    M = []

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
        return

    if div == 0:
        raise ZeroDivisionError("division by zero")
        return

    if type(matrix) is not list or matrix == [[]]:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        return

    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            return

    for row in matrix:
        for col in row:
            if type(col) is not int and type(col) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                return

    for row in matrix:
        if len(row) is not len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
            return

    for row in matrix:
        newrow = []
        for col in row:
            newrow.append(round((col / div), 2))
        M.append(newrow)
    return M
