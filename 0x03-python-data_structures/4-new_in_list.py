#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    i = 0
    a = my_list.copy()
    while(i < len(a)):
        if idx < 0 or idx >= len(a):
            return(my_list)
        elif i == idx:
            a[i] = element
            return(a)
        i += 1
