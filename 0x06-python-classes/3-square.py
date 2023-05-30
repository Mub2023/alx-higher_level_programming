#!/usr/bin/python3
"""Defines a square class thats all."""


class Square:
    """An new Square."""

    def __init__(self, size=0):
        """Initiaize the new Sqare and its args

        Args:
        size: Private instance attribute.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area."""
        return(self.__size * self.__size)
