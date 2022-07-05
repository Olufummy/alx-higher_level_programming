#!/usr/bin/python3
"""Module that read a file and print your content
"""


def number_of_lines(filename=""):
        """Function that read a file and count number of lines.

        Args:
            filename (str, optional): file path. Defaults to "".
        """
        with open(filename, mode='r', encoding='utf-8') as afile:
                num_line = 0
                while (afile.readline()):
                        num_line += 1
                return num_line
