#!/usr/bin/python3

from models.base import Base


class Rectangle(Base):
    print_symbol = "#"

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):

        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):

        if not isinstance(value, int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        return self.width * self.height

    def display(self):
        string = ""

        print("\n" * self.y, end="")
        for i in range(self.__height):
            print(" " * self.x, end="")
            for j in range(self.__width):
                print(self.print_symbol, end="")
            print()

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
            self.width, self.height)

    def update(self, *args):
        if len(args) is 0:
            if len(args) is 1:
                self.id = args[1]
            if len(args) is 2:
                self.width = args[1]
            if len(args) is 3:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
            if len(args) is 4:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
            if len(args) is 5:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]