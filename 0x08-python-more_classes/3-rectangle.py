#!/usr/bin/python3
class Rectangle:
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
        a = self.width * self.height
        return a
    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return ' '
        else:
            c = str("#")
            print("{}".format(c))
            return 2 * (self.width + self.height)

