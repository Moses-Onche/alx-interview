from math import factorial


def pascal_triangle(n):
    """Defines a class that uses n to create a Pascal Triangle with lists."""
    triangle = []
    if n <= 0:
        return []
    else:
        for a in range(0, n):
            i = 1
            row = []
            for b in range(0, a+1):
                i = factorial(a)/(factorial(a - b) * factorial(b))
                row.append(int(i))
            triangle.append(row)
    return triangle
