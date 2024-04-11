#!/usr/bin/python3
""" function def pascal_triangle(n): that returns a list of lists of integers"""

def pascal_triangle(n):
    """outer loop"""
    if n <= 0:
        return []
    value = []
    for line in range(1, n + 1):
        """inner loop"""
        j = 1
        row_series = []
        for i in range(1, line + 1):
            row_series.append(j)
            j = int(j * (line - i) / i)
        value.append(row_series)
    return value
