#!/usr/bin/python

""" File Storage Module """

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.city import City

class FileStorage():

    """ Deserialization and serialization of json file """

    __file_path = 'file.json'
    __objects = {}

    def all(self):

        """ public instance methods """

        return FileStorage.__objects

    def new(self, obj):

        """ create new  """

        key = f'{obj.__class__.__name__}.{obj.id}'

        FileStorage.__objects[key] = obj

    def save(self):

        """ serialize __objects to json and saves file """
        serialized_obj = {}
        for key, obj in FileStorage.__objects.items():
            serialized_obj[key] = obj.to_dict()
        path = FileStorage.__file_path
        with open(path, mode='w', encoding='utf-8') as file:
            json.dump(serialized_obj, file)

    def reload(self):

        """ deserializes json file to __objects """

        models = {'BaseModel': BaseModel,
                  'User':User, 'Place':Place,
                  'State':State, 'Amenity':Amenity,
                  'City':City, 'Review':Review
                  }
        
        path = FileStorage.__file_path
        try:
            with open(path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                for keys, value in data.items():
                    model = keys.split('.')[0]
                    obj = models[model](**value)
                    FileStorage.__objects[keys] = obj

        except FileNotFoundError:
            pass
