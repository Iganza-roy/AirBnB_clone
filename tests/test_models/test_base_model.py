#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage

class TestBaseModel(unittest.TestCase):

    def test_init(self):
        """Test default attribute values after initialization."""
        instance = BaseModel()
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_str(self):
        """Tests the str rep of an instance is formatted as excpected"""
        instance = BaseModel()
        str_rep = str(instance)
        self.assertIn("BaseModel", str_rep)
        self.assertIn(instance.id, str_rep)

    def test_save_method(self):
        """Test the update of updated_at after calling save."""
        instance = BaseModel()
        created_at = instance.updated_at
        instance.save()
        self.assertNotEqual(created_at, instance.updated_at)

    def test_to_dict_method(self):
        """Test the dictionary representation of the model."""
        instance = BaseModel()
        instance_dict = instance.to_dict()
        expected_keys = ['__class__', 'id', 'created_at', 'updated_at']
        self.assertEqual(set(instance_dict.keys()), set(expected_keys))
        self.assertIsInstance(instance_dict['created_at'], str)
        self.assertIsInstance(instance_dict['updated_at'], str)

    def test_id_uniqueness(self):
        """verifies that the id generated is unique for each instance"""
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id, "Each ID should be unique")

    def test_init_with_kwargs(self):
        """Test __init__ with kwargs."""
        kwargs = {'id': '123', 'created_at': '2022-01-01T00:00:00.000000', 'updated_at': '2022-01-01T01:00:00.000000'}
        instance = BaseModel(**kwargs)
        self.assertEqual(instance.id, '123')
        self.assertEqual(instance.created_at, datetime(2022, 1, 1, 0, 0, 0))
        self.assertEqual(instance.updated_at, datetime(2022, 1, 1, 1, 0, 0))

    def test_to_dict_after_update(self):
        """Test to_dict method after updating attributes."""
        instance = BaseModel()
        instance.name = "New Name"
        instance.my_number = 42
        instance.save()
        instance_dict = instance.to_dict()
        self.assertEqual(instance_dict['name'], 'New Name')
        self.assertEqual(instance_dict['my_number'], 42)


if __name__ == '__main__':
    unittest.main()
