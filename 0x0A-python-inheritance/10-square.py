#!/usr/bin/python3
"""
a class Square that inherits
Rectangle (9-rectangle.py) i cant get my inhertance.
"""
Rectangle = __import__('9-rectangle').Rectangle


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
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """calaulates thearea of the Square"""
        return self.__size * self.__size
