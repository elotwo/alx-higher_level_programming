#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = map(lambda row: list(map(lambda x: x*x, row)), matrix)
    squared_matrix_str = str([list(row) for row in squared_matrix])
    print(squared_matrix_str[1:-1])
