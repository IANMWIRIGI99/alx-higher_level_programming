#!/usr/bin/python3
"""
A function that checks if object is an instance of a class that
inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """Returns True if condition passes ; otherwise False."""
    return(type(obj) != a_class and issubclass(type(obj), a_class))
