#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):

    def test_init(self):
        """Test default attribute values after initialization."""
        n_inst = BaseModel()
        self.assertIsInstance(n_inst.id, str)
        self.assertIsInstance(n_inst.created_at, datetime)
        self.assertIsInstance(n_inst.updated_at, datetime)

    def test_str(self):
        """Tests the str rep of an n_inst is formatted as excpected"""
        n_inst = BaseModel()
        str_rep = str(n_inst)
        self.assertIn("BaseModel", str_rep)
        self.assertIn(n_inst.id, str_rep)

    def test_save_method(self):
        """Test the update of updated_at after calling save."""
        n_inst = BaseModel()
        created_at = n_inst.updated_at
        n_inst.save()
        self.assertNotEqual(created_at, n_inst.updated_at)

    def test_to_dict_method(self):
        """Test the dictionary representation of the model."""
        n_inst = BaseModel()
        n_inst_dict = n_inst.to_dict()
        expected_keys = ['__class__', 'id', 'created_at', 'updated_at']
        self.assertEqual(set(n_inst_dict.keys()), set(expected_keys))
        self.assertIsInstance(n_inst_dict['created_at'], str)
        self.assertIsInstance(n_inst_dict['updated_at'], str)

    def test_id_uniqueness(self):
        """verifies that the id generated is unique for each n_inst"""
        n_inst1 = BaseModel()
        n_inst2 = BaseModel()
        self.assertNotEqual(n_inst1.id, n_inst2.id, "Each ID should be unique")

    def test_init_with_kwargs(self):
        """Test __init__ with kwargs."""
        kwargs = {
                'id': '123', 'created_at': '2022-01-01T00:00:00.000000',
                'updated_at': '2022-01-01T01:00:00.000000'
                }
        n_inst = BaseModel(**kwargs)
        self.assertEqual(n_inst.id, '123')
        self.assertEqual(n_inst.created_at, datetime(2022, 1, 1, 0, 0, 0))
        self.assertEqual(n_inst.updated_at, datetime(2022, 1, 1, 1, 0, 0))

    def test_to_dict_after_update(self):
        """Test to_dict method after updating attributes."""
        n_inst = BaseModel()
        n_inst.name = "New Name"
        n_inst.my_number = 42
        n_inst.save()
        n_inst_dict = n_inst.to_dict()
        self.assertEqual(n_inst_dict['name'], 'New Name')
        self.assertEqual(n_inst_dict['my_number'], 42)

    def test_save_updates_file(self):
        """Test if calling save updates the content of the file."""
        n_inst = BaseModel()
        n_inst.save()
        file_content = ""
        with open("file.json", "r") as f:
            file_content = f.read()

        self.assertIn("BaseModel." + n_inst.id, file_content)

    def test_to_dict_includes_new_attributes(self):
        """Test if to_dict includes newly added attributes."""
        n_inst = BaseModel()
        n_inst.new_attribute = "New Value"
        n_inst.save()
        n_inst_dict = n_inst.to_dict()

        self.assertIn("new_attribute", n_inst_dict)


if __name__ == '__main__':
    unittest.main()
