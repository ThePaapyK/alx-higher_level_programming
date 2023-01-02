#!/usr/bin/python3
"""This module has a function that writes \
an Object to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, \
    using a JSON representation:

    Args:
    my_obj (object): object to be added
    filename (str): name of the file
    """
    with open(filename, mode='w', encoding='utf-8') as file_:
        json.dump(my_obj, file_)
