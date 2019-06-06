#!/usr/bin/python3
from json import dumps


def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as f:
        a = dumps(my_obj)
        f.write(a)
