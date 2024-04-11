#!/usr/bin/python3
def add_integer(a, b=98):
    c = int(a)
    d = float(b)
    if isinstance(a, (int,float)) or isinstance(a,(int, float)):
        return c + d
    else:
        raise TypeError("a must be an integer or b must be an integer")
