#!/usr/bin/python3

"""
    test cases

"""

from models.city import City
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

        """ test model attributes """

        self.assertTrue(issubclass(City, BaseModel))
        self.assertTrue(hasattr(City, 'state_id'))
        self.assertTrue(hasattr(City, 'name'))

    def test_city_attributes(self):

        """ city attributs check xist"""

        self.assertEqual(City.name, "")
        self.assertTrue(hasattr(City, 'name'))
        self.assertTrue(hasattr(City, 'state_id'))
