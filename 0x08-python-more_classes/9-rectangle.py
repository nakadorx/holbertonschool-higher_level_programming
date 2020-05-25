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
                x += str(self.print_symbol)
            x += '\n'
        return x[:-1]

    def __repr__(self):
        """ return repr """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ destroy object """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ big one """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ new one """
        return cls(size, size)
