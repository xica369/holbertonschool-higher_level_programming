#!/usr/bin/pyton3
from models.base import Base
"""Fuction Rectangle"""


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """function init"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
                raise ValueError("height must be > 0")
        self.__height = height
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if type(y) is not int:
                raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """function getter width"""
        return self.__width

    @width.setter
    def width(self, width):
        """function setter width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """function getter height"""
        return self.__height

    @height.setter
    def height(self, height):
        """function setter height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """function getter x"""
        return self.__x

    @x.setter
    def x(self, x):
        """function setter x"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """function getter y"""
        return self.__y

    @y.setter
    def y(self, y):
        """function setter y"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """function getter area"""
        return self.__width * self.__height

    def display(self):
        """function display"""
        i = 0
        j = 0
        for j in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + '#' * self.__width)

    def __str__(self):
        """function str"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".
                format(self.id, self.__x, self.__y, self.__width,
                       self.__height))

    def update(self, *args):
        """function update all attributes"""
        ar = ["id", "width", "height", "x", "y"]
        i = 0
        for i in range(len(args)):
            if i < 5:
                setattr(self, ar[i], args[i])
