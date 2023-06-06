#!/usr/bin/python3
"""a function that multiplies 2 matrices:
    m_a: is matrix to multipleis.
    m_b: is matrix to multipleis.
    return: the multipleis list.
    """


def matrix_mul(m_a, m_b):
    """
    that multiplies 2 matrices:
    m_a * m_b"""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    for x in m_a:
        if not isinstance(x, list):
            raise TypeError("m_a must be a list of lists")
    for x in m_b:
        if not isinstance(x, list):
            raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    for y in m_a:
        if len(y) == 0:
            raise ValueError("m_a can't be empty")
    for y in m_b:
        if len(y) == 0:
            raise ValueError("m_b can't be empty")
    for t in list(m_a):
        for g in t:
            if not isinstance(g, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for w in list(m_b):
        for g in w:
            if not isinstance(g, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    for row in m_a:
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    for row in m_b:
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for z in range(len(m_a)):
        row = []
        for v in range(len(m_b[0])):
            p = 0
            for k in range(len(m_b)):
                p += m_a[z][k] * m_b[k][v]

            row.append(p)
        result.append(row)
    return result
