#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 3-square.py)

Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:

"""


class Square:
    """Defines a square with size"""

    def __init__(self, size=0):
        """ Initializes a new square

        Args:
        size (int): size of the new square

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        return (self.__size)**2

    def size(self):
        return self.__size

    def size(self, value):
        """Sets the size of the square

        Args:
        value (int): value of size

        """
        self.__size = value
