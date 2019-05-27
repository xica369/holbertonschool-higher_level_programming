#!/usr/bin/python3
"""Module for matrix division"""


def matrix_divided(matrix, div):
    """function for division"""
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    str1 = "matrix must be a matrix (list of lists) of integers/floats"
    str2 = "Each row of the matrix must have the same size"
    lent = len(matrix[0])
    d = div

    for n in matrix:
        if len(n) != lent:
            raise TypeError(str2)
        if type(n) is not list:
            raise TypeError(str1)
        for m in n:
            if type(m) is not int and type(m) is not float:
                raise TypeError(str1)
    return list(map(lambda i: list(map(lambda j: round(j / d, 2), i)), matrix))
