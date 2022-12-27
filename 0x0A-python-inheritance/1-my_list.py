#!/usr/bin/python3
"""class that inherits from list"""


class MyList(list):
    """class that inherits from list"""
    def __init__(self):
        """initializes the object"""
        super().__init__()
    def print_sorted(self):
        """prints a sorted list of list items"""
        print(sorted(self))
