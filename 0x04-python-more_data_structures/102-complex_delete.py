#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_with_val = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            keys_with_val.append(key)
    for key in keys_with_val:
        del a_dictionary[key]
    return(a_dictionary)
