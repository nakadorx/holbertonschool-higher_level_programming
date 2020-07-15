#!/usr/bin/python3
"""holbertontask"""


def pascal_triangle(n):
    """holbertontask"""
    if n <= 0:
        return []
    result = []
    last = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            if i == 0 or j == 0 or i == j:
                row.append(1)
            else:
                row.append(last[j] + last[j - 1])
        last = row
        result.append(row)
    return result
