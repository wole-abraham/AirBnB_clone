#!/usr/bin/python3

""" base model  """

import uuid
from datetime import datetime


class BaseModel():

    """
    BaseModel serves as the base class for all models in the system.

    Attributes:
        id (str): A unique identifier for the object.
        created_at (datetime): The datetime when the object was created.
        updated_at (datetime): The datetime when the object was last updated.

    Methods:
        __init__(self, *args, **kwargs):
            Initializes a new instance of the BaseModel class.
        __str__(self):
            Returns a string representation of the object.
        save(self):
            Updates the `updated_at` attribute and saves the object.
        to_dict(self):
            Returns a dictionary representation of the object.

    """

    def __init__(self, *args, **kwargs):

        """
        Initializes a new instance of the BaseModel class.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        If keyword arguments are provided (`kwargs`),
        it sets attributes of the object based on those arguments.
        If no keyword arguments are provided,
        it generates a new `id` using `uuid.uuid4()`,
        sets `created_at` and `updated_at` attributes
        to the current datetime, and adds the new object to storage.

        """

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

        """
        Returns a string representation of the object.

        Returns:
            str: A string representation of the object,
            including class name, object ID, and attribute dictionary.
        """

        return (f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}')

    def save(self):

        """
        Updates the `updated_at` attribute to the current datetime
        and saves the object.

        This method is responsible for updating the
        `updated_at` attribute with the current datetime
        and saving the object using the storage mechanism.
        """

        from models import storage

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):

        """
        Returns a dictionary representation of the object.

        Returns:
            dict: A dictionary representation of the object,
            including all attributes,
            class name, and timestamps formatted as ISO 8601 strings.
        """

        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()

        return instance_dict
