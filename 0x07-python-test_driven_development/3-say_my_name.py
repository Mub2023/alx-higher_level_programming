#!/usr/bin/python3
"""
prints My name is <first name> <last name>
first_name and last_name must be strings.
Return: the my name is <first name> <last name>.
"""


def say_my_name(first_name, last_name=""):
    """
    prints first name and last name
    first name and last name from main."""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
