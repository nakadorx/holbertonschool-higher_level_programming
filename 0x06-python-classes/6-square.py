#!/usr/bin/python3
"""empty class Square
"""


class Square:
    """ Square Object
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Square Const """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Get Square """
        return self.__size

    @size.setter
    def size(self, value):
        """ Set Square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Get Position """
        return self.__position

    @position.setter
    def position(self, value):
        """ Set Position"""
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """  the square """
        return self.__size ** 2

    def my_print(self):
        """ Echo a # square"""
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(0, self.size):
                for k in range(self.position[0]):
                    print(" ", end='')
                for j in range(self.size):
                    print("#", end='')
                print()
