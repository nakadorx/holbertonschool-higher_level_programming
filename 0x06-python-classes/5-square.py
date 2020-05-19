#!/usr/bin/python3
class Square:
    """ Square Object """
    def __init__(self, size=0):
        """ Square Const """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Get Square """
        return self.__size ** 2

    @property
    def size(self):
        """ Get Size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Set Size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """ Echo Square """
        if not self.__size:
            print()
        else:
            for x in range(self.__size):
                for y in range(self.__size):
                    print("#", end='')
                print()
