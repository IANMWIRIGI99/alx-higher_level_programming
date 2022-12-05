#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        max_ = None
    if len(my_list) > 0:
        max_ = my_list[0]
        for value in my_list:
            if(value > max_):
                max_ = value
    return(max_)
