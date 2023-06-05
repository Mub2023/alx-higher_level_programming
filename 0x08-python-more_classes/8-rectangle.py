#!/usr/bin/python3
""" class Rectangle that defines a rectangle with
Private instance attribute: width.
Private instance attribute: height."""


class Rectangle:
    """
    Rectangle with two private attribute width and height."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initiaze the new class and its args.
        Args:
        width: The width of the Rectangle
        height: The height of the Rectangle."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """return the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        r = ""
        for x in range(0, self.__height):
            for e in range(0, self.__width):
                r += str(self.print_symbol)
            r += "\n"
        r = r[:-1]
        return r

    def __repr__(self):
        """return a string representation of the rectangle"""
        re = "Rectangle({}, {})".format(self.__width, self.__height)
        return re

    def __del__(self):
        """delete the rectangle with msg Bye rectangle..."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def __gt__(self, other):
        """check if the rectangle 1 is greater than rectangle 2"""
        return self.area() > other.area()

    def __lt__(self, other):
        """check if the rectangle 2 is greater than rectangle 1"""
        return self.area() < other.area()

    def __eq__(self, other):
        """check if the rectangle 1 is equal rectangle 2"""
        return self.area() == other.area()

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1 == rect_2:
            return rect_1
        if rect_1 > rect_2:
            return rect_1
        else:
            return rect_2
