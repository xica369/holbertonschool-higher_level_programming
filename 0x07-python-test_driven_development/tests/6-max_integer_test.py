#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer_output(self):
        self.assertAlmostEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertAlmostEqual(max_integer([]), None)

    def test_max_integer_input(self):
        self.assertRaises(TypeError, max_integer, 123)
        self.assertRaises(TypeError, max_integer, True)
