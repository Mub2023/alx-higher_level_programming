#!/usr/bin/python3
"""Defines the Square class"""


class Square:
    """An new Square """

    def __init__(self, size=0):
        """Initiaize a new Square.
        Args:
        size: Private instance attribute the size of Square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
