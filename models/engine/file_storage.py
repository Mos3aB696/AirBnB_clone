#!/usr/bin/python3
"""class FileStorage"""

import json
from ..base_model import BaseModel


class FileStorage:
    """serializes instances to a JSON file and deserializes
    JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """set in __objects the obj"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        dictionary_obj = {}
        for key, val in FileStorage.__objects.items():
            dictionary_obj[key] = val.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(dictionary_obj, file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r") as file:
                FileStorage.__objects = json.load(file)
                for key, val in FileStorage.__objects.items():
                    FileStorage.__objects[key] = BaseModel(**val)
        except FileNotFoundError:
            pass
