#!/usr/bin/python3
"""a medual Student that defines a student by:
    first_name
    last_name
    age
"""


class Student:
    """class of the info about Student"""
    def __init__(self, first_name, last_name, age):
        """initialize the Student
        class with Public instance attributes:
        first_name (str): the first name of student
        last_name (str): the last name of student
        age (int): the age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """that retrieves a dictionary representation of a Student
        Args:
            attrs: only attribute names of the students
        return: a dictionary representation of a Student"""
        if (type(attrs) == list and
                all(type(e) == str for e in attrs)):
            return {x: getattr(self, x) for x in attrs if hasattr(self, x)}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance
        Args:
            json (dict): the dictionary of the student."""
        for w, z in json.items():
            setattr(self, w, z)
