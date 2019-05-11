#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    n_dictionary = {}
    for key, val in a_dictionary.items():
        if val != value:
            n_dictionary.setdefault(key, val)
    return n_dictionary
