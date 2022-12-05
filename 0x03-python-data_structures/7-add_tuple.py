#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    zero_tuple = (0, )
    i = len(tuple_a)
    j = len(tuple_b)
    if i > 2:
        w = tuple_a[0]
        x = tuple_a[1]
        tuple_a = (w, x)
    if j > 2:
        y = tuple_b[0]
        z = tuple_b[1]
        tuple_b = (y, z)
    if i < 2:
        while(i < 2):
            tuple_a = tuple_a + zero_tuple
            i += 1
    if j < 2:
        while(j < 2):
            tuple_b = tuple_b + zero_tuple
            j += 1
    a1, a2 = tuple_a
    b1, b2 = tuple_b
    a = a1 + b1
    b = a2 + b2
    new_tuple = (a, b)
    return(new_tuple)
