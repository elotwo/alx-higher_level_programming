"""
This is my module base
The module base conatains a private class __nb_objects and a
public instance attribute id
"""
#!/usr/bin/python3
class Base:
    """
    class Base generate id on increment
    """
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None :
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

