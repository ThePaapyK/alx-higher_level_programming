#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMax(unittest.TestCase):
    def test_max_end(self):
        self.assertEqual(max_integer([1, 3, 4, 9]), 9)
        self.assertEqual(max_integer([9, 4, 6, 3, 2]), 9)
        self.assertEqual(max_integer([2, 4, 10, 5, 6]), 10)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([2, -1, 4, 7]), 7)
        self.assertEqual(max_integer([-1, -3, -9, -6]), -1)
        self.assertEqual(max_integer([8]), 8)
