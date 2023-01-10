#!/usr/bin/python3
"""A function that returns a list of lists of integers
representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    """returns an empty list if n <= 0"""
    if n <= 0:
        return([])

    l_list = [[1]]
    for i in range(1, n):
        row = [1]
        for elm in range(1, i):
            row.append(l_list[i - 1][elm - 1] + l_list[i - 1][elm])
        row.append(1)
        l_list.append(row)
    return(l_list)
