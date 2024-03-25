#!/bin/usr/python3

from models.user import User
import unittest


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
