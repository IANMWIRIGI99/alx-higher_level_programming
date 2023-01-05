#!/usr/bin/python3
"""An empty class Rectangle that defines a rectangle."""


class Rectangle:
    """Module of a rectangle


    Attributes:
        __width (int): Decribes the width of a rectangle
        __height (int): Describes the height of a rectangle
    """
    def __init__(self, width=0, height=0):
        """Initializes the rectangle attributes


        Args:
            width (int): Decribes the width of a rectangle
            height (int): Describes the height of a rectangle


        Returns:
            None
        """
        self.width = width
        self.height = height

    def area(self):
        """Calculates area of a rectangle


        Returns:
            the rectangle area
        """
        return(self.__width * self.__height)

    def perimeter(self):
        """Calculates perimeter of a rectangle


        Returns:
            the rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return(0)
        else:
            return ((self.__width * 2) + (self.__height * 2))

    @property
    def width(self):
        """getting the width


        Returns:
            the width of a rectangle
        """
        return(self.__width)

    @property
    def height(self):
        """getting the height


        Returns:
            the height of a rectangle
        """
        return(self.__height)

    @width.setter
    def width(self, value):
        """setting the width


        Args:
            value (int):Describes the width of a rectangle


        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """setting the height


        Args:
            value (int):Describes the height of a rectangle


        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
