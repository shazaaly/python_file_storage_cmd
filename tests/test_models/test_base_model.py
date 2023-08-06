#!/usr/bin/python3
"""
This is the unittest of Base Module
It contains a class for unitest
"""

import unittest
from models.base_model import BaseModel
import datetime
import uuid


class TestBaseInstantation(unittest.TestCase):
    """
    Test case to ensure that the BaseModel class is instantiated correctly.

    It checks the following aspects of the BaseModel instance:
    1. 'id': Checks if the 'id' attribute is a valid UUID.
    2. 'created_at' and 'updated_at': Checks if both attributes are datetime objects.
    3. Timestamp comparison: Verifies that 'created_at' is earlier than 'updated_at'.

    """

    def test_model_json(self):
        """_test instantiation with correct id, created_at and updated_at
        """
        my_model = BaseModel()
        self.assertIsInstance(uuid.UUID(my_model.id), uuid.UUID)
        self.assertIsInstance(my_model.created_at, datetime.datetime)
        self.assertIsInstance(my_model.updated_at, datetime.datetime)
        self.assertLess(my_model.created_at, my_model.updated_at)


if __name__ == "__main__":
    unittest.main()
