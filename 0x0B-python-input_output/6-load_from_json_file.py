#!/usr/bin/python3
"""a function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """creates an object from a JSON FILE

    Args:
    filename (str): name of the file
    """
    with open(filename, encoding='utf-8') as file_:
        return json.load(file_)
