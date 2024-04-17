#!/usr/bin/python3
def inherits_from(obj, a_class):
    if obj == a_class:
        return True
    if obj in obj.__base__:
        if inherits_from(base_class, a_class):
            return True
    return False
