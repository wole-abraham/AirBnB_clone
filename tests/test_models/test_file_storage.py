#!/usr/bin/python3

""" test model filestorage engine """

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import unittest
from datetime import datetime
import os
import json
from unittest.mock import patch


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

    def test_file_storgage_new(self):

        """
        new() method create dictionary object
        and passes it to __objects

        """
        base_model = BaseModel()
        base_model_key = f"{BaseModel}.{base_model.id}"
        storage_all = self.fs.all()
        self.assertTrue(base_model_key in self.fs.all())
        self.fs.reload()

    def test_file_storage_reload(self):

        """ test reloaded are objetcs """

        fs = FileStorage()
        bm = BaseModel()
        fs.new(bm)
        bm.save()
        fs.reload()
        self.assertTrue(isinstance(fs.__objects[f'BaseModel.{bm.id}'], BaseModel))

class TestFileStorageReload(unittest.TestCase):
    def setUp(self):
        # Create a sample JSON file with some data
        sample_data = {
            'BaseModel.1': {'attr1': 'value1'},
            'User.2': {'attr2': 'value2'}
        }
        with open('test_file.json', 'w') as f:
            json.dump(sample_data, f)

    def tearDown(self):
        # Delete the test JSON file after the test
        import os
        os.remove('test_file.json')

    def test_reload(self):
        # Instantiate a FileStorage object and call reload
        fs = FileStorage()
        fs.reload()

        # Check if __objects attribute contains the expected data
        expected_data = {
            'BaseModel.1': {'attr1': 'value1'},
            'User.2': {'attr2': 'value2'}
        }
        self.assertEqual(fs._FileStorage__objects, expected_data)

class TestFileStorageSave(unittest.TestCase):
    @patch('models.storage')
    def test_file_storage_save(self, mock_storage):
        # Create a FileStorage instance
        fs = FileStorage()

        # Create a BaseModel instance
        bm = BaseModel()

        # Set the initial updated_at time
        initial_updated_at = bm.updated_at

        # Add the BaseModel instance to the FileStorage instance
        fs.new(bm)

        # Call the save method of the BaseModel instance
        bm.save()

        # Assert that the save method of the FileStorage instance was called
        mock_storage.save.assert_called_once()

        # Assert that the updated_at attribute of the BaseModel instance was updated
        self.assertNotEqual(bm.updated_at, initial_updated_at)
        self.assertEqual(bm.updated_at, mock_storage.updated_at)
