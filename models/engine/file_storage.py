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

        attr = ['email','password', 'first_name', 'last_name',
                'name', 'number_rooms', 'number_bathrooms',
                'max_guest', 'price_by_night', 'latitude',
                'longitude', 'amenity_id', 'place_id',
                'user_id', 'text', 'state_id']

        models = ['User', 'State', 'Review', 'Amenity',
                'City', 'Place', 'BaseModel']

        if obj.__class__.__name__ in models:
            for attr in attr:
                if hasattr(obj, attr):
                    setattr(obj, attr, getattr(obj, attr))
            FileStorage.__objects[key] = obj

        """elif obj.__class__.__name__ == "State":
            obj_dict['name'] = obj.name

        elif obj.__class__.__name__ == 'City':

            obj_dict['state_id'] = obj.id
            obj_dict['name'] = ""

        elif obj.__class__.__name__ == 'Amenity':
            obj_dict['name'] = obj.name

        elif obj.__class__.__name__ == 'Place':
            obj_dict['city_id'] = ""
            obj_dict['user_id'] = ""
            obj_dict['name'] = obj.name
            obj_dict['description'] = obj.description
            obj_dict['number_rooms'] = obj.number_rooms
            obj_dict['number_bathrooms'] = obj.number_rooms
            obj_dict['max_guest'] = obj.max_guest
            obj_dict['price_by_night'] = obj.price_by_night
            obj_dict['latitude'] = obj.latitude
            obj_dict['longitude'] = obj.longitude
            obj_dict['amenity_ids'] = obj.amenity_id

        elif obj.__class__.__name__ == 'Review':
            obj_dict['place_id'] = ""
            obj_dict['user_id'] = ""
            obj_dict['text'] = "" """



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
