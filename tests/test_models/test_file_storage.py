#!/usr/bin/python3

""" test model filestorage engine """

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest
import json


class TestFileStorage(unittest.TestCase):

    """ Test cases for FileStorage """

    def setUp(self):

        """ instances """

        self.fs = FileStorage()
        self.bm = BaseModel()

    def test_file_storage_all(self):

        """ checks all() method returns a dictionary """

        fs = self.fs.all()
        self.assertIsInstance(fs, dict)

    def test_file_storgae_new(self):

        """
        new() method create dictionary object
        and passes it to __objects

        """

        bm2 = self.bm
        bm2_dict = bm2.to_dict()
        id, name = bm2.id, bm2.__class__.__name__
        fs = self.fs
        fs_new = fs.new(bm2)
        fs_all = fs.all()
        self.assertTrue(f'{name}.{id}' in fs_all)

    def setUp(self):
        self.file_path = 'test_file.json'
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_save_and_reload(self):
        # Create objects
        obj1 = BaseModel(id='1', created_at=datetime(2022, 1, 1),
                         updated_at=datetime(2022, 1, 1))
        obj2 = BaseModel(id='2', created_at=datetime(2022, 1, 2),
                         updated_at=datetime(2022, 1, 2))

        # Add objects to storage and save
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()

        # Clear objects from storage
        self.storage._FileStorage__objects = {}

        # Reload objects from file
        self.storage.reload()

        # Check if objects were properly loaded
        self.assertTrue('BaseModel.1' in self.storage._FileStorage__objects)
        self.assertTrue('BaseModel.2' in self.storage._FileStorage__objects)
        self.assertEqual(self.storage._FileStorage__objects['BaseModel.1'].id,
                         '1')
        self.assertEqual(self.storage._FileStorage__objects['BaseModel.2'].id,
                         '2')

    def test_new_and_all(self):
        # Create objects
        obj1 = BaseModel(id='1', created_at=datetime(2022, 1, 1),
                         updated_at=datetime(2022, 1, 1))
        obj2 = BaseModel(id='2', created_at=datetime(2022, 1, 2),
                         updated_at=datetime(2022, 1, 2))

        # Add objects to storage
        self.storage.new(obj1)
        self.storage.new(obj2)

        # Retrieve all objects from storage
        objects = self.storage.all()

        # Check if all objects are retrieved
        self.assertEqual(len(objects), 2)
        self.assertTrue('BaseModel.1' in objects)
        self.assertTrue('BaseModel.2' in objects)
        self.assertEqual(objects['BaseModel.1'].id, '1')
        self.assertEqual(objects['BaseModel.2'].id, '2')
