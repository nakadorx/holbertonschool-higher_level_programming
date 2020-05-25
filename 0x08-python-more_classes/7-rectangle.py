#!/usr/bin/python3
"""
calss making for rectangle
"""


class Rectangle:
    """ rectangle class """
    number_of_instances = 0

    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ cosntractor """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def perimeter(self):
        """ perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def area(self):
        """ aria for rectngle """
        return self.__width * self.__height

    def __str__(self):
        """ str """
        x = ""
        if self.__height == 0 or self.__width == 0 :
            return x
        for i in range(self.__height):
            for j in range(self.__width):
                x += "#"
            x += '\n'
        return x[:-1]

    def __repr__(self):
        """ return repr """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ destroy object """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")