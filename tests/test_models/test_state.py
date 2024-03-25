#!/usr/bin/python3

from models.state import State
from models.base_model import BaseModel
from models import storage
import unittest


"""
    CHECK:
        attr: name// EXISTS
"""


class Test_State_Model(unittest.TestCase):

    """ test cases user model """

    def test_user_without_kwargs(self):

        """
        initialize without kwarsgs

        """

        self.asserTrue(hasattr(State, 'id'))
        self.assertTrue(hasattr(State, 'created_at'))
        self.assertTrue(hasattr(State, 'updated_at'))
        self.assertTrue(issubclass(State, BaseModel))
        self.assertTrue(hasattr(State, 'name'))

    def test_attributes(self):

        """ check state attributes """

        self.assertEqual(State.name, "")
        self.isinstance(State.id, str)
        self.issubclass(State, BaseModel)
