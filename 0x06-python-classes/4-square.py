#!/usr/bin/python3
class Square:
    """Square Class const"""

    def __init__(self, size=0):
        """init method"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """method 2 """
        return self.__size ** 2

    @property
    def size(self):
        """Return size for a square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Value for the object"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
