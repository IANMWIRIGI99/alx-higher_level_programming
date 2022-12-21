#!/usr/bin/python3
"""A class Square that defines a square"""


class Square:
    """Module of a square
    Attributes:
        __size (int): Describes the length of a square
    """
    def __init__(self, size=0):
        """Initializes the square attributes
        Args:
            size (int): Describes the length of a square
        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates area of a square
        Returns:
            the current square area
        """
        return (f"{self.__size*self.__size}")
