#!/usr/bin/python3
"""Module that read a file and print your content
"""


def read_lines(filename="", nb_lines=0):
        """Function that read n lines of a file.

        Args:
            filename (str, optional): path file. Defaults to "".
            nb_lines (int, optional): n line. Defaults to 0.
        """
        with open(filename, mode='r', encoding='utf-8') as afile:
                total_lines = 0
                while (afile.readline()):
                        total_lines += 1

        with open(filename, mode='r', encoding='utf-8') as afile:
                i = 0

                if (nb_lines <= 0 or nb_lines >= total_lines):
                        print(afile.read(), end="")
                else:
                        line = ""
                        while (i < nb_lines):
                                line = afile.readline()
                                print(line, end="")
                                i += 1
