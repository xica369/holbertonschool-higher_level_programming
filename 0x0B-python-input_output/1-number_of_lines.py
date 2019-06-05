#!/usr/bin/python3
def number_of_lines(filename=""):
    cont = 0
    with open(filename, 'r') as f:
        for li in f:
            cont += 1
    return cont
