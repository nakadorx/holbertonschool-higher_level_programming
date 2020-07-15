#!/usr/bin/python3
"""holbertontask"""


class Student:
    """holbertontask"""

    def __init__(self, first_name, last_name, age):
        """holbertontask"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """holbertontask"""
        if type(attrs) is list and all([type(x) == str for x in attrs]):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """holbertontask"""
        for k, v in json.items():
            self.__dict__[k] = v
