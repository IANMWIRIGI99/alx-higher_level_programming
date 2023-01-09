#!/usr/bin/python3
"""
A class Square that inherits from Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Module of a square"""
    def __init__(self, size):
        """Initializes the square attributes


        Args:
            size (int): Describes the length of a square


        Returns:
            None
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Calculates area of a square


        Returns:
            the square area
        """
        return(self.__size ** 2)

    def __str__(self):
        """Represents the Square objects as a string


        Returns:
            the 'informal' representing string
        """
        return(f"[Square] {self.__size}/{self.__size}")
