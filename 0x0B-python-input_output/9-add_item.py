#!/usr/bin/python3
from sys import argv
from os import path
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


a = []
if path.exists("add_item.json"):
    a = load_from_json_file("add_item.json")
a = a + argv[1:]
save_to_json_file(a, "add_item.json")
