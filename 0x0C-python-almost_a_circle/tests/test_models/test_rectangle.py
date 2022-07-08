#!/usr/bin/python3

from models.rectangle import Rectangle
import unittest


class TestRectangleId(unittest.TestCase):

        def test_Rectangle_id_1(self):

                obj1 = Rectangle(width=6, height=54)
                self.assertEqual(obj1.id, 3)

        def test_Rectangle_id_2(self):

                obj2 = Rectangle(height=2, width=2)
                self.assertEqual(obj2.id, 4)

        def test_Rectangle_id_negative(self):

                obj2 = Rectangle(height=2, width=2, id=-3)
                self.assertEqual(obj2.id, -3)

        def test_Rectangle_id_any(self):

                obj = Rectangle(2, 4, 0, 0, 15)
                self.assertEqual(obj.id, 15)


class TestRectangleValidation(unittest.TestCase):

        def test_not_argument(self):

                with self.assertRaises(TypeError):
                        obj = Rectangle()

        def test_more_than_five_argument(self):

                with self.assertRaises(TypeError):
                        obj = Rectangle(3, 4, 3, 4, 4, 5)

        def test_width_type_error(self):

                with self.assertRaises(TypeError):
                        objE = Rectangle("hola", 3)

        def test_height_type_error(self):

                with self.assertRaises(TypeError):
                        objE_1 = Rectangle(6, "betty")

        def test_x_type_error(self):

                with self.assertRaises(TypeError):
                        objE_1 = Rectangle(6, 7, "Miguel")

        def test_y_type_error(self):

                with self.assertRaises(TypeError):
                        objE_1 = Rectangle(6, 7, 2, "what")

        def test_width_value_error(self):

                with self.assertRaises(ValueError):
                        objE_1 = Rectangle(-6, 7)

                with self.assertRaises(ValueError):
                        objE_1 = Rectangle(0, 7)

        def test_height_value_error(self):

                with self.assertRaises(ValueError):
                        objE_1 = Rectangle(1, -1)

                with self.assertRaises(ValueError):
                        objE_1 = Rectangle(1, 0)

        def test_x_value_error(self):

                with self.assertRaises(ValueError):
                        objE_1 = Rectangle(1, 1, -4)

        def test_y_value_error(self):

                with self.assertRaises(ValueError):
                        objE_1 = Rectangle(1, 1, 0, -1)

        def setUp(self):

                self.rec = Rectangle(5, 6, id=100)

        def test_width(self):

                self.assertEqual(self.rec.width, 5)

        def test_height(self):

                self.assertEqual(self.rec.height, 6)

        def test_x(self):

                self.assertEqual(self.rec.x, 0)

        def test_y(self):

                self.assertEqual(self.rec.y, 0)

        def test_id(self):

                self.assertEqual(self.rec.id, 100)

        def test_set_get_width(self):

                self.rec.width = 12
                self.assertEqual(self.rec.width, 12)
                with self.assertRaises(ValueError):
                        self.rec.width = 0
                with self.assertRaises(TypeError):
                        self.rec.width = "DILL"

        def test_set_get_height(self):

                self.rec.height = 15
                self.assertEqual(self.rec.height, 15)
                with self.assertRaises(ValueError):
                        self.rec.height = 0
                with self.assertRaises(TypeError):
                        self.rec.height = "DILL"

        def test_set_get_x(self):

                self.rec.x = 8
                self.assertEqual(self.rec.x, 8)
                with self.assertRaises(ValueError):
                        self.rec.x = -1
                with self.assertRaises(TypeError):
                        self.rec.x = "DILL"

        def test_set_get_y(self):

                self.rec.y = 6
                self.assertEqual(self.rec.y, 6)
                with self.assertRaises(ValueError):
                        self.rec.y = -12
                with self.assertRaises(TypeError):
                        self.rec.y = "DILL"


class TestRectangleMethods(unittest.TestCase):

        def setUp(self):

                self.rec2 = Rectangle(5, 6, 1, 3, id=101)

        def test_method_area(self):

                self.assertEqual(self.rec2.area(), 30)

        def test_method_desplay(self):

                self.assertIsNone(self.rec2.display())

        def test_method__str__(self):

                self.assertEqual(
                        self.rec2.__str__(), "[Rectangle] (101) 1/3 - 5/6")

        def test_method_update(self):

                self.rec2.update(101, 7, 6, 1, 2)

                self.assertEqual(self.rec2.id, 101)
                self.assertEqual(self.rec2.width, 7)
                self.assertEqual(self.rec2.height, 6)
                self.assertEqual(self.rec2.x, 1)
                self.assertEqual(self.rec2.y, 2)

                with self.assertRaises(TypeError):
                        self.rec2.update(101, "width", 3, 5, 6)

                with self.assertRaises(ValueError):
                        self.rec2.update(101, 4, 3, -5, 6)

        def test_method_update_v2(self):

                self.rec2.update(height=17, width=4, y=1, x=1, id=50)

                self.assertEqual(self.rec2.id, 50)
                self.assertEqual(self.rec2.width, 4)
                self.assertEqual(self.rec2.height, 17)
                self.assertEqual(self.rec2.x, 1)
                self.assertEqual(self.rec2.y, 1)

                with self.assertRaises(TypeError):
                        self.rec2.update(width="width")

                with self.assertRaises(ValueError):
                        self.rec2.update(width=0)

        def test_method_to_dict(self):

                self.assertEqual(type(self.rec2.to_dictionary()), dict)

        def test_create(self):

                r1_dictionary = self.rec2.to_dictionary()
                r2 = Rectangle.create(**r1_dictionary)
                self.assertIsInstance(r2, Rectangle)

if __name__ == '__main__':
        unittest.main()
