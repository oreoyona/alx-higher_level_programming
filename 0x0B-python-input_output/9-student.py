#!/usr/bin/python3
"""Defines the class Student."""


class Student:
    """xlass Student"""

    def __init__(self, first_name, last_name, age):
        """Creates a new Student.
        Args:
            first_name (str): The first name
            last_name (str): The last name
            age (int): The age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns a dictionary of the Student."""
        return self.__dict__
