#!/usr/bin/python3
"""This module is to serializes instances
to a JSON file and deserializes JSON file to instances
"""
import json
from models.base_model import to_dict


class FileStorage():
    """class FileStorage that serializes
        instances to a JSON file and deserializes
        JSON file to instances
    """
    __file_path = ""  # string - path to the JSON file (ex: file.json)
    __objects = {}  # dictionary, empty will store \
    # all objects <class name>.id\ example BaseModel.12121212

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        data = {}

        for key, obj in FileStorage.__objects.items():
            obj_dict = obj.to_dict()
            data[key] = obj_dict

        with open(FileStorage.__file_path, "w") as file:
            file.write(json.dumps(data))

    def reload(self):
        """deserializes the JSON file to __objects \
            (only if the JSON file (__file_path) exists ;\
                otherwise, do nothing. If the file doesn’t exist,\
                    no exception should be raised)"""
        try:
            if FileStorage.__file_path:
                with open(FileStorage.__file_path, "r") as file:
                    json_format = file.read()
                    back_to_dict = json.loads(json_format)
                    return back_to_dict
        except FileNotFoundError:
            pass
