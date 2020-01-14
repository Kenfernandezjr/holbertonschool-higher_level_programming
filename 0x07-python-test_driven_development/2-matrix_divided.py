#!/usr/bin/python3
def matrix_divided(matrix, div):


    if not isinstance(div, int):
        raise TypeError("div must be a number")

    if isinstance(div, float):
        raise TypeError("div must be a number")

    if div is 0:
        raise ZeroDivisionError("division by zero")

    for col in range(len(matrix)):

        if len(matrix[0]) is not len(matrix[col]):
            raise TypeError("Each row of the matrix must have the same size")
        for row in range(len(matrix[col])):

            if not isinstance(matrix[col][row], int):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

            if float(matrix[col][row]) is type:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

            return [[round(col/div, 2)for col in row]for row in matrix]
