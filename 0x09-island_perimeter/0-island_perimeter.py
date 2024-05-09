#!/usr/bin/python3
"""perimeter island"""


def island_perimeter(grid):
    """island perimeter"""
    if not grid:
        return 0
    
    perimeter = 0
    rows, cols = len(grid), len(grid[0])
    
    # irections to check for adjacent cells
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # check its adjacent cells For each land cell
                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    # If the adjacent cell is out of bounds or water, add to the perimeter
                    if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] == 0:
                        perimeter += 1
    
    return perimeter
