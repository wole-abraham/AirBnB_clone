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
        model = User()
        b_model = BaseModel()
        self.assertTrue(hasattr(model, 'name'))
        self.asserTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))
        self.assertTrue(issubclass(model, b_model))
