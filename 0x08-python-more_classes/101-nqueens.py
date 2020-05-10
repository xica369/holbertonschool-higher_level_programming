#!/usr/bin/python3

"""program that solves the N queens problem

Usage: nqueens N

where N must be an integer greater or equal to 4
The program should print everrow possible solution to the problem
"""

import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

if sys.argv[1].isdigit() is False:
    print("N must be a number")
    exit(1)

Nq = int(sys.argv[1])

if Nq < 4:
    print("N must be at least 4")
    exit(1)
