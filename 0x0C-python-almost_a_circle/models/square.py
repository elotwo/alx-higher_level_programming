#!/usr/bin/python3
from models.rectangle import Rectangle
class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id,x,y,width,height)
        self.__width = size
        self.__height = size
        self.__x = x
        self.__y = y

