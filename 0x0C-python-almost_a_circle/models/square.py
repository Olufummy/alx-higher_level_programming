#!/usr/bin/python3
"""Module rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
        """Class Square"""

        def __init__(self, size, x=0, y=0, id=None):
                """construtor
                """

                super().__init__(size, size, x, y, id)

        def __str__(self):
                """overloand str"""
                return ("[Square] ({}) {}/{} - {}".format(
                        self.id, self.x, self.y, self.width))

        @property
        def size(self):
                """"getter size"""
                return self.width

        @size.setter
        def size(self, value):
                """setter size"""
                self.width = value
                self.height = value

        def update(self, *parameter, **kwargs):
                """Method update"""
                if len(parameter) > 0:
                        self.id = parameter[0]
                if len(parameter) > 1:
                        self.size = parameter[1]
                if len(parameter) > 2:
                        self.x = parameter[2]
                if len(parameter) > 3:
                        self.y = parameter[3]
                if parameter is None or len(parameter) == 0:
                        for key, value in kwargs.items():
                                if key == "size":
                                        self.size = value
                                elif key == "x":
                                        self.x = value
                                elif key == "y":
                                        self.y = value
                                elif key == "id":
                                        self.id = value

        def to_dictionary(self):
                """Method to dictionary"""
                return {'id': self.id,
                        'size': self.size,
                        'x': self.x,
                        'y': self.y
                        }
