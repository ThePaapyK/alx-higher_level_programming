#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = [[x**2, y**2] for [x, y] in matrix]
    return new_matrix
