#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    d = {}
    for key, value in a_dictionary.items():
        d[key] = a_dictionary[key] * 2
    return d
