#!/usr/bin/python3
from models.rectangle import Rectangle

""" square class that inherits from rectangle """


class Square(Rectangle):
    """ initialize """

    def __init__(self, size, x=0, y=0, id=None):
        """The constructor for the Square class.
        
            Calls the super class constructor with id, x, y, width and height.
            The width and height are assigned to the value of size.
            
            Args:
                size (int): The size of the square.
                x (int, optional): The x-coordinate of the square.
                Defaults to 0.
                y (int, optional): The y-coordinate of the square.
                Defaults to 0.
                id (int, optional): The id of the square.
                Defaults to None.
        """

        super().__init__(id, x, y, size, size)

        @property
        def size(self):
            """ returns the size"""
            
            return self.width
        
        @size.setter
        def size(self, value):
            """ sets the size of square"""
            
            self.width = value
            self.height = value

        def update(self, *args, **kwargs):
            """ updates to the attributes of the square"""

            if args:
                for i, arg in enumerate(args):
                    if i == 0:
                        self.id = arg
                    if i == 1:
                        self.size = arg
                    if i == 2:
                        self.x = arg
                    if i == 3:
                        self.y = arg
            else:
                for key, value in kwargs.items():
                    setattr(self, key, value)
        def to_dictionary(self):
            """Returns the dictionary representation of the square.
            
            Returns:
                dict: A dictionary with the following keys:
                id: The id of the square.
                size: The size of the square.
                x: The x-coordinate of the square.
                y: The y-coordinate of the square.
            """
            return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        
        def __str__(self):
            """Returns a string representation of the square.
            
            Returns:
                str: A string in the format [Square] (<id>) <x>/<y> - <size>.
            """
            return ("[Square] ({}) {}/{} - {}".format
                    (self.id, self.x, self.y, self.width))
