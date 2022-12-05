#!/usr/bin/python3
def no_c(my_string):
    replacement = ""
    for value in my_string:
        if value != 'c' and value != 'C':
            replacement += value
    return(replacement)
