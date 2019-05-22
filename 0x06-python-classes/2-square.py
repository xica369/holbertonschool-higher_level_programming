#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise TypeError
            print("size must be an integer")
        if size < 0:
            raise ValueError
            print("size must be >= 0")
