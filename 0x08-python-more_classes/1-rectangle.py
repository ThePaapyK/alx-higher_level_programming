#!/usr/bin/python3
"""
A class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
Private instance attribute: width:
property def width(self): to retrieve it
property setter def width(self, value): to set it:
width must be an integer, otherwise raise a TypeError exception
with the message width must be an integer
if width is less than 0, raise a ValueError exception
with the message width must be >= 0

Private instance attribute: height:
property def height(self): to retrieve it
property setter def height(self, value): to set it:
height must be an integer, otherwise raise a TypeError exception
with the message height must be an integer
if height is less than 0, raise a ValueError exception
with the message height must be >= 0

Instantiation with optional width and height:
def __init__(self, width=0, height=0):
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
            raise ValueError("height must be an integer")
        self.__height = value
