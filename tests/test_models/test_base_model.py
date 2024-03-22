#!/usr/bin/python3

""" BaseModel tests """

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    """ BaseModel tests """

    def test_id(self):

        """ test id is unique for all instance
            id is string
            instance has attribute id
        """

        bm1 = BaseModel()
        bm2 = BaseModel()

        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm1.id, str)
        self.assertIsInstance(bm1, BaseModel)
        self.assertTrue(hasattr(bm1, 'id'))

    def test_dates(self):

        """
           test created_at and updated_at are strings
           instance has attributes created_at and updated_at

        """

        bm3 = BaseModel()
        self.assertTrue(hasattr(bm3, 'created_at'))
        self.assertTrue(hasattr(bm3, 'updated_at'))

    def test_to_dict(self):

        """
         test to_dict returns a dictionary
         dictionary contains: __class__, created_at, updated_at
         check datetime are strings

        """

        bm4 = BaseModel()
        bm4_dict = bm4.to_dict()

        self.assertIsInstance(bm4.to_dict(), dict)
        self.assertTrue('created_at' in bm4_dict)
        self.assertTrue('updated_at' in bm4_dict)
        self.assertIsInstance(bm4_dict.get('created_at'), str)
        self.assertIsInstance(bm4_dict.get('updated_at'), str)

    def test_from_dict(self):

        """
            re-create instance from dict
        """

        bm5 = BaseModel()
        bm5_dict = bm5.to_dict()
        bm6 = BaseModel(**bm5_dict)
        bm6_dict = bm6.to_dict()

        self.assertIsInstance(bm5, BaseModel)
        self.assertIsInstance(bm6, BaseModel)
        self.assertTrue(bm5_dict == bm6_dict)
        self.assertIsInstance(bm6.created_at, datetime)
        self.assertIsInstance(bm6.created_at, datetime)
