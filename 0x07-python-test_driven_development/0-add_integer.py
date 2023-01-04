#!/usr/bin/python3
"""
This is the 0-add_integer module.

The 0-add_integer module supplies one function, add_integer().  For example,

>>> add_integer(2, 3)
5
"""


def add_integer(a, b=98):
    """Return the addition of 2 integers"""
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    if type(a) is int and type(b) is int:
        sum = a + b
        return(sum)
