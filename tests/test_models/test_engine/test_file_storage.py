#!/usr/bin/python3
"""defining the testfilestorage class"""
import unittest
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()

    def test_all_method(self):
        """Test the all method."""
        self.storage._FileStorage__objects.clear()
        actual_result = self.storage.all()
        self.assertEqual(actual_result, {})

    def test_new_method(self):
        """Test the new method."""
        obj = BaseModel()

        self.storage.new(obj)

        self.assertIn(f"{type(obj).__name__}.{obj.id}", self.storage.all())

    def test_save_method(self):
        """Test the save method."""
        obj = BaseModel()

        self.storage.new(obj)

        self.storage.save()

        with open(self.storage._FileStorage__file_path, 'r') as file:
            data = json.load(file)
            self.assertIn(f"{type(obj).__name__}.{obj.id}", data)

    def test_reload_method(self):
        """Test the reload method."""
        obj = BaseModel()
        self.storage.new(obj)

        self.storage.save()

        self.storage._FileStorage__objects.clear()
        self.storage.reload()

        self.assertIn(f"{type(obj).__name__}.{obj.id}", self.storage.all())

    def test_invalid_json(self):
        """Test invalid json file"""
        with open(self.storage._FileStorage__file_path, 'w') as f:
            f.write("Invalid JSON file")

        self.storage.reload()
        actual = self.storage.all()
        self.assertEqual(actual, {})


if __name__ == '__main__':
    unittest.main()
