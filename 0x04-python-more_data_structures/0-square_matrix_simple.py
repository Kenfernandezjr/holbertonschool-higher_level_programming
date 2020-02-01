#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result[i][j] += pow(matrix[i][j], 2)

    for n in result:
        return(result)
