#!/usr/bin/python3
"""
print square
"""


def print_square(size):
    """
    prints square
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
        return

    if size < 0:
        raise ValueError('size must be >= 0')
        return

    for row in range(0, size):
        for col in range(0, size):
            print("#", end="")
        print()
