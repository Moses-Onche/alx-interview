#!/usr/bin/python3
"""Defines a function that calculates the perimiter of a grid."""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.
    
    Args:
        grid (list of list of int): The grid representing the island.

    Returns:
        int: The perimeter of the island.
    """
    if not grid:
        return 0
    
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Add 4 sides for the land cell
                
                # Check left neighbor
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Subtract 2 for the shared side
                
                # Check top neighbor
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Subtract 2 for the shared side
                    
    return perimeter
