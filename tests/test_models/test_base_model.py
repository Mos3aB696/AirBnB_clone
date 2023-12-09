#!/usr/bin/python3
"""Unit Tests For The `base_model` Module"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Tests for the BaseModel class"""

    def setUp(self):
        """Set up for the tests"""
        self.instance = BaseModel()

    def test_init(self):
        """Test for the __init__ method"""
        self.assertIsInstance(self.instance, BaseModel)
        self.assertIsInstance(self.instance.id, str)
        self.assertIsInstance(self.instance.created_at, datetime)
        self.assertIsInstance(self.instance.updated_at, datetime)

    def test_str(self):
        """Test for the __str__ method"""
        string = "[BaseModel] ({}) {}".format(
            self.instance.id, self.instance.__dict__)
        self.assertEqual(str(self.instance), string)

    def test_save(self):
        """Test for the save method"""
        the_updated_at = self.instance.updated_at
        self.instance.save()
        self.assertNotEqual(self.instance.updated_at, the_updated_at)

    def test_to_dict(self):
        """Test for the to_dict method"""
        dict = self.instance.to_dict()
        self.assertEqual(dict["__class__"], "BaseModel")
        self.assertEqual(dict["id"], self.instance.id)
        self.assertEqual(dict["created_at"],
                         self.instance.created_at.isoformat())
        self.assertEqual(dict["updated_at"],
                         self.instance.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
