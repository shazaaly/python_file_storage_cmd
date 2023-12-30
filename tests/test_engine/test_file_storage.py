#!/usr/bin/python3

import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import json

# Get the absolute path to the project directory
project_dir = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))

# Construct the path to file.json
json_file_path = os.path.join(project_dir, 'file.json')

# Load the JSON data
with open(json_file_path, 'r') as json_file:
    json_data = json.load(json_file)


class TestFileStorage(unittest.TestCase):
    """Unittests for FileStorage class"""

    def test_all_return_dict(self):
        """Test all method that returns the dictionary __objects"""
        dict_of_obj = FileStorage._FileStorage__objects
        self.assertIsInstance(dict_of_obj, dict)

    def test_all_dict_of_obj(self):
        """Test if returns dict of obj"""
        dict_of_obj = FileStorage._FileStorage__objects
        for key, obj in dict_of_obj.items():
            self.assertIsInstance(obj, object)

    def test_new(self):
        """sets in __objects the obj with key <obj class name>.id"""
        # expect :self.__objects[obj.__class__.__name__ + "." + obj.id] = obj
        dict_of_obj = FileStorage._FileStorage__objects
        for key, obj in dict_of_obj.items():
            self.assertEqual(key, f"{obj.__class__.__name__}.{obj.id}")

    def test_save(self):
        """Test serialization of __objects to the JSON file"""
        # make new obj save it and check key presence in file read
        base_inst = BaseModel()
        models.storage.new(base_inst)
        models.storage.save()
        text = ""
        with open(json_file_path, "r") as f:
            text = f.read()
            self.assertIn("BaseModel." + base_inst.id, text)

    def test_reload(self):
        """Test Deserialization the JSON file to __objects dict"""
        base_inst = BaseModel()
        models.storage.new(base_inst)
        models.storage.save()
        models.storage.reload()
        dict_of_obj = FileStorage._FileStorage__objects
        self.assertIn(f"BaseModel." + base_inst.id, dict_of_obj)


