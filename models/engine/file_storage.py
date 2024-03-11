#!/usr/bin/env python3
"""Defining a FileStorage class"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    Serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        ser_obj = {}
        for key, obj in FileStorage.__objects.items():
            ser_obj[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(ser_obj, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        if os.path.exists(self._FileStorage__file_path):
            try:
                with open(FileStorage.__file_path, 'r') as file:
                    ser_obj = json.load(file)

                    if ser_obj:
                        for key, obj_dict in ser_obj.items():
                            class_name, obj_id = key.split('.')
                            if class_name == 'BaseModel':
                                obj = BaseModel(**obj_dict)
                            elif class_name == 'User':
                                obj = User(**obj_dict)
                            elif class_name == 'Place':
                                obj = Place(**obj_dict)
                            elif class_name == 'State':
                                obj = State(**obj_dict)
                            elif class_name == 'City':
                                obj = City(**obj_dict)
                            elif class_name == 'Amenity':
                                obj = Amenity(**obj_dict)
                            elif class_name == 'Review':
                                obj = Review(**obj_dict)
                            else:
                                continue
                            self._FileStorage__objects[key] = obj
            except (FileNotFoundError, json.JSONDecodeError):
                pass
