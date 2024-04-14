#!/usr/bin/python3
def matrix_divided(matrix, div):
    divided_results = []
    list(divided_results)
    if all(isinstance(x, (int, float))for x in matrix):
        n = len(matrix)
        c = 0
        while c <= n:
            a = len(matrix[c])
            c += 1
        b = a
        if a != b:
            raise TypeError("Each row of the matrix must have the same size")
        else:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if not isinstance(div, (int, float)):
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")
        for row in matrix:
            divided_row = []
            list(divided_row)
            for element in row:
                divide = element / div
                divided_row.append(divide)
            divided_results.append(divided_row)
    
    return divided_results
