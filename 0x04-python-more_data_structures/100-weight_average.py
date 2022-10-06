#!/usr/bin/python3

""" finds the weighted average of scores """


def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    add = 0
    divisor = 0
    for row in my_list:
        add = add + (row[0] * row[1])
        divisor = divisor + row[1]

    avg = add / divisor
    return avg
