#!/usr/bin/python3
""" A class Square that defines a square by: (based on 6-square.py).
In addition,
Printing a Square instance should have the same behavior as my_print()
"""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.
        Args:
        size (int): The size of the new square
        position (int, int): a tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or \
               len(value) != 2 or \
               not all(isinstance(i, int) for i in value) or \
               not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
            for n in range(self.__position[1]):
                print("")

            for i in range(self.__size):
                for m in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")

    def __repr__(self):
        sqr = ""
        if (self.__size == 0):
            sqr = ""
        else:
            for t in range(self.__position[1]):
                sqr += "\n"
            for u in range(self.__size):
                for v in range(self.__position[0]):
                    sqr += " "
                for w in range(self.__size):
                    sqr += "#"
                if u < (self.__size - 1):
                    sqr += "\n"
        return sqr
