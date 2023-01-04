#!/usr/bin/python3
"""
Module to find the max integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Test the max_integer function
    """

    def test_max_integer(self):
        """
        Test if integer is max integer
        """
        result = max_integer([2, 5, 4, 1])
        self.assertEqual(result, 5)
        result = max_integer([11, 8, 5, 7])
        self.assertEqual(result, 11)

    def test_isint(self):
        """
        Test to check variable against integer
        """
        m = 1
        self.assertTrue(max_integer([m, 3]) == 3)
        p = 5
        self.assertTrue(max_integer([2, p]) == p)

    def test_same_entry(self):
        """
        Test to check max int if same
        """
        n = 50
        self.assertEqual(max_integer([n, n, n, n]), n)

    def test_float_integer(self):
        """
        Test to see if float is max integer
        """
        self.assertEqual(max_integer([5.0, 4, 3]), 5.0)

    def test_one_entry(self):
        """
        Test to check if only one entry
        """
        self.assertEqual(max_integer([11]), 11)

    def test_negative_integer(self):
        """
        Test only negative integers
        """
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_no_argument(self):
        """
        Test that None is returned if no argument
        """
        self.assertEqual(max_integer(), None)

    def test_empty_list(self):
        """
        Test if list is empty
        """
        self.assertEqual(max_integer([]), None)

    if __name__ == '__main__':
        unittest.main()
