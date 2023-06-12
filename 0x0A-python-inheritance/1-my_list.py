#!/usr/bin/python3
"""a class MyList that inherits from list"""


class MyList(list):
    """a class MyList that inherits from list"""
    def __init__(self):
        """initializes the class"""
        super().__init__()

    def print_sorted(self):
        """ that prints the list, but sorted (ascending sort)"""
        print(sorted(self))
