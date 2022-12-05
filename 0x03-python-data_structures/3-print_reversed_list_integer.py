#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        a = my_list[::-1]
        for value in a:
            print("{:d}".format(value), end="\n")
