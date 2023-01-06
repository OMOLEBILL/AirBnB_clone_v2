#!/usr/bin/python3
""" tests fot the console.py"""
import unittest
import pycodestyle
from io import StringIO
from unittest.mock import patch
import os
import json
import test
import console
from console import HBNBCommand
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.engine.file_storage import fileStorage


class TestConsole(unittest.TestCase):
    """This class contains test for the consle"""

    @classmethod
    def setUpClass(cls):
        cls.con = HBNBCommand()
    
    @classmethod
    def tearDownClass(cls) -> None:
        del cls.con
    
    def tearDown(self) -> None:
        """removes the file.json if it exist"""
        try:
            os.remove("file.json")
        except Exception:
            pass
    
    def test_pep8_base(self):
        """to test if file: console.py comform to PEP8
        """
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
    
    def test_docstring(self):
        """check wether the methods are documented"""
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_count.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_help.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNone(HBNBCommand.do_show.__doc__)