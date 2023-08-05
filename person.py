#!/usr/bin/python3

import json


class Person:

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        print(f"Name : {self.name} - Age : {self.age}")


person_1 = Person("Ahmed", 27)
person1_dict = person_1.__dict__
print(person1_dict)
person_1_json = json.dumps(person1_dict)
print(person_1_json)

with open("person.json", "w") as file:
    file.write(person_1_json)
