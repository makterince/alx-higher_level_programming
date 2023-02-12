#!/usr/bin/python3
""" creating a class Rectangle that inherits the base attributes """

from models.base import Base


class Rectangle(Base):
    """ class rectangle inherits from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor: initializes new instances
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x coordinate of the rectangle. Defaults to 0
            y (int, optional): The y coordinate of the rectangle. Defaults to 0
            id (int, optional): The ID of the rectangle.
            If not provided, the Base class will generate one.
        """
        
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """int: The width of the rectangle."""
        
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):

        """int: The x coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """int: The y coordinate of the rectangle."""

        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """ returns the height multiplied by width"""

        return (self.width * self.height)
    
    def display(self):
        """Prints the rectangle instance with #"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
            Returns a string representation of the rectangle instance
        """

        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        attrs = ["id", "width", "height", "x", "y"]
        if args and len(args) > 0:
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
