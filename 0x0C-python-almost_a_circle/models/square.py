#!/usr/bin/python3
""" Square class/Module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """
    def __init__(self, size, x=0, y=0, id=None):
        """ init with super inheritance """
        super().__init__(size, size, x, y, id)
        self.width = size
        self.height = size
        self.x = x
        self.y = y

    def __str__(self):
        """ str for Square """
        return("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size))

    @property
    def size(self):
        """ getter for size """
        return self.width

    @size.setter
    def size(self, value):
        """ setter for size """
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value
