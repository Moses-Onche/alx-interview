#!/usr/bin/python3
"""Pascal Triangle"""
from math import factorial


def pascal_triangle(n):
    """Pascal's triangle
    Args:
      n (int): The number of rows of the triangle
    Returns:
      List of lists of integers representing the Pascal’s triangle
    """
    triangle = []
    if n <= 0:
        return triangle
    else:
        for a in range(0, n):
            i = 1
            row = []
            for b in range(0, a+1):
                i = factorial(a)/(factorial(a - b) * factorial(b))
                row.append(int(i))
            triangle.append(row)

    return triangle
