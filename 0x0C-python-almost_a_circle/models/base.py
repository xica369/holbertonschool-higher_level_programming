#!/usr/bin/python3
"""This is the class Base"""
import json


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
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save to file - function"""
        lis = []
        name = cls.__name__ + ".json"
        if list_objs:
            for j in list_objs:
                lis.append(j.to_dictionary())
        with open(name, 'w') as f:
            f.write(cls.to_json_string(lis))
