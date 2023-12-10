#!/usr/bin/python3
"""Unit Tests For The `base_model` Module"""
import os
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel


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

    def test_class_name(self):
        self.assertEqual(self.base_model.__class__.__name__, "BaseModel")

    def test_attribute_types(self):
        self.assertEqual(type(self.base_model.id), str)
        self.assertEqual(type(self.base_model.created_at), datetime)
        self.assertEqual(type(self.base_model.updated_at), datetime)

    def test_attribute_values(self):
        self.assertTrue(len(self.base_model.id) > 0)
        self.assertTrue(self.base_model.created_at <= datetime.now())
        self.assertTrue(self.base_model.updated_at <= datetime.now())

    def test_updated_at_after_save(self):
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertTrue(self.base_model.updated_at > old_updated_at)


if __name__ == '__main__':
    unittest.main()
