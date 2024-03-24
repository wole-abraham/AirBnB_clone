#!/usr/bin/python3

""" base model  """

import uuid
from datetime import datetime


class BaseModel():

    """ basemodel """

    def __init__(self, *args, **kwargs):

        """ initialize constructors """

        from models import storage

        if kwargs:
            t_format = '%Y-%m-%dT%H:%M:%S.%f'
            for key in kwargs:
                if key != "__class__":
                    setattr(self, key, kwargs[key])
            self.created_at = datetime.strptime(kwargs['created_at'], t_format)
            self.updated_at = datetime.strptime(kwargs['updated_at'], t_format)

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

        from models import storage

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):

        """ dictionary represntation """

        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()

        return instance_dict
