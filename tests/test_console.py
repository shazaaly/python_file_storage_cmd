#!/usr/bin/python3
"""This module is to test console functionalities"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


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
            self.assertEqual("", output.getvalue().strip())
