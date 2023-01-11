#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""

def pascal_triangle(n):
    """Represent Pascal's Triangle of size n
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        x = triangles[-1]
        tmp = [1]
        for i in range(len(x) - 1):
            tmp.append(x[i] + x[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
