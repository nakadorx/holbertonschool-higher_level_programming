#!/usr/bin/python3
import math


class MagicClass:

    """ search aria"""
    def area(self):
        return math.pi * (self.__radius ** 2)

    """ search 1 """
    def circumference(self):
        return self.__radius * 2 * math.pi

    """save data"""
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not float and type(radius) is not int:
            raise TypeError('radius must be a number')
        self.__radius = radius
