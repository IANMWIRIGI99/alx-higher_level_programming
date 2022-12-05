#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for element in matrix:
        print(" ".join("{:d}".format(value) for value in element))
