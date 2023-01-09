#!/usr/bin/python3
"""
A class Rectangle that inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Module of a rectangle"""
    def __init__(self, width, height):
        """Initializes the rectangle attributes"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
