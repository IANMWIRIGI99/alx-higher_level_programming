#!/usr/bin/python3
"""A class LockedClass with no class or object attribute"""


class LockedClass:
    """The module prevents the user from dynamically creating new instance
    attributes,except if the new instance attribute is called first_name"""
    __slots__ = ["first_name"]
