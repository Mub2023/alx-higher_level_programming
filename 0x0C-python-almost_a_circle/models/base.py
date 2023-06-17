#!/usr/bin/python3
"""the first class Base"""
import json
import csv
import turtle


class Base:
    """This class will be the “base”
    of all other classes in this project."""
    __nb_objects = 0

    def __init__(self, id=None):
        """the initiaizle of the class with:
        Args:
        id (int): is an integer """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """that returns the JSON string
        representation of list_dictionaries
        Arg:
            list_dictionaries:is a list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """that writes the JSON string
        representation of list_objs to a file
        Args:
            list_objs:is a list of instances who inherits of Base
            cls: <Class name>.json - example: Rectangle.json
        """
        empty_ls = []
        if list_objs is not None and len(list_objs) > 0:
            for ob in list_objs:
                empty_ls.append(ob.to_dictionary())
        with open(cls.__name__ + ".json", "w") as w:
            w.write(Base.to_json_string(empty_ls))

    @staticmethod
    def from_json_string(json_string):
        """that returns the list of the
        JSON string representation json_string
        Arg:
            json_string: is a string representing a list of dictionaries"""
        if json_string is None and len(json_string) > 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        Args:
        **dictionary can be thought of as a double pointer to a dictionary
        """
        if cls.__name__ == "Rectangle":
            new_di = cls(1, 1)
        else:
            new_di = cls(1)
        new_di.update(**dictionary)
        return new_di

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances"""
        try:
            with open(cls.__name__ + ".json", 'r') as re:
                json_f = Base.from_json_string(re.read())
                return [cls.create(**dt) for dt in json_f]
        except IOError:
            return []

    @classmethod
    def load_from_file_csv(cls):
        """that returns a list of instances:"""
        fil = []
        try:
            with open(cls.__name__ + ".csv", 'r') as fils:
                if cls.__name__ == "Rectangle":
                    fil = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == "Square":
                    fil = ['id', 'size', 'x', 'y']
                reading = csv.DictReader(fils, fieldnames=fil)
                dc = [dict([z, int(a)] for z, a in ls.items())
                      for ls in reading]
                return [cls.create(**dt) for dt in dc]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """that serializes and deserializes in CSV"""
        fil = []
        with open(cls.__name__ + ".csv", 'w') as fils:
            if list_objs is None or len(list_objs) <= 0:
                fils.write('[]')
            else:
                if cls.__name__ == "Rectangle":
                    fil = ['id', 'width', 'height', 'x', 'y']
                elif cls.__name__ == "Square":
                    fil = ['id', 'size', 'x', 'y']
                writing = csv.DictWriter(fils, fieldnames=fil)
                for ob in list_objs:
                    writing.writerow(ob.to_dictionary())

    @staticmethod
    def draw(list_rectangles, list_squares):
        """that opens a window and draws all the Rectangles and Squares
        Args:
            list_rectangles (list): a list of the rectangle instances
            list_squares (list): a list of the Square instances
        """
        mc = turtle.Turtle()
        mc.screen.bgcolor('#000000')
        mc.shape('turtle')
        mc.color('#ffffff')
        mc.penup()
        mc.goto(-200, 200)
        for re in list_rectangles:
            mc.goto(mc.xcor() + (re.width + 20), mc.ycor() - (re.height + 20))
            mc.up()
            mc.down()
            for z in range(2):
                mc.forward(re.width)
                mc.left(90)
                mc.forward(re.height)
                mc.left(90)
            mc.penup()
        mc.goto(-200, 200)
        for si in list_squares:
            mc.goto(mc.xcor() + (si.width + 20), mc.ycor() - (si.height + 20))
            mc.up()
            mc.down()
            for z in range(2):
                mc.forward(si.width)
                mc.left(90)
                mc.forward(si.height)
                mc.left(90)
            mc.penup()
        mc.screen().exitonclick()
