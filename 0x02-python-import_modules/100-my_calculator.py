#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        tabla = {'+': add, '-': sub, '*': mul, '/': div}
        for sig, op in tabla.items():
            if argv[2] == sig:
                print("{:s} {:s} {:s} = {:d}".
                      format(argv[1], argv[2], argv[3],
                             op(int(argv[1]), int(argv[3]))))
                exit(0)
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
