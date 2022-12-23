#!/usr/bin/python3
"""a function that adds 2 integers."""


def add_integer(a, b=98):
    """ a and b must be integer or floats """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    _a = int(a)
    _b = int(b)

    return _a + _b
