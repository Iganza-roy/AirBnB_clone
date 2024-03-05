#!/usr/bin/python3
"""Defines BaseModel Class"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Class that defines all common attributes/methods for other classes"""
    def __init__(self):
        """Inits an instance of BaseModel"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """String represntation of an object"""
        c_name = self.__class__.__name__
        return "[{}] ({}) <{}>".format(c_name, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dict containing keys/values of __dict__"""
        o_dict = self.__dict__.copy()
        o_dict['__class__'] = self.__class__.__name__
        o_dict['created_at'] = self.created_at.isoformat()
        o_dict['updated_at'] = self.updated_at.isoformat()
        return o_dict
