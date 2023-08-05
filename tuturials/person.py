#!/usr/bin/python3

import json


class Person:

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"Name : {self.name} - Age : {self.age}"


person_1 = Person("Ahmed", 27)
person1_dict = person_1.__dict__
print(person1_dict)
person_1_json = json.dumps(person1_dict)
print(person_1_json)

with open("person.json", "w") as file:
    file.write(person_1_json)

# read json str from file
with open("person.json", "r") as f:
    person1_str = f.read()

person1_dict_format = json.loads(person1_str)
print(person1_dict_format)


def create_inst_from_dict(className, data_dict):
    inst = className.__new__(className)
    for key, value in data_dict.items():
        setattr(inst, key, value)
    return inst


person_instance_deserialized = create_inst_from_dict(
    Person, person1_dict_format)

print("Deserialized instance:", person_instance_deserialized)
