#!/usr/bin/python3
"""
Define a class square
"""


class Square:
    """
    class Square that defines a square by: (based on 4-square.py)
    """

    def __init__(self, size=0):
        """
        Create instance of Square
        Args:
            size: size of the square
        """
        self.size = size

    @property
    def size(self):
        """
        Set and get the value of private size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Find area of square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square using #
        """
        for i in range(self.__size):
            print("#" * self.__size)

        if (self.__size == 0):
            print()
