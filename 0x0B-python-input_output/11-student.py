#!/usr/bin/python3
"""holbertontask"""


class Student:
    """holbertontask"""

    def __init__(self, first_name, last_name, age):
        """holberton"""
		self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def to_json(self):
        """holbertontask"""
        return self.__dict__
