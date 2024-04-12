#!/usr/bin/python3
def matrix_divided(matrix, div):
    if isinstance(matrix, (int, float)):
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
    if isinstance(div, (int, float)):
        if div != 0:
            divided_result = []
            for x in matrix[n]:
                d = matrix[x] / div
                divided_result.append(d)
                x += 1
                print(divided_result)
        else:
             raise ZeroDivisionError("division by zero")
    else:
        raise TypeError("div must be a number")
