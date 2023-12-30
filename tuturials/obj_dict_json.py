#!/usr/bin/env python3
class Student:
	def __init__(self, name, age, **kwargs):
		self.name = name
		self.age = age
		self.extra_info = kwargs

	def __str__(self):
		return self.name + ", " + str(self.age)


std = Student("Ahmed", 26, **{"class" : "A"})
print(f"object : {std}")
print(f"object name : {std.__dict__}")
