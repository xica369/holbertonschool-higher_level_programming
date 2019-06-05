#!/usr/bin/python3
class MyInt(int):
    def __init__(self, value):
        self.num = value

    def __eq__(self, val):
        return self.val
