#!/usr/bin/python3
"""Defines a class Student."""

class Student:
    """student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student
        Args:
            first_name (str): The first name
            last_name (str): The last name
            age (int): The age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return a dictionary representation of the Student
        Args:
            attrs (list): (Optional) The attributes
        """
        if (type(attrs) == list and
                all(type(element) == str for element in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Reloads attributes of the Student.
        Args:
            json (dict): The key/value x and y
        """
        for x, y in json.items():
            setattr(self, x, y)
