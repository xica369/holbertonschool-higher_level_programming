#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.__size = size
    def size(self, value):
        if type(size) != int:
            raise TypeError
            print("size must be an integer")
        if size < 0:
            raise ValueError
            print("size must be >= 0")
    def area(self):
        return self.__size * self.__size
