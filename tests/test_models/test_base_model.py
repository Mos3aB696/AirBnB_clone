#!/usr/bin/python3
"""Unit Tests For The `base_model` Module"""
import os
import models
import unittest
import json
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


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

    def test_unique_id(self):
        """Test if the id is unique for each instance"""
        base_model2 = BaseModel()
        self.assertNotEqual(self.base_model.id, base_model2.id)

    def test_created_at(self):
        """Test if created_at is set correctly"""
        self.assertEqual(self.base_model.created_at,
                         self.base_model.updated_at)

    def test_save_method(self):
        """Test if save method updates updated_at"""
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(self.base_model.updated_at, old_updated_at)

    def test_str_method(self):
        """Test if __str__ method returns expected string"""
        string = "[BaseModel] ({}) {}".format(
            self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), string)

    def test_storage(self):
        """Test if the BaseModel instance is correctly stored"""
        models.storage.new(self.base_model)
        models.storage.save()
        self.assertIn("BaseModel.{}".format(
            self.base_model.id), models.storage.all())

    def test_removal(self):
        """Test if the BaseModel instance is correctly removed"""
        models.storage.new(self.base_model)
        models.storage.save()
        models.storage.delete(self.base_model)
        self.assertNotIn("BaseModel.{}".format(
            self.base_model.id), models.storage.all())

    def test_update(self):
        """Test if the BaseModel instance is correctly updated"""
        self.base_model.name = "New Name"
        models.storage.save()
        self.assertEqual(models.storage.all()["BaseModel.{}".format(
            self.base_model.id)].name, "New Name")

    def test_retrieval(self):
        """Test if the BaseModel instance is correctly retrieved"""
        models.storage.new(self.base_model)
        models.storage.save()
        retrieved_model = models.storage.get("BaseModel", self.base_model.id)
        self.assertEqual(retrieved_model, self.base_model)


if __name__ == '__main__':
    unittest.main()
