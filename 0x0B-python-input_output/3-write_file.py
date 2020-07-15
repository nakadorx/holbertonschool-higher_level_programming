#!/usr/bin/python3
"""holbertontask"""


def write_file(filename="", text=""):
    """holbertontask"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
