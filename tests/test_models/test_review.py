#!/bin/usr/python3

from models.review import Review
import unittest


class TestUser(unittest.TestCase):

    """
     check all user attributes are available

    """
    def test_user_attributes(self):

        """ if user mode has:
            its iwn attr
        """

        self.assertTrue(hasattr(Review, 'id'))
        self.assertTrue(hasattr(Review, 'created_at'))
        self.assertTrue(hasattr(Review, 'updated_at'))
        self.assertTrue(hasattr(Review, 'place_id'))
        self.assertTrue(hasattr(Review, 'user_id'))
        self.assertTrue(hasattr(Review, 'place_id'))

    def test_class_attributes(self):
        # Test if class attributes are initialized correctly
        self.assertEqual(Review.place_id, "")
        self.assertEqual(Review.user_id, "")
        self.assertEqual(Review.text, "")

    def test_inheritance(self):
        # Test if User class inherits from BaseModel
        self.assertTrue(issubclass(Review, BaseModel))
