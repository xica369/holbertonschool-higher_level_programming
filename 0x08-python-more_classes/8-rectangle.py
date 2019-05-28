#!/usr/bin/python3
class Rectangle:

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            TypeError("width must be an integer")
        if value < 0:
            ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            TypeError("height must be an integer")
        if value < 0:
            ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        return self.__height * 2 + self.__width * 2

    def __str__(self):
        string = ''
        if self.__height != 0 and self.__width != 0:
            for i in range(self.__height):
                string += str(self.print_symbol) * self.__width + '\n'
        return string[:-1]

    def __repr__(self):
        string = ''
        string += "Rectangle(" + str(self.__width) + ", "
        string += str(self.__height) + ")"
        return string

    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
