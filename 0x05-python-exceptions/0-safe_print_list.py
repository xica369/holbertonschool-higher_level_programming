#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        for j in range(x):
            print("{:d}".format(my_list[j]), end="")
            i = i + 1
        print()
        return i
    except IndexError:
        print()
        return i
