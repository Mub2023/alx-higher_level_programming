#!/usr/bin/python3
"""the class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """the class Square that inherits from Rectangle
    and make it Square !!!
    """
    def __init__(self, size, x=0, y=0, id=None):
        """initialize the Square attributes from Rectangle class
        Args:
        size (int): the size of the square
        x (int): the x of the square
        y (int): the y of the square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """print the Suare attributes id, x, y, size"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """set/get of the size attributes"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter from the rectangle"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the class Square by adding the public
        method that assigns attributes:
        *args:
            1st argument should be the id attribute
            2nd argument should be the size attribute
            3rd argument should be the x attribute
            4th argument should be the y attribute
        **kwargs:
            a dictionary: key/value (keyworded arguments)
            like id=55
            kwargs will beskipped if *args exists and is not empty
        """
        if args and len(args) != 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key in ("id", "size", "x", "y"):
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {"id": self.id, "x": self.x, "size": self.size, "y": self.y}
