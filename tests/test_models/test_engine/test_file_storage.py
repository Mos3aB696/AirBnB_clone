#!/usr/bin/python3
"""Unit Tests For The `file_storage` Module"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

    def setUp(self):
        """Set up for the tests"""
        self.file_storage = FileStorage()

    def tearDown(self):
        """Tear down for the tests"""
        del self.file_storage

    def test_all(self):
        """Test the all method"""
        self.assertIsInstance(self.file_storage.all(), dict)

    def test_new(self):
        """Test the new method"""
        base_model = BaseModel()
        self.file_storage.new(base_model)
        self.assertIn("BaseModel." + base_model.id, self.file_storage.all())

    def test_save(self):
        """Test the save method"""
        base_model = BaseModel()
        self.file_storage.new(base_model)
        self.file_storage.save()
        with open("file.json", "r") as file:
            self.assertIn("BaseModel." + base_model.id, file.read())

    def test_reload(self):
        """Test the reload method"""
        self.file_storage.reload()
        self.assertIsInstance(self.file_storage.all(), dict)


if __name__ == "__main__":
    unittest.main()
