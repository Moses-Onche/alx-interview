#!/usr/bin/python3
"""Defines a function that rotates a 2D matrix"""


def rotate_2d_matrix(matrix):
    """
       Rotates a 2D matrix 90 degrees clockwise
       Rotation is done in in-place and returns nothing.
       args:
          matrix
    """
    left = 0
    right = len(matrix) - 1

    while left < right:
        for a in range(right - left):
            top = left
            bottom = right
            # Rotate each outer element
            topLeft = matrix[top][left + a]
            matrix[top][left + a] = matrix[bottom - a][left]
            matrix[bottom - a][left] = matrix[bottom][right - a]
            matrix[bottom][right - a] = matrix[top + a][right]
            matrix[top + a][right] = topLeft
        right -= 1
        left += 1
