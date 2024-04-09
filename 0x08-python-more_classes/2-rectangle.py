#!/usr/bin/python3
class rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    def width(self):
        return self.__width
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer" )
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    def height(self):
        return self.__height
    def height(self, value):
        if not isinstance (value, int):
            raise TypeError("height must be an inter")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value 
    def area(self):


