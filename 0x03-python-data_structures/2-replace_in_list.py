#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    i = 0
    while(i < len(my_list)):
        if idx < 0 or idx >= len(my_list):
            return(my_list)
        elif i == idx:
            my_list[i] = element
            return(my_list)
        i += 1
