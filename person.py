#!/usr/bin/python3


class Person:

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        print(f"Name : {self.name} - Age : {self.age}")
