#!/usr/bin/python3

import unittest
from models.engine.file_storage import FileStorage
import sys
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
