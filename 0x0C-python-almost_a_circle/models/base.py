"""
This is my module base
It is base class for rectangle and square class
class base generate id on each call
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

