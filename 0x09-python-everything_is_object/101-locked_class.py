#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """prevents the dynamic creation of new instances attributes except
    if the instance attribute is called first_name
    """
    __slots__ = ["first_name"]
