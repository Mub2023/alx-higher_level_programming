#!/usr/bin/python3
"""
a class Square that inherits
Rectangle (9-rectangle.py) i cant get my inhertance.
"""
Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """Square class that inherit
    Rectangle class and change to
    Square class ^_^"""
    def __init__(self, size):
        """change to
        Square

        Args:
        size (int): the size of the Square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """ return, the square description:"""
        return("[Square] {}/{}".format(self.__size, self.__size))

    def area(self):
        """Return the area of the square"""
        return super().area()
