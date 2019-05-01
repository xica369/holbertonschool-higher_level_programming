#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) > 96 and ord(i) < 123:
            charac = ord(i) - 32
        else:
            charac = ord(i)
        print("{}".format(chr(charac)), end="")
    print()
