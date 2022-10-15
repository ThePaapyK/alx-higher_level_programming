#!/usr/bin/python3
"""A class Square that defines a square by: (based on 4-square.py) +
Public instance method: def my_print(self): that prints in stdout
 the square with the character #:
if size is equal to 0, print an empty line

"""



class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.
        Args:
        size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints in stdout the square with the character #

        if the size is zero, print an empty line
        """
        if (self.__size == 0):
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("")
