#!/usr/bin/python3
"""
function to add a + fixed b 98
"""


def add_integer(a, b=98):
    """
    add a +b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
        return
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
        return
    return int(a) + int(b)
