#!/usr/bin/python3
"""holbertontask"""


def pascal_triangle(n):
    """holbertontask"""
    if n <= 0:
        return []
    res = []
    lt = []
    for i in range(n):
        x = []
        for j in range(i + 1):
            if j == 0 or i == 0 or j == i:
                x.append(1)
            else:
                x.append(lt[j] + lt[j - 1])
        lt = x
        res.append(x)
    return res
