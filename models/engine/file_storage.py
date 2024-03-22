#!/usr/bin/python

""" File Storage Module """

import json


class FileStorage():

    """ Deserialization and serialization of json file """

    __file_path = 'file.json'
    __objects = {}

    def all(self):

        """ public instance methods """

        return FileStorage.__objects

    def new(self, obj):

        """ create new  """

        obj_key = f'{obj.__class__.__name__}.{obj.id}'
        obj_dict = obj.to_dict()

        if obj.__class__.__name__ == "User":
            obj_dict['first_name'] = obj.first_name
            obj_dict['last_name'] = obj.last_name
            obj_dict['email'] = obj.email
            obj_dict['password'] = obj.password

        elif obj.__class__.__name__ == "State":
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
            obj_dict['text'] = ""

        FileStorage.__objects[obj_key] = obj_dict

    def save(self):

        """ serialize __objects to json and saves file """

        path = FileStorage.__file_path
        with open(path, mode='w', encoding='utf-8') as file:
            file.write(json.dumps(FileStorage.__objects))

    def reload(self):

        """ deserializes json file to __objects """

        path = FileStorage.__file_path
        try:
            with open(path, 'r', encoding='utf-8') as file:
                objects = file.read()
                FileStorage.__objects = json.loads(objects)

        except FileNotFoundError:
            pass
