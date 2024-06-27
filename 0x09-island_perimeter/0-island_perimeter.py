#!/usr/bin/python3
"""
This module contains the function island_perimeter.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Args:
        grid (list of list of int): A list of list of integers
        representing the grid.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if i == 0 or grid[i-1][j] == 0:  # up
                    perimeter += 1
                if i == len(grid) - 1 or grid[i+1][j] == 0:  # down
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:  # left
                    perimeter += 1
                if j == len(grid[i]) - 1 or grid[i][j+1] == 0:  # right
                    perimeter += 1

    return perimeter
