#!/usr/bin/python3
# rectangle.py
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
        if self.width == 0 or self.height == 0:
            print("")
            return
        
        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def to_dictionary(self):
        """ returns the dictionary representation of the rectangle """

        return {'id': self.id, 'width': self.width, 'height': self.height
                'x': self.x, 'y':self.y}

    def __str__(self):
        """
            Returns a string representation of the rectangle instance
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                        self.x, self.y,
                                                        self.width, self.height)


    def update(self, *args, **kwargs):
    """Update the Rectangle.

    Args:
        *args (ints): New attribute values.
        - 1st argument represents id attribute
        - 2nd argument represents width attribute
        - 3rd argument represent height attribute
        - 4th argument represents x attribute
        - 5th argument represents y attribute
        **kwargs (dict): New key/value pairs of attributes.
    """
    if args and len(args) != 0:
        a = 0
        for arg in args:
            if a == 0:
                if arg is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                else:
                    self.id = arg
            elif a == 1:
                self.width = arg
            elif a == 2:
                self.height = arg
            elif a == 3:
                self.x = arg
            elif a == 4:
                self.y = arg
            a += 1
            
    elif kwargs and len(kwargs) != 0:
        for k, v in kwargs.items():
            if k == "id":
                if v is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                else:
                    self.id = v
            elif k == "width":
                self.width = v
            elif k == "height":
                self.height = v
            elif k == "x":
                self.x = v
            elif k == "y":
                self.y = v
