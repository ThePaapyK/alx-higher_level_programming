#!/usr/bin/python3
""" A class Rectangle that defines a rectangle by: (based on 7-rectangle.py).
In addition:
Static method def bigger_or_equal(rect_1, rect_2):
that returns the biggest rectangle based on the area
rect_1 must be an instance of Rectangle, otherwise raise
a TypeError exception with the message rect_1 must be an instance of Rectangle
rect_2 must be an instance of Rectangle, otherwise raise
a TypeError exception with the message rect_2 must be an instance of Rectangle
Returns rect_1 if both have the same area value
"""


class Rectangle:
    """Defines a Rectangle
    Args:
    number_of_instances (int): number of instances in the class
    print_symbol (any type): symbol for string representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialises rectangle
        Args:
        width (int): width of the rectangle.
        height (int): height of the rectangle.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __str__(self):
        rect = ""
        if (self.__width == 0) or (self.__height == 0):
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                rect += str(self.print_symbol)
            if i < self.__height - 1:
                rect += "\n"
        return rect

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        if rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2
