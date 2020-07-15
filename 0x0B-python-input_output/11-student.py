#!/usr/bin/python3
"""holbertontask"""


class Student:
    """holbertontask
	    Attributes:
        first_name (str): holberton
        last_name (str): holberton
        age (int): holberton"""

    def __init__(self, first_name, last_name, age):
        """holberton"""
        self.first_name = first_name
        self.last_name = last_name
		self.age = age

    def to_json(self):
        """holbertontask"""
        return self.__dict__
