#!/usr/bin/python3
"""Unit Tests For The `state` Module"""
import unittest
from models.state import State


class Teststate(unittest.TestCase):
    """TestState class to test State class"""

    def setUp(self):
        """setup for the tests"""
        self.state = State()
        
    def test_instance(self):
        """test for instanatio"""
        self.assertIsInstance(self.state, State)

    def test_attributes(self):
        """test attribute exist"""

        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(self.state.name, "")


if __name__ == "__main__":
    unittest.main()