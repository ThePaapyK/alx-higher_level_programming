#!/usr/bin/python3
"""Contains the base class"""


class Base:
    """The base class from which other classes inherit"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialises class
        Args:
        id (int): an id to be assigned to an instance"""
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
