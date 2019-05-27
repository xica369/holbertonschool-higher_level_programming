#!/usr/bin/python3
"""Module to test the function max_integer"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_integer_output(self):
        """Function to test the output the function max_integer"""

        self.assertAlmostEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([1]), 1)
        self.assertAlmostEqual(max_integer(), None)

    def test_max_integer_input(self):
        """Function to test the input the function max_integer"""

        self.assertRaises(TypeError, max_integer, 123)
        self.assertRaises(TypeError, max_integer, True)
