#!/usr/bin/python3
"""holbertontaske"""


def number_of_lines(filename=""):
    """holbertontask"""
    with open(filename, encoding="utf-8") as f:
        x = 0
        for line in f:
            x += 1

    return x
