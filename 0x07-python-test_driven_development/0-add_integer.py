#!/usr/bin/python3
"""function that adds 2 integers
a and b must be integers or floats
otherwise raise a TypeError
Return: an integer the addition of a and b.
"""


def add_integer(a, b=98):
    """add two numbers a + b
    a and b will be casted into integers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, (float)):
        a = int(a)
    if isinstance(b, (float)):
        b = int(b)
    return a + b
