#!/usr/bin/python3
""" defines a class, BaseGeometry"""


class BaseGeometry:
    """A class"""
    def __init__(self):
        """Initialises the object"""

    def area(self):
        """raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
