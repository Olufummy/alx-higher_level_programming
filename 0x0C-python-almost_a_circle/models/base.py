#!/usr/bin/python3
"""Module base
"""


import json


class Base:
        """ Class base
        """
        __nb_objects = 0

        def __init__(self, id=None):

                if id is None:
                        Base.__nb_objects += 1
                        self.id = Base.__nb_objects
                else:
                        self.id = id

        @staticmethod
        def to_json_string(list_dictionaries):
                """to json string"""

                if list_dictionaries is None:
                        return "[]"
                return json.dumps(list_dictionaries)

        @classmethod
        def save_to_file(cls, list_objs):
                """save to file"""
                list_dictionaries = []
                if list_objs is not None:
                        for obj in list_objs:
                                list_dictionaries.append(obj.to_dictionary())
                stream = Base.to_json_string(list_dictionaries)
                with open(cls.__name__+".json", mode='w') as afile:
                        afile.write(stream)

        @staticmethod
        def from_json_string(json_string):
                """from json str"""
                if json_string is None:
                        return []
                list_objs = json.loads(json_string)
                return [dictionary for dictionary in list_objs]

        @classmethod
        def create(cls, **dictionary):
                """Classmethod create"""
                if cls.__name__ == "Rectangle":
                        dummy = cls(9, 5)
                if cls.__name__ == "Square":
                        dummy = cls(9)
                dummy.update(**dictionary)
                return dummy

        @classmethod
        def load_from_file(cls):
                """load from file"""
                list_instances = []
                ext = ".json"
                try:
                        with open(cls.__name__+ext, encoding='utf-8') as afile:
                                list_dict = cls.from_json_string(afile.read())
                        for way in list_dict:
                                dummy = cls.create(**way)
                                list_instances.append(dummy)
                        return list_instances
                except FileNotFoundError:
                        return []
