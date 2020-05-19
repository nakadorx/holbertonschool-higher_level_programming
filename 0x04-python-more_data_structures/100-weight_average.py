#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    x = 0
    n = 0
    for x in my_list:
        n += x[0] * x[1]
        x += x[1]
    return n / x
