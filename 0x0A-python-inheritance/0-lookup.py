#!/usr/bin/python3
"""returns the list of available
attributes and methods of an object
"""


def lookup(obj):
    """the list of available attributes
    and methods of an object
    Args:
        obj: any python object.
    Return: a list object
    """
    return (dir(obj))
