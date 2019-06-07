#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list:
            dic = {}
            for i in attrs:
                if type(i) is not str:
                    return self.__dict__
                for j in self.__dict__:
                    if i == j:
                        dic[i] = self.__dict__[j]
            return dic
        return self.__dict__

    def reload_from_json(self, json):
        return self.__dict__.update(json)
