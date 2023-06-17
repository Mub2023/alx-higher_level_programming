#!/usr/bin/python3
"""the class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """the class that inherits from Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initilasize the Rectangle class with attributes
        Arg:
        Width (int): the width of Rectangle
        height (int): theheight of Rectangle
        x : is the x the of Rectangle
        y : is the y the of Rectangle
        id : fromthe Base class.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """return the width of the Rectangle"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """get/set the width of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """return the height of the Rectangle"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """get/set the height of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """return the x of the Rectangle"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """get/set the x  of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """return the y of the Rectangle"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """get/set the y  of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return the area of the Rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        print('\n' * self.y, end="")
        for y in range(0, self.height):
            print(' ' * self.x + '#' * self.width, end="")
            print("")

    def __str__(self):
        """return basic ifo about Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update the class Rectangle by adding the public method
        method that assigns attributes:
        *args:
        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4rd argument should be the x attribute
        5th argument should be the y attribute
        **kwargs:
        a dictionary: key/value (keyworded arguments)
        like id=55
        kwargs will beskipped if *args exists and is not empty"""
        if args and len(args) != 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key in ("id", "width", "height", "x", "y"):
                    setattr(self, key, value)

    def to_dictionary(self):
        """that returns the dictionary representation of a Rectangle"""
        return {
                'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width
                }
