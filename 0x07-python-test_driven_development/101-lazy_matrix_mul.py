#!/usr/bin/python3
"""
This is the 101-lazy_matrix_mul module.

The 101-lazy_matrix_mul module supplies one function, def lazy_matrix_mul().
For example,
>>> print(lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
[[ 7 10]
 [15 22]]
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Return result of multiplication of 2 matrices by NumPy"""
    return(np.matmul(m_a, m_b))
