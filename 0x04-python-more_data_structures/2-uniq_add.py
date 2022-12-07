#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    uniq_list = []
    uniq_no = set(my_list)
    for value in uniq_no:
        uniq_list.append(value)
        result += value
    return(result)
