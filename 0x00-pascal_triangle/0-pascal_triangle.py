#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(n):
    """
    Pascal's triangle
    Args:
      n (int): The number of rows of the triangle
    Returns:
      List of lists of integers representing the Pascal’s triangle
    """
    triangle = []
    if n == 0:
        return triangle
    for a in range(n):
        triangle.append([])
        triangle[a].append(1)
        if (a > 0):
            for b in range(1, a):
                triangle[a].append(triangle[a - 1][b - 1] + triangle[a - 1][b])
            triangle[a].append(1)
    return triangle
