#!/usr/bin/python3
"""holbertontask"""


class Student:
    """holbertontask"""

    def __init__(self, first_name, last_name, age):
        """Initailazer"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """holbertontask"""
        if type(attrs) is list and all([type(x) == str for x in attrs]):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
