#!/usr/bin/python3
"""class Rectangle inherits from the Base class"""
from models.base import Base


class Rectangle(Base):
    """A rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialises class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """returns value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """returns the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """returns the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the value of x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """returns the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the value of y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of the triangle"""
        return self.__width * self.__height
