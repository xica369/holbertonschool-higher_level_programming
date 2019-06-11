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
