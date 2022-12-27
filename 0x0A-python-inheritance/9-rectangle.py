#!/usr/bin/python3
"""Defines a sublcass of BaseGeometry called Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inherits from BaseGeometry"""
    def __init__(self, width, height):
        """initializes the object

        Args:
        width (int): The width of the rectangle
        height (int): the height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns the following"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
