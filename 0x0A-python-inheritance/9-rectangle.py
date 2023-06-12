#!/usr/bin/python3
"""a class Rectangle that inherits
BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a class that represents a rectangle
    ####
    #  #
    ####
    """
    def __init__(self, width, height):
        """initializes a rectangle with
        width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """calculates and return the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """ return a str of the  representation of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
