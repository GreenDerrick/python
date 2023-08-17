#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = matrix.copy()
    final = []
    for row in new:
        row = list(map(lambda num: num ** 2, row))
        final.append(row)
    return final
