#!/bin/usr/python3

from models.user import User
import unittest

class TestUser(unittest.TestCase):
    
    """
     test cases:
            user has id
            user has created at, updated_at

    """

    def test_user_attributes(self):

        """ if user mode has:
                id, email, password, first_name
        """
        user = User()
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))

