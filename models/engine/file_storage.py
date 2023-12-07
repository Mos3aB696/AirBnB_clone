#!/usr/bin/python3
"""class FileStorage"""

import json
from models.base_model import BaseModel

class FileStorage:
    """Private class attributes"""

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
        dic_objects = {}
        for key, value in FileStorage.__objects.items():
            dic_objects[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            json.dump(dic_objects, file)
