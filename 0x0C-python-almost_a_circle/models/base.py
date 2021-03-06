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

    @staticmethod
    def from_json_string(json_string):
        """from_json_string function"""
        lis = []
        if json_string:
            lis = json.loads(json_string)
        return lis

    @classmethod
    def create(cls, **dictionary):
        """create function"""
        cla = cls.__name__
        if cla == "Rectangle":
            dummy = cls(3, 4)
        if cla == "Square":
            dummy = cls(3)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """load from file function"""
        lis = []
        name = cls.__name__ + ".json"
        try:
            with open(name, "r") as f:
                read = json.load(f)
                l = cls.from_json_string(read)
                dummy = cls.create(l)
                return dummy
        except:
            return lis

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save to file csv function"""
        name = cls.__name__ + ".csv"
        with open(name, 'w') as f:
            for j in list_objs:
                a = json.dumps(j)
            f.write(a)

    @classmethod
    def load_from_file_csv(cls):
        """load from file csv function"""
        name = cls.__name__ + ".csv"
        with open(name, 'r') as f:
            return json.loads(f.read())
