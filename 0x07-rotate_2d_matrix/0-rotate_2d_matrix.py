#!/usr/bin/python3
"""
Module for 2D Matrix rotation.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in-place.
    """

    matrix.reverse()


    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)): 
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
