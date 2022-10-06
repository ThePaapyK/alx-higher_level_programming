#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    new_l = sorted(a_dictionary)
    for i in new_l:
        print("{}: {}".format(i, a_dictionary[i]))
