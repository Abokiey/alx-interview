#!/usr/bin/python3

"""rotating a 2D matrix to 90 degrees"""

def rotate_2d_matrix(matrix):
    """rotate the matrix 90 degrees"""
    n = len(matrix)
    
    # Transpose the matrix
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row of the transposed matrix
    for i in range(n):
        matrix[i] = matrix[i][::-1]