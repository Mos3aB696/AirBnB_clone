#!/usr/bin/python3
"""Unit Tests For The `city` Module"""
import unittest
from models.city import City


class Testcity(unittest.TestCase):
    """"""

    def setUp(self):
        """"""
        self.city = City()

    def test_instance(self):
        """"""
        self.assertIsInstance(self.city, City)

    def test_attributes(self):
        """"""
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertEqual(self.city.state_id, "")

        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(self.city.name, "")


if __name__ == "__main__":
    unittest.main()
