#!/usr/bin/python3
"""
A function that checks if object is an instance of, or if
object is an instance of a class that inherited from,
the specified class.
"""


def is_kind_of_class(obj, a_class):
    """Returns True if condition passes ; otherwise False."""
    return(isinstance(obj, a_class))
