#!/usr/bin/python3
"""This module is to test console functionalities"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage


class TestConsole(unittest.TestCase):
    """Test a console functionalities: (hbnb)"""

    def test_prompt(self):
        """Test prompt message"""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_quit(self):
        """Test prompt message"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF(self):
        """Test EOF functionality"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_empty_line(self):
        """ Test handling empty lines """
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertEqual("", output.getvalue())


class TestCreate(unittest.TestCase):
    """Test Creating a new instance of Class,
    saves it (to the JSON file)"""

    def test_args_length(self):
        """test if args length < 1 to print [** class name missing **]"""
        with patch("sys.stdout", new=StringIO()) as output:
            input = "create"
            expected = "** class name missing **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected, output.getvalue().strip())

    def test_invalid_className(self):
        """Test if input is not a valid class"""
        with patch("sys.stdout", new=StringIO()) as output:
            input = "create UnknownClass"
            expected = "** class doesn't exist **"
            HBNBCommand().onecmd(input)  # excute command
            self.assertEqual(expected, output.getvalue().strip())

    def test_create(self):
        """test creating a new instance of a Class,
        saves it (to the JSON file)"""
        with patch("sys.stdout", new=StringIO()) as output:
            input = "create BaseModel"  # input
            HBNBCommand().onecmd(input)  # excute command
            captured_id = output.getvalue().strip()

            inst_key = "BaseModel.{}".format(captured_id)
            input = "create BaseModel"
            self.assertIn(inst_key, storage.all().keys())
