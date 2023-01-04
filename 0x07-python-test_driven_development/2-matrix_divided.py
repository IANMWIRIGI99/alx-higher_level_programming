#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.

The 2-matrix_divided module supplies one function, matrix_divided().
For example,
>>> matrix = [[1, 2, 3], [4, 5, 6]]
>>> matrix_divided(matrix, 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    """Return division of all elements of a matrix"""
    rowsz = None
    e = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list):
        raise TypeError(e)
    for elm in matrix:
        if not isinstance(elm, list):
            raise TypeError(e)
        for val in elm:
            if not isinstance(val, int) and not isinstance(val, float):
                raise TypeError(e)
        if rowsz is None:
            rowsz = len(elm)
        elif rowsz != len(elm):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return([[round(val / div, 2) for val in elm] for elm in matrix])
