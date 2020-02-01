#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matr = []
    for n in matrix:
        new_matr.append(list(map(lambda x: x ** 2, n)))
    return new_matr
