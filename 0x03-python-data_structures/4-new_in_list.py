#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        join = my_list[:]
        if 0 <= idx < len(my_list):
            join[idx] = element
    return join
