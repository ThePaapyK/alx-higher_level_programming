#!/usr/bin/python3
"""reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """opens file and prints it content"""
    with open(filename, encoding='utf-8') as file_:
        for line in file_:
            print(line, end="")
