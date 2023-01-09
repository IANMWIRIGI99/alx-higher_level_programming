#!/usr/bin/python3
"""
A class MyList that inherits from list
"""


class MyList(list):
    """Derived class of super class list"""
    def __init__(self):
        """initializes the object's attributes"""
        super().__init__()
        """Calls the initialization method of the super class list"""

    def print_sorted(self):
        """prints the sorted list (ascending sort)"""
        print(sorted(self))
