#!/usr/bin/python3

from models.rectangle import Rectangle
from models.square import Square
import unittest


class TestSquareId(unittest.TestCase):

        def test_Square_id_1(self):

                obj1 = Square(5)
                self.assertEqual(obj1.id, 16)

        def test_Square_id_2(self):

                obj2 = Square(2)
                self.assertEqual(obj2.id, 17)

        def test_Square_id_negative(self):

                obj2 = Square(8, id=-5)
                self.assertEqual(obj2.id, -5)

        def test_Square_id_any(self):

                obj = Square(7, 0, 0, 90)
                self.assertEqual(obj.id, 90)

        def test_subclass(self):

                self.assertTrue(issubclass(Square, Rectangle))


class TestSquareValidation(unittest.TestCase):
        def test_not_argument_Square(self):

                with self.assertRaises(TypeError):
                        obj = Square()

        def test_more_than_five_argument(self):

                with self.assertRaises(TypeError):
                        obj = Square(3, 4, 3, 4, 4, 5)

        def test_size_type_error(self):

                with self.assertRaises(TypeError):
                        objE = Square("hola", 3)

        def test_x_type_error(self):

                with self.assertRaises(TypeError):
                        objE_1 = Square(6, "Miguel")

        def test_y_type_error(self):

                with self.assertRaises(TypeError):
                        objE_1 = Square(6, 7, "what")

        def test_size_value_error(self):

                with self.assertRaises(ValueError):
                        objE_1 = Square(-6)

                with self.assertRaises(ValueError):
                        objE_1 = Square(0)

        def test_x_value_error(self):

                with self.assertRaises(ValueError):
                        objE_1 = Square(1, -1, 4)

        def test_y_value_error(self):

                with self.assertRaises(ValueError):
                        objE_1 = Square(1, 1, -1)

        def setUp(self):

                self.squ = Square(5, 6, id=100)

        def test_size(self):

                self.assertEqual(self.squ.size, 5)

        def test_x(self):

                self.assertEqual(self.squ.x, 6)

        def test_y(self):

                self.assertEqual(self.squ.y, 0)

        def test_id(self):

                self.assertEqual(self.squ.id, 100)

        def test_set_get_size(self):

                self.squ.size = 12
                self.assertEqual(self.squ.size, 12)
                with self.assertRaises(ValueError):
                        self.squ.size = -1
                with self.assertRaises(TypeError):
                        self.squ.size = "DILL"

        def test_set_get_x(self):

                self.squ.x = 8
                self.assertEqual(self.squ.x, 8)
                with self.assertRaises(ValueError):
                        self.squ.x = -1
                with self.assertRaises(TypeError):
                        self.squ.x = "DILL"

        def test_set_get_y(self):

                self.squ.y = 6
                self.assertEqual(self.squ.y, 6)
                with self.assertRaises(ValueError):
                        self.squ.y = -12
                with self.assertRaises(TypeError):
                        self.squ.y = "DILL"


class TestSquareMethods(unittest.TestCase):

        def setUp(self):

                self.squ2 = Square(5, 6, 1, id=101)

        def test_method_area(self):

                self.assertEqual(self.squ2.area(), 25)

        def test_method_desplay(self):

                self.assertIsNone(self.squ2.display())

        def test_method__str__(self):

                self.assertEqual(self.squ2.__str__(), "[Square] (101) 6/1 - 5")

        def test_method_update(self):

                self.squ2.update(101, 7, 1, 2)

                self.assertEqual(self.squ2.id, 101)
                self.assertEqual(self.squ2.size, 7)
                self.assertEqual(self.squ2.x, 1)
                self.assertEqual(self.squ2.y, 2)

                with self.assertRaises(TypeError):
                        self.squ2.update(101, "size", 3, 6)

                with self.assertRaises(ValueError):
                        self.squ2.update(101, 4, -5, 6)

        def test_method_update_v2(self):

                self.squ2.update(size=17, y=1, x=1, id=50)

                self.assertEqual(self.squ2.id, 50)
                self.assertEqual(self.squ2.size, 17)
                self.assertEqual(self.squ2.x, 1)
                self.assertEqual(self.squ2.y, 1)

                with self.assertRaises(TypeError):
                        self.squ2.update(size="size")

                with self.assertRaises(ValueError):
                        self.squ2.update(size=0)

        def test_method_to_dict(self):

                self.assertEqual(type(self.squ2.to_dictionary()), dict)

        def test_create(self):

                r1_dictionary = self.squ2.to_dictionary()
                r2 = Rectangle.create(**r1_dictionary)
                self.assertIsInstance(r2, Rectangle)

if __name__ == '__main__':
        unittest.main()
