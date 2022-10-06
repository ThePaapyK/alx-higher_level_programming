#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    keel = list(a_dictionary)
    new_dict = dict(map(lambda i: (i, a_dictionary[i] * 2), keel))
    return new_dict
