#!/usr/bin/python3

from models.base import Base
import unittest


class TestBase(unittest.TestCase):

        def test_id_1(self):

                obj1 = Base()
                self.assertEqual(obj1.id, 1)

        def test_id_2(self):

                obj2 = Base()
                self.assertEqual(obj2.id, 2)

        def test_id_any(self):

                obj = Base(15)
                self.assertEqual(obj.id, 15)

if __name__ == '__main__':
        unittest.main()
