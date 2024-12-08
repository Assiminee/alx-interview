#!/usr/bin/python3
"""
Island perimeter module
"""


def island_perimeter(grid):
    """Calculates perimeter of an island (2D array)"""
    rows = len(grid)
    cols = len(grid[0])
    per = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                per += 4
                if i > 0 and grid[i-1][j] == 1:
                    per -= 2
                if j > 0 and grid[i][j-1] == 1:
                    per -= 2

    return per
