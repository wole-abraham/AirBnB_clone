#!/bin/usr/python3

from models.user import User
import unittest
from models.base_model import BaseModel

class TestUser(unittest.TestCase):

    """
     check all user attributes are available

    """
    def test_user_attributes(self):

        """ if user mode has:
                id, email, password, first_name
        """
        user = User()
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_class_attributes(self):
        # Test if class attributes are initialized correctly
        self.assertEqual(User.email, "")
        self.assertEqual(User.password, "")
        self.assertEqual(User.first_name, "")
        self.assertEqual(User.last_name, "")

    def test_inheritance(self):
        # Test if User class inherits from BaseModel
        self.assertTrue(issubclass(User, BaseModel))
