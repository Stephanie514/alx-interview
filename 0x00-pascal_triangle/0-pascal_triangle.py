#!/usr/bin/python3
""" function def pascal_triangle(n): that returns a
list of lists of integers"""


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for line in range(n):
        row = [1]  # First element in each row is always 1
        for i in range(1, line + 1):
            # Calculating the next element in the row using the previous row
            row.append(row[i - 1] * (line - i + 1) // i)
        triangle.append(row)

    return triangle
