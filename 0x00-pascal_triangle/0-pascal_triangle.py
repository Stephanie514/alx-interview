#!/usr/bin/python3
""" function def pascal_triangle(n): that returns a
list of lists of integers"""


def pascal_triangle(n):
    """inner loop"""
    if n <= 0:
        return []

    triangle = []
    for line in range(n):
        row = [1]
        for i in range(1, line):
            # Calculate the next element in the row using the previous row
            row.append(triangle[line-1][i-1] + triangle[line-1][i])
        if line > 0:
            row.append(1)  # Last element in each row is always 1
        triangle.append(row)

    return triangle
