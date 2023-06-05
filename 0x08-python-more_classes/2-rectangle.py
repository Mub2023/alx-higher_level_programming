#!/usr/bin/python3
""" class Rectangle that defines a rectangle with
Private instance attribute: width.
Private instance attribute: height."""


class Rectangle:
    """
    Rectangle with two private attribute width and height."""
    def __init__(self, width=0, height=0):
        """Initiaze the new class and its args.
        Args:
        width: The width of the Rectangle
        height: The height of the Rectangle."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieve width Private attribute"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """define width value arg"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve height Private attribute"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """define height value arg"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """retrieve the rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """retrieve the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))
