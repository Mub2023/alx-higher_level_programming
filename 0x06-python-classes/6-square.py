#!/usr/bin/python3
"""Defines class Square"""


class Square:
    """An new Square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initiaze the new class and its args.

        Args:
        size: The size of the square.
        position: The position of the square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Sets the current position of the square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(n, int) for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of square ."""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the square with #."""
        if self.__size == 0:
            print("")
            return

        for v in range(0, self.__position[1]):
            print("")
        for x in range(0, self.__size):
            for z in range(0, self.__position[0]):
                print(" ", end="")
            for y in range(self.__size):
                print("#", end="")
            print("")
