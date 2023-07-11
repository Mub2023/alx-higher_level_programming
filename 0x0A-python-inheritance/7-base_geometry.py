#!/usr/bin/python3
"""defines a class BaseGeometry
"""


class BaseGeometry:
    """new BaseGeometry class
    includes area and integer_validator func !!!"""
    def area(self):
        """raises an Exception Error
        calculates and returns the area of the geometry object
        Raise:
        Exception: area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method:
        Args:
        name (str): name of basegeometry .
        value (int): the value of basegeometry always is int.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
