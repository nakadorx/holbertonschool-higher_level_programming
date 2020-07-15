#!/usr/bin/python3
"""holbertontask"""


def append_after(filename="", search_string="", new_string=""):
    """holbertontask"""
    with open(filename, "r+", encoding="utf-8") as f:
        string = ""
        for line in f:
            string += line
            if search_string in line:
                string += new_string
        f.seek(0)
        f.write(string)
