#!/usr/bin/python3
"""This module has a function that returns the object form \
of a JSON string
"""
import json


def from_json_string(my_str):
    """returns an object (Python data structure) \
    represented by a JSON string

    Args:
    my_str (str): JSON string
    """
    return json.loads(my_str)
