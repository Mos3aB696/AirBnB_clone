#!/usr/bin/python3
"""Unit Tests For The `file_storage` Module"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
from models.state import State


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

    def test_reload_empty_file(self):
        """Test the reload method with an empty file"""
        with open("file.json", "w") as file:
            file.write("{}")
        self.file_storage.reload()
        self.assertEqual(len(self.file_storage.all()), 0)

    def test_reload_invalid_json(self):
        """Test the reload method with invalid JSON"""
        with open("file.json", "w") as file:
            file.write("{invalid json}")
        with self.assertRaises(ValueError):
            self.file_storage.reload()

    def test_new_invalid_object(self):
        """Test the new method with an invalid object"""
        with self.assertRaises(AttributeError):
            self.file_storage.new("invalid object")

    def test_save_file_error(self):
        """Test the save method with a file error"""
        self.file_storage.__file_path = "/invalid/path"
        with self.assertRaises(FileNotFoundError):
            self.file_storage.save()

    def test_reload_all_types(self):
        """Test the reload method with all object types"""
        self.file_storage.reload()
        for obj in self.file_storage.all().values():
            self.assertIn(obj.__class__.__name__, [
                          "BaseModel", "User", "Amenity", "City", "Review",
                          "Place", "State"])

    def test_all_multiple_new(self):
        """Test the all method with multiple new calls"""
        base_model_one = BaseModel()
        base_model_two = BaseModel()
        self.file_storage.new(base_model_one)
        self.file_storage.new(base_model_two)
        self.assertEqual(len(self.file_storage.all()), 2)

    def test_all_no_objects(self):
        """Test the all method with no objects"""
        self.assertEqual(len(self.file_storage.all()), 0)

    def test_reload_user(self):
        """Test the reload method with User object"""
        user = User()
        self.file_storage.new(user)
        self.file_storage.save()
        self.file_storage.reload()
        self.assertIn("User." + user.id, self.file_storage.all())

    def test_reload_state(self):
        """Test the reload method with State object"""
        state = State()
        self.file_storage.new(state)
        self.file_storage.save()
        self.file_storage.reload()
        self.assertIn("State." + state.id, self.file_storage.all())

    def test_reload_review(self):
        """Test the reload method with Review object"""
        review = Review()
        self.file_storage.new(review)
        self.file_storage.save()
        self.file_storage.reload()
        self.assertIn("Review." + review.id, self.file_storage.all())

    def test_reload_city(self):
        """Test the reload method with City object"""
        city = City()
        self.file_storage.new(city)
        self.file_storage.save()
        self.file_storage.reload()
        self.assertIn("City." + city.id, self.file_storage.all())

    def test_reload_place(self):
        """Test the reload method with Place object"""
        place = Place()
        self.file_storage.new(place)
        self.file_storage.save()
        self.file_storage.reload()
        self.assertIn("Place." + place.id, self.file_storage.all())

    def test_reload_amenity(self):
        """Test the reload method with Amenity object"""
        amenity = Amenity()
        self.file_storage.new(amenity)
        self.file_storage.save()
        self.file_storage.reload()
        self.assertIn("Amenity." + amenity.id, self.file_storage.all())


if __name__ == "__main__":
    unittest.main()
