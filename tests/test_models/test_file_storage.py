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
        self.fs.reload()
        self.assertTrue(isinstance(self.fs.all(), dict))

    def test_file_storage_reload(self):

        """ test reloaded are objetcs """

        fs = FileStorage()
        bm = BaseModel()
        fs.new(bm)
        bm.save()
        fs.reload()
        self.assertTrue(isinstance(fs.all()[f'BaseModel.{bm.id}'], BaseModel))

    def test_save(self):

        """ test if time is updated """
        
        bm = BaseModel()
        bm.save()
        self.assertTrue(bm.created_at != bm.updated_at)
