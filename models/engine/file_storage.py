#!/usr/bin/env python3
"""defining a FileStorage class"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                serialized_objects = json.load(file)

                if serialized_objects:
                    for key, obj_dict in serialized_objects.items():
                        class_name, obj_id = key.split('.')
                        obj = eval(class_name)(**obj_dict)
                        FileStorage.__objects[key] = obj
        except (FileNotFoundError, json.JSONDecodeError):
            pass
