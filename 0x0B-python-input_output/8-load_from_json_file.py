#!/usr/bin/python3
from json import loands


def load_from_json_file(filename):
    with open(filename, 'r') as f:
        return loads(f.read())
