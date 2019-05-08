#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    aux = 1
    for i in matrix:
        for j in i:
            if aux < len(i):
                print("{:d}".format(j), end=" ")
            else:
                print("{:d}".format(j), end="")
            aux = aux + 1
        aux = 1
        print()
