#!/usr/bin/python3
"""This is the class Base"""
from json import dumps


class Base:
    """class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """init function"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string function"""
        if list_dictionaries is None or is not list_dictionaries:
            return "[]"
        return dumps(list_dictionaries)
