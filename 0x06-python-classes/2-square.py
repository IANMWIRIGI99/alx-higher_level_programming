#!/usr/bin/python3
"""
Define a class square
"""


class Square:
    """
    class Square that defines a square by: (based on 1-square.py)
    """

    def __init__(self, size=0):
        """
        Create an instance of Square
        Args:
            size: size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
