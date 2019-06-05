#!/usr/bin/python3
def inherits_from(obj, a_class):
    return not issubclass(a_class, type(obj))
