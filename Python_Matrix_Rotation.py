# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 13:26:44 2023

@author: Haryish Elangumaran
"""

def rotate_matrix(matrix, degrees):
    """
    Rotates a given matrix by the specified number of degrees.

    Args:
        matrix (list): The matrix to rotate.
        degrees (int): The number of degrees to rotate the matrix (must be a multiple of 90).

    Returns:
        The rotated matrix.
    """
    if degrees % 90 != 0:
        raise ValueError("Degrees must be a multiple of 90.")

    # Calculate the number of 90-degree rotations to perform.
    num_rotations = degrees // 90

    # Perform the rotations.
    for i in range(num_rotations):
        # Transpose the matrix (switch rows and columns).
        matrix = list(zip(*matrix))

        # Reverse each row to rotate 90 degrees clockwise or 270 degrees counter-clockwise.
        if degrees % 360 != 0:
            matrix = [list(reversed(row)) for row in matrix]

    return matrix


# Example matrix.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Menu loop.
while True:
    print("Current matrix:")
    for row in matrix:
        print(row)

    print("1. Rotate 90 degrees clockwise")
    print("2. Rotate 180 degrees")
    print("3. Rotate 270 degrees counter-clockwise")
    print("4. Rotate 360 degrees")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))

    if choice == 1:
        matrix = rotate_matrix(matrix, 90)
    elif choice == 2:
        matrix = rotate_matrix(matrix, 180)
    elif choice == 3:
        matrix = rotate_matrix(matrix, 270)
    elif choice == 4:
        matrix = rotate_matrix(matrix, 360)
    elif choice == 5:
        break
    else:
        print("Invalid choice.")
