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

    def test_init_with_kwargs(self):
        # Test initialization with keyword arguments
        data = {
            'id': '123',
            'created_at': '2024-03-24T12:00:00.000000',
            'updated_at': '2024-03-24T12:00:00.000000',
            'custom_attr': 'value'
        }
        obj = BaseModel(**data)
        self.assertEqual(obj.id, '123')
        self.assertEqual(obj.created_at, datetime(2024, 3, 24, 12, 0, 0))
        self.assertEqual(obj.updated_at, datetime(2024, 3, 24, 12, 0, 0))
        self.assertEqual(obj.custom_attr, 'value')

    def test_init_without_kwargs(self):
        # Test initialization without keyword arguments
        obj = BaseModel()
        self.assertTrue(isinstance(obj.id, str))
        self.assertTrue(isinstance(obj.created_at, datetime))
        self.assertTrue(isinstance(obj.updated_at, datetime))
        self.assertNotEqual(obj.id, '')
        self.assertNotEqual(obj.created_at, obj.updated_at)

    def test_save(self):
        # Test the save method
        obj = BaseModel()
        old_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(obj.updated_at, old_updated_at)

    def test_to_dict(self):
        # Test the to_dict method
        data = {
            'id': '123',
            'created_at': '2024-03-24T12:00:00.000000',
            'updated_at': '2024-03-24T12:00:00.000000',
            'custom_attr': 'value'
        }
        obj = BaseModel(**data)
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict['id'], '123')
        self.assertEqual(obj_dict['created_at'], '2024-03-24T12:00:00')
        self.assertEqual(obj_dict['updated_at'], '2024-03-24T12:00:00')
        self.assertEqual(obj_dict['custom_attr'], 'value')
