#!/usr/bin/python3
"""Module to generate Pascal's Triangle"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal’s triangle of n rows.

    Args:
        n (int): The number of rows in Pascal's Triangle.

    Returns:
        List[List[int]]: Pascal's Triangle represented as a list of lists.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        previous = triangle[-1]
        current = [1]
        for i in range(len(previous) - 1):
            current.append(previous[i] + previous[i + 1])
        current.append(1)
        triangle.append(current)
    return triangle
