#!/usr/env/python3
"""this module is the base class of all models. It contains common elements
"""
import uuid
from datetime import datetime


class BaseModel:
    """A class to be used as base class to rest of models
    """

    def __init__(self, id, created_at, updated_at) -> None:
        """Constructor to initialize Public instance attributes in need at base
                Args:
                        id (_type_): uuidv4
                        created_at (_type_): datetime
                        updated_at (_type_): datetime
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self) -> str:
        """function returns string representatoin of BaseModel objects

                Returns:
                        str: prints: [<class name>] (<self.id>) <self.__dict__>
        """
        class_name = self.__class__.name
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """ updates the updated_at with the current datetime
                """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary of keys/values of __dict__ of the instance:
                """

        obj_dict = self.__dict__
        class_name = self.__class__.__name__
        obj_dict['__class__'] = class_name
        return obj_dict