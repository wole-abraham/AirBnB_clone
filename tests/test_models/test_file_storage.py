#!/usr/bin/python3

""" test model filestorage engine """

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import unittest
from datetime import datetime
import os
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
    
    def test_file_storage_save(self):

        """ test save """

        fs = FileStorage()
        bm = BaseModel()

        fs.new(bm)
        bm.save()
        self.assertTrue(bm.updated_at == datetime.now())
