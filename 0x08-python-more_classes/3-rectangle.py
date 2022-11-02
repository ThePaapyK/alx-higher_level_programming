#!/usr/bin/python3
"""A class Rectangle that defines a rectangle by: (based on 2-rectangle.py).
In addition:
print() and str() should print the rectangle with the character #:
if width or height is equal to 0, return an empty string
"""


class Rectangle:
    """Defines a Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialises rectangle
        Args:
        width (int): width of the rectangle.
        height (int): height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """returns width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        rect = ""
        if (self.__width == 0) or (self.__height == 0):
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                rect += "#"
            if i < self.__height - 1:
                rect += "\n"
        return rect