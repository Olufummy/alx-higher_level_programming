#!/usr/bin/python3
"""Module that read a file and print your content
"""


def read_file(filename=""):
        """Function that a file and print.

        Args:
            filename (str, optional): file path. Defaults to "".
        """
        with open(filename, mode='r', encoding='utf-8') as afile:
                print(afile.read(), end="")
