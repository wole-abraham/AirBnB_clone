#!/usr/bin/python3

""" base model  """

import uuid
import copy
from datetime import datetime
from . import storage

class BaseModel():
    
    """ basemodel """

    def __init__(self, *args, **kwargs):

        """ initialize constructors """
        
        if kwargs:
            self.id = kwargs['id']
            self.created_at = datetime.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):

        """ string representation of basemodel """

        return (f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}')

    
    def save(self):
        
        """ updates the public instance attribute update_at """

        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):

        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()

        return instance_dict
