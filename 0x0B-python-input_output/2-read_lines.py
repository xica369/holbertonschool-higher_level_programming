#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    cont = 0
    with open(filename, 'r') as f:
        for li in f:
            if nb_lines == cont and nb_lines > 0:
                break
            print(li, end="")
            cont += 1
