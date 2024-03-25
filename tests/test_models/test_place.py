#!/usr/bin/python3

from models.place import Place
from models.base_model import BaseModel
import unittest


class TestPlaceModel(unittest.TestCase):

    """
    Test cases for place_model

    """

    def test_attributes(self):

        """ check all attributes """

        self.assertEqual(Place.city_id, "")
        self.assertEqual(Place.user_id, "")
        self.assertEqual(Place.name, "")
        self.assertEqual(Place.description, "")
        self.assertEqual(Place.number_rooms, 0)
        self.assertEqual(Place.number_bathrooms, 0)
        self.assertEqual(Place.max_guest, 0)
        self.assertEqual(Place.price_by_night, 0)
        self.assertEqual(Place.latitude, 0.0)
        self.assertEqual(Place.longitude, 0.0)
        self.assertEqual(Place.amenity_ids, [])

    def test_instance(self):

        """ check atributes inherited from bas_model """

        self.assertTrue(issubclass(Place, BaseModel))
