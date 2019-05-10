#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    Ndictionary = {}
    for key, value in a_dictionary.items():
        Ndictionary.setdefault(key, (value * 2))
    return Ndictionary
