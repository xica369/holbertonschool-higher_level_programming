#!/usr/bin/python3
"""Function Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """function init"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """function str"""
        return ("[Square] ({}) {}/{} - {}".
                format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """function size getter"""
        return self.width

    @size.setter
    def size(self, size):
        """function size setter"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """function update"""
        ar = ["id", "size", "x", "y"]
        if args and args != "":
            for i in range(len(args)):
                if i < 5:
                    setattr(self, ar[i], args[i])
        if kwargs and kwargs != "":
            for key, value, in kwargs.items():
                for j in ar:
                    if j == key:
                        setattr(self, j, value)

    def to_dictionary(self):
        """function dictionary"""
        dic = {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
        return dic
