#!/usr/bin/python3
"""
test test max
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class testlist(unittest.TestCase):
    """
    testlist
    """
    def test_max(self):
        """
        testlist testlist
        """
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer(""), None)
        self.assertEqual(max_integer([5, 3, 7]), 7)
        self.assertEqual(max_integer([25, 1, 3]), 25)
        self.assertEqual(max_integer([1, 1, -1, -6]), 1)
        self.assertEqual(max_integer("zkataf"), "z")
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([[50, 70], [100, 10]]), [100, 10])
        self.assertEqual(max_integer([5, 7, 9, 8, 9, 10]), 10)
        with self.assertRaises(TypeError):
            max_integer(["yo man", 1, 2])
