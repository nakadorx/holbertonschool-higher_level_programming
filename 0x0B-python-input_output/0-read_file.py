#!/usr/bin/python3
"""holbertontask"""


def read_file(filename=""):
    """holbertontask"""
    with open(filename, encoding="UTF-8") as f:
        string = f.read()
        print(string, end="")
