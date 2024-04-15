#!/usr/bin/python3
def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif  not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        if isinstance(a, float) and isinstance(b, float):
           a =  int(a)
           b = int(b)
    return a + b
