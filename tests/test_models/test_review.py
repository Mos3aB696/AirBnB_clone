#!/usr/bin/python3
"""Unit Tests For The `review` Module"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """TestReview class to test Review class"""

    def setUp(self):
        """setup for the tests"""
        self.review = Review()

    def test_is_instance(self):
        """test for instanation"""
        self.assertIsInstance(self.review, Review)

    def test_attribute(self):
        """test attribute exist"""
        self.assertTrue(hasattr(self.review, "plac_id"))
        self.assertEqual(self.review.place_id, "")
        
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertEqual(self.review.user_id, "")

        self.assertTrue(hasattr(self.review, "text"))
        self.assertEqual(self.review.text, "")

if __name__ == "__main__":
    unittest.main()