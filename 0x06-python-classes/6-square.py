#!/usr/bin/python3
""" a class `Square` that defines a square by: (based on `5-square.p`y) +
Private instance attribute: position:
property def position(self): to retrieve it
property setter def position(self, value): to set it:
position must be a tuple of 2 positive integers, otherwise raise a
TypeError exception with the message
`position must be a tuple of 2 positive integers`
Instantiation with optional size and optional position:
`def __init__(self, size=0, position=(0, 0)):`
Public instance method: def my_print(self):
that prints in stdout the square with the character #:
if size is equal to 0, print an empty line
position should be use by using space -
Don’t fill lines by spaces when position[1] > 0

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
        if (not isinstance(value, tuple) or
              len(value) != 2 or
              not all(isinstance(i, int) for i in value) or
              not all(i >= 0 for i in value)):
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
                    print(" ", end ="")
                for j in range(self.__size):
                    print("#", end="")
                print("")
