#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    Nmatrix = []
    for i in range(len(matrix)):
        Nmatrix.append(list(map(lambda x: x * x, matrix[i])))
    return Nmatrix
