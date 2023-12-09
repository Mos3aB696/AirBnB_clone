#!/usr/bin/python3
"""Unit Tests For The `base_model` Module"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Tests for the BaseModel class"""

    def setUp(self):
        """Set up for the tests"""
        self.base_model = BaseModel()

    def test_init(self):
        """Test for the __init__ method"""
        self.assertIsInstance(self.base_model, BaseModel)
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_str(self):
        """Test for the __str__ method"""
        string = "[BaseModel] ({}) {}".format(
            self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), string)

    def test_save(self):
        """Test for the save method"""
        the_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(self.base_model.updated_at, the_updated_at)

    def test_to_dict(self):
        """Test for the to_dict method"""
        dict = self.base_model.to_dict()
        self.assertEqual(dict["__class__"], "BaseModel")
        self.assertEqual(dict["id"], self.base_model.id)
        self.assertEqual(dict["created_at"],
                         self.base_model.created_at.isoformat())
        self.assertEqual(dict["updated_at"],
                         self.base_model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
