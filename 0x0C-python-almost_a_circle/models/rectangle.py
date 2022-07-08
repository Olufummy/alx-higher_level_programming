#!/usr/bin/python3
"""Module rectangle
"""


from models.base import Base


class Rectangle(Base):
        """Class rectangle"""

        def __init__(self, width, height, x=0, y=0, id=None):
                """construtor
                """

                super().__init__(id)
                if type(width) is not int:
                        raise TypeError("width must be an integer")
                elif width <= 0:
                        raise ValueError("width must be > 0")
                else:
                        self.__width = width

                if type(height) is not int:
                        raise TypeError("height must be an integer")
                elif height <= 0:
                        raise ValueError("height must be > 0")
                else:
                        self.__height = height

                if type(x) is not int:
                        raise TypeError("x must be an integer")
                elif x < 0:
                        raise ValueError("x must be >= 0")
                else:
                        self.__x = x

                if type(y) is not int:
                        raise TypeError("y must be an integer")
                elif y < 0:
                        raise ValueError("y must be >= 0")
                else:
                        self.__y = y

        @property
        def width(self):
                """"getter width"""
                return self.__width

        @width.setter
        def width(self, value):
                """"setter width"""
                if type(value) is not int:
                        raise TypeError("width must be an integer")
                elif value <= 0:
                        raise ValueError("width must be > 0")
                else:
                        self.__width = value

        @property
        def height(self):
                """"getter height"""
                return self.__height

        @height.setter
        def height(self, value):
                """"setter height"""
                if type(value) is not int:
                        raise TypeError("height must be an integer")
                elif value <= 0:
                        raise ValueError("height must be > 0")
                else:
                        self.__height = value

        @property
        def x(self):
                """getter x"""
                return self.__x

        @x.setter
        def x(self, value):
                """setter x """
                if type(value) is not int:
                        raise TypeError("x must be an integer")
                elif value < 0:
                        raise ValueError("x must be >= 0")
                else:
                        self.__x = value

        @property
        def y(self):
                """getter y"""
                return self.__y

        @y.setter
        def y(self, value):
                """setter y"""
                if type(value) is not int:
                        raise TypeError("y must be an integer")
                elif value < 0:
                        raise ValueError("y must be >= 0")
                else:
                        self.__y = value

        def area(self):
                """Area of a rectangle
                """
                return self.__width * self.__height

        def display(self):
                """Show a rectangle
                """
                Ry, Rx = "", ""

                for y in range(self.__y):
                        Ry += '\n'

                for x in range(self.__x):
                        Rx += ' '

                print(Ry, end="")
                for row in range(self.__height):
                        print(Rx + "#" * self.__width)

        def __str__(self):
                """overloand str"""
                return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                                self.__x,
                                                                self.__y,
                                                                self.__width,
                                                                self.__height)
                        )

        def update(self, *parameter, **kwargs):
                """Method update"""

                if len(parameter) > 0:
                        self.id = parameter[0]
                if len(parameter) > 1:
                        self.width = parameter[1]
                if len(parameter) > 2:
                        self.height = parameter[2]
                if len(parameter) > 3:
                        self.x = parameter[3]
                if len(parameter) > 4:
                        self.y = parameter[4]
                if parameter is None or len(parameter) == 0:
                        for key, value in kwargs.items():
                                if key == "width":
                                        self.width = value
                                elif key == "height":
                                        self.height = value
                                elif key == "x":
                                        self.x = value
                                elif key == "y":
                                        self.y = value
                                elif key == "id":
                                        self.id = value

        def to_dictionary(self):
                """Method to dictionary"""

                return {'id': self.id,
                        'width': self.__width,
                        'height': self.__height,
                        'x': self.__x,
                        'y': self.__y
                        }
