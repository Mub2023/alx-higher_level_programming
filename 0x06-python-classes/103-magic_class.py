#!/usr/bin/python3
"""Define a MagicClass that does exactly the same as python bytecode"""

import math

class MagicClass:
    """initilazile the magic magic magic class"""

    def __init__(self, radius=0):
        """initilazile the magic magic class

        Arg:
        radius: The radius of the new magic class
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._radius = radius

    def area(self):
        """Return the area of the magic magic class"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return The circumference of the magic magic class"""
        return (2 * math.pi * self.__radius)
