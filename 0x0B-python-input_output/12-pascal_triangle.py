#!/usr/bin/python3
""" that returns a list of lists of
integers representing the
Pascal’s triangle of n"""


def pascal_triangle(n):
    """returns the pascal's triangle of n"""
    if n <= 0:
        return []

    tri = [[1]]
    while len(tri) != n:
        t = tri[-1]
        x = [1]
        for y in range(len(t) - 1):
            x.append(t[y] + t[y + 1])
        x.append(1)
        tri.append(x)
    return tri
