#!/usr/bin/python3
"""holbertontask"""
import json


def save_to_json_file(my_obj, filename):
    """holbertontask"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
