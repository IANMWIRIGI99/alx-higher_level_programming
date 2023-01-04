#!/usr/bin/python3
"""
This is the 100-matrix_mul module.

The 100-matrix_mul module supplies one function, def matrix_mul().
For example,
>>> matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
[[7, 10], [15, 22]]
"""


def matrix_mul(m_a, m_b):
    """Return result of multiplication of 2 matrices"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    len_a = len(m_a)
    if len_a == 0:
        raise ValueError("m_a can't be empty")
    len_b = None
    for elm in m_a:
        if type(elm) is not list:
            raise TypeError("m_a must be a list of lists")
        if len_b is None:
            len_b = len(elm)
            if len_b == 0:
                raise ValueError("m_a can't be empty")
        if len_b != len(elm):
            raise TypeError("each row of m_a must be of the same size")
        for val in elm:
            if type(val) is not int and type(val) is not float:
                raise TypeError("m_a should contain only integers or floats")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    len_elm = None
    for elm in m_b:
        if type(elm) is not list:
            raise TypeError("m_b must be a list of lists")
        if len_elm is None:
            len_elm = len(elm)
            if len_elm == 0:
                raise ValueError("m_b can't be empty")
        if len_elm != len(elm):
            raise TypeError("each row of m_b must be of the same size")
        for val in elm:
            if type(val) is not int and type(val) is not float:
                raise TypeError("m_b should contain only integers or floats")
    if len_b != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    result = []
    for elm in range(len_a):
        x = []
        for i in range(len_elm):
            y = 0
            for j in range(len_b):
                y += m_a[elm][j] * m_b[j][i]
            x.append(y)
        result.append(x)
    return(result)
