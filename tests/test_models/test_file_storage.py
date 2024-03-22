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

    def test_file_storage_save(self):
        pass

    def test_file_storage_reload(self):
        pass

