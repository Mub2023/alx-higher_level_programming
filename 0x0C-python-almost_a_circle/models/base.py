#!/usr/bin/python3
"""the first class Base"""


class Base:
    """This class will be the “base”
    of all other classes in this project."""
    __nb_objects = 0

    def __init__(self, id=None):
        """the initiaizle of the class with:
        Args:
        id (int): is an integer """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
