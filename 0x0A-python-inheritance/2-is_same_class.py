#!/usr/bin/python3
"""
medlule returns True if the object is exactly an instance
of the specified class ; otherwise False.
"""

def is_same_class(obj, a_class):
    """check if if the object is exactly
    an instance of the specified class
    """
    return type(obj) == a_class
