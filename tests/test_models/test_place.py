#!/usr/bin/python3
"""Unit Tests For The `place` Module"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """TestPlace class to test Place class"""

    def setUp(self):
        """setup for the tests"""
        self.place = Place()

    def test_is_instance(self):
        """test for instanation"""
        self.assertIsInstance(self.place, Place)

    def test_attribute(self):
        """test attribute exist"""
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertEqual(self.place.city_id, "")

        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertEqual(self.place.user_id, "")

        self.assertTrue(hasattr(self.place, "name"))
        self.assertEqual(self.place.name, "")

        self.assertTrue(hasattr(self.place, "description"))
        self.assertEqual(self.place.description, "")

        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertEqual(self.place.latitude, 0.0)

        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertEqual(self.place.number_rooms, 0)

        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertEqual(self.place.number_bathrooms, 0)

        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertEqual(self.place.max_guest, 0)

        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertEqual(self.place.price_by_night, 0.0)

        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertEqual(self.place.longitude, 0.0)

        self.assertTrue(hasattr(self.place, "amenity_ids"))
        self.assertEqual(self.place.amenity_ids, [])


if __name__ == "__main__":
    unittest.main()
