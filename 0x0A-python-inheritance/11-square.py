#!/usr/bin/python3
"""
7-base_geometry.py Module
"""


class BaseGeometry:
    """
    class
    """
    def area(self):
        """
        public instance method
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer validator
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

            """
            Subclass created
            """


class Rectangle(BaseGeometry):
    """
    inherit class
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)

    def area(self):
        """
        area of the Rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Printing str of width and height
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """
    inherit class
    """
    def __init__(self, size):
        self.__size = size
        super().integer_validator("size", size)
        super().__init__(self.__size, self.__size)

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
