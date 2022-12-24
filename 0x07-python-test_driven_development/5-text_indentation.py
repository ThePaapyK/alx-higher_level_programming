#!/usr/bin/python3
"""prints a text with 2 new lines after each of \
these characters: ., ? and :"""


def text_indentation(text):
    """prints a text with 2 new lines after each of \
    these characters: ., ? and :"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    prev = ''
    for i in text:
        if (prev == ".") or (prev == "?") or (prev == ":"):
            print("")
            print("")
            if i != ' ':
                print(i, end="")
        else:
            print(i, end="")
        prev = i
