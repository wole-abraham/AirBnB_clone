#!/usr/bin/python3

"""
    test cases

"""

from models.state import City
from models.base_model import BaseModel
from models import storage
import unittest


class TestCityModel(unittest.TestCase):

    """
        model:
        attr
        inherits
    """

    def test_model_attr(self):

        model = City()
        base_model = BaseModel()
        self.assertTrue(hasattr(User, 'id'))
        self.assertTrue(hasattr(User, 'created_at'))
        self.assertTrue(hasattr(User, 'updated_at'))
        self.assertTrue(issubclass(User, BaseModel))
        self.assertTrue(hasattr(User, 'state_id'))
