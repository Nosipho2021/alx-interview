#!/usr/bin/python3
"""
Contains function that calculates the perimeter of an island described in a grid
"""


def island_perimeter(grid):
    """
    param grid: List of lists of integers (0 represents water, 1 represents land).
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with a perimeter of 4 for each land cell
                perimeter += 4

                # Check if the land cell has a neighbor to the right (shared side)
                if j < cols - 1 and grid[i][j + 1] == 1:
                    perimeter -= 2

                # Check if the land cell has a neighbor below (shared side)
                if i < rows - 1 and grid[i + 1][j] == 1:
                    perimeter -= 2

    return perimeter
