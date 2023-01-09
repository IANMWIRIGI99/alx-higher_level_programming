#!/usr/bin/python3
"""
A class MyInt that inherits from int
"""


class MyInt(int):
    """Module of a rebel"""
    def __new__(cls, *args, **kwargs):
        """creates object inside __new__ method by using super"""
        return(super(MyInt, cls).__new__(cls, *args, **kwargs))

    def __eq__(self, other):
        """!= inverted to =="""
        return(int(self) != other)

    def __ne__(self, other):
        """== inverted to !="""
        return(int(self) == other)
