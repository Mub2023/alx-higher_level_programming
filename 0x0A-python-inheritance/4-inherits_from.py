#!/usr/bin/python3
"""
that returns True if the object is an instance of a class
that inherited (directly or indirectly)
from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class
    that inherited (directly or indirectly) other wise false"""
    return isinstance(obj, a_class) and obj.__class__ != a_class
