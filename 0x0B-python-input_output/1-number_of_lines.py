#!/usr/bin/python3
"""holbertontaske"""


def number_of_lines(filename=""):
    """holbertontask"""
    with open(filename, encoding="utf-8") as f:
        number = 0
        for line in f:
            number += 1

    return number
