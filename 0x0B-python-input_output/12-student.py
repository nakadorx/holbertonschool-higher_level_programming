#!/usr/bin/python3
"""holbertontask"""


class Student:
    """holbertontask"""

    def __init__(self, first_name, last_name, age):
        """holberton"""
        self.first_name = first_name
        self.last_name = last_name
		self.age = age

    def to_json(self, attrs=None):
		"""holberton"""
        if type(attrs) is list and all([type(x) == str for x in attrs]):
            return {key: value for key, value in self.__dict__.items() if key in attrs}
        return self.__dict__
