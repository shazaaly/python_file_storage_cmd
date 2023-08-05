#!/usr/bin/python3
import unittest


class Tester(unittest.TestCase):

    def setUp(self):
        self.a = 10
        self.b = 20

    def tearDown(self) -> None:
        self.a = None
        self.b = None
