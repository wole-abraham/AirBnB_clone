#!/usr/bin/python3

"""
    test cases

"""

from models.amenity import Amenity
from models.base_model import BaseModel
import unittest


class TestCityModel(unittest.TestCase):

    """
        model:
        attr
        inherits
    """

    def test_model_attr(self):

        """ test model attributes """

        model = Amenity()
        self.assertTrue(issubclass(Amenity, BaseModel))
        self.assertTrue(hasattr(Amenity, 'name'))

    def test_city_attributes(self):

        """ city attributs check xist"""

        self.assertEqual(Amenity.name, "")
        self.assertTrue(hasattr(Amenity, 'name'))
