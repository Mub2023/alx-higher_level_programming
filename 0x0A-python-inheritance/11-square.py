#!/usr/bin/python3
"""
a class Square that inherits
Rectangle (9-rectangle.py) i cant get my inhertance.
change it to square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherit
    Rectangle class and change to
    Square class"""
    def __init__(self, size):
        """change to Square
        Args:
        size (int): the size of the Square.
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """return, the square description:"""
        return("[Square] {:d}/{:d}".format(self.__size, self.__size))

    def area(self):
        """Return the area of the square"""
        return super().area()
