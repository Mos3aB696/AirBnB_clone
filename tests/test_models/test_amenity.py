#!/usr/bin/python3
"""Unit Tests For The `amenity` Module"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """TestAmenity class to test Amenity class"""

    def setUp(self):
        """setup for the tests"""
        self.amenity = Amenity()

    def test_instance(self):
        """test for instanation"""
        self.assertIsInstance(self.amenity, Amenity)

    def test_attributes(self):
        """test attribute exist"""
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.name, "")


if __name__ == "__main__":
    unittest.main()
