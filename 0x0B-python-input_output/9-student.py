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

    def to_json(self):
        return self.__dict__
