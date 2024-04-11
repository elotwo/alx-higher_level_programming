#!/usr/bin/python3
def add_integer(a, b=98):
    if isinstance(a,(int, float)):
        int(a)
    else:
        raise TypeError("a must be an integer")
    if isinstance(b,(int, float)) :
        int(b)
    else:
        raise TypeError("b must be an integer")
    return a + b
