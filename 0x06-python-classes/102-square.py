#!/usr/bin/python3
"""Defines class Square"""


class Square:
    """An new Square."""

    def __init__(self, size=0):
        """Initiaze the new class and its args.

        Args:
        size: The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Gets the size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets the current size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of square ."""
        return (self.__size * self.__size)

    def __equal__(self, oth):
        """Defines the == comparison"""
        return self.area() == oth.area()

    def __dontequal__(self, oth):
        """Defines the != comparison"""
        return self.area() != oth.area()

    def __bigger__(self, oth):
        """Defines the > comparison"""
        return self.area() > oth.area()

    def __less__(self, oth):
        """Defines the < comparison"""
        return self.area() < oth.area()

    def __biggerorequall__(self, oth):
        """Defines the >= comparison"""
        return self.area() >= oth.area()

    def __lessorequall__(self, oth):
        """Defines the <= comparison"""
        return self.area() <= oth.area()
