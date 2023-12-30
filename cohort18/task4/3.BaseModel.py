import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"


    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dict_representation = self.__dict__.copy()
        dict_representation['__class__'] = self.__class__.__name__
        dict_representation['created_at'] = self.created_at.isoformat()
        dict_representation['updated_at'] = self.updated_at.isoformat()
        return dict_representation


my_model = BaseModel()
print(my_model)
# Modify the instance (here we could add or change attributes)
my_model.save()  # Update the 'updated_at' attribute
model_dict = my_model.to_dict()
print(model_dict)


