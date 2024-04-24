"""
This is a module for rectangle
The class rectangle inherits from a class base module Base
The class rectangle checks for if the parameters given are of int data types
and also its attribute are of private. it's caculates areas of the rectangle by using the 
atrribute height and width
"""
#!/usr/bin/python3
from models.base import Base
class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    def height(self):
        return  self.__height
    def height(self, value):
        """
        method height is used to check if its value is of int data type, 
        other wise an error will be raise
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
    def width(self):
       return self.__width
    def width(self, value):
        """
        method width is used to check if its value is of int data type,
        other wise it will raise an error
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    def x(self):
       return  self.__x
    def x(self, value):
        """
        method(function) "x" is used to check if its value is of int data type,
        other wise it will raise an error
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
    def y(self):
       return self.__y
    def y(self, value):
        """
        method "y" is used to check if its value is of int data type,
        other wise it will raise an error
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer") 
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    def area(self):
        """
        The method(function) area is used to return the area of the rectangle
        """
        return self.__height * self.__width
    def display(self, *args):
        """
        The method(function) display is used to display the stucture of the
        rectangle with character "#"
        """
        if len(args) <= 2:
            for i in range(self.__height):
                for j in range(self.__width):
                    print("#",end = "")
                print()
        else:
            for _ in range(self.__x):
                for _ in range(self.__y):
                    print("#",end = "")
                print()
    def __str__(self):
        """
          A public method for string
        """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"
    def update(self, *args, **kwargs):
        """
        A public method that assign an arguiment to each attribute
        """
        if len(args) > 5:
            return
        attributes = ["id", "_Rectangle__width", "_Rectangle__height", "_Rectangle__x", "_Rectangle__y"]
        for arg, attribute in zip(args, attributes):
            setattr(self, attribute, arg)
        if args:
            return
        for key, value in kwargs.items():
            if key in attributes:
                setattr(self, key, value)

