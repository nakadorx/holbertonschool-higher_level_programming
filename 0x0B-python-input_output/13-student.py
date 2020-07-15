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
        dictionary = {}
        if type(attrs) is list:
            for i in attrs:
                if hasattr(self, i):
                    dictionary[i] = self.__dict__[i]
            return dictionary
        return self.__dict__

    def reload_from_json(self, json):
        for k, v in json.items():
            if hasattr(self, k):
                self.__dict__[k] = v
