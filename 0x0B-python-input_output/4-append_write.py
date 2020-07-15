#!/usr/bin/python3
"""holbertontask"""


def append_write(filename="", text=""):
    """holbertontask"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
