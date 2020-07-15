#!/usr/bin/python3
"""ReadLines module"""


def read_lines(filename="", nb_lines=0):
    """holbertontask"""
    with open(filename, encoding="utf-8") as f:
        if nb_lines <= 0:
            print(f.read(), end="")
        for i in range(nb_lines):
            print(f.readline(), end="")
