#!/usr/bin/python3
"""Mudule test pep8"""


import unittest
import pep8


class TestCodeFormat(unittest.TestCase):
        """Test format PEP8"""
        def test_pep8_conformance(self):
                """Test that we conform to PEP8."""

                pep8style = pep8.StyleGuide(quiet=True)
                result = pep8style.check_files(['models/base.py',
                                                'models/rectangle.py',
                                                'models/square.py'])

                for key in result.messages:
                        print("{}:{}".format(key, result.messages[key]))

                self.assertEqual(result.total_errors, 0)
