#!/usr/bin/python3
"""Unit Tests For The `user` Module"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """TestUser class to test User class"""

    def setUp(self):
        """setup for the tests"""
        self.user = User()

    def tearDown(self):
        """tearing down"""
        del self.user

    def test_is_instance(self):
        """test for instanation"""
        self.assertIsInstance(self.user, User)

    def test_attribute(self):
        """test attribute exist"""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_attribute_default(self):
        """test default attribute values"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_type_attribute(self):
        """test attribute value"""
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.last_name), str)

    def test_change_attribute(self):
        """test changing attribute values"""
        self.user.email = "email@email.com"
        self.user.password = "email1234"
        self.user.first_name = "Email"
        self.user.last_name = "User"
        self.assertEqual(self.user.email, "email@email.com")
        self.assertEqual(self.user.password, "email1234")
        self.assertEqual(self.user.first_name, "Email")
        self.assertEqual(self.user.last_name, "User")


if __name__ == "__main__":
    unittest.main()
