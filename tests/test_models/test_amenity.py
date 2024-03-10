#!/usr/bin/python3
"""defining TestAmenity class"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from models import storage
from datetime import datetime, timedelta


class TestAmenity(unittest.TestCase):
    """unittests various user methods"""

    def test_amenity_inst_creation(self):
        amenity_inst = Amenity()
        self.assertIsInstance(amenity_inst, Amenity)

    def test_amenity_attributes(self):
        amenity_inst = Amenity()
        self.assertEqual(amenity_inst.name, "")

    def test_amenity_inheritance(self):
        amenity_inst = Amenity()
        self.assertIsInstance(amenity_inst, BaseModel)

    def test_amenity_to_dict_method(self):
        amenity_inst = Amenity()
        amenity_dict = amenity_inst.to_dict()

        expected_keys = set(['id', 'created_at', 'updated_at', 'name'])
        actual_keys = set(amenity_dict.keys())

    def test_amenity_str_representation(self):
        amenity_inst = Amenity()
        amenity_str = str(amenity_inst)

        self.assertTrue(amenity_str.startswith("[Amenity] ("))
        self.assertIn(amenity_inst.id, amenity_str)
        self.assertIn("{", amenity_str)
        self.assertIn("}", amenity_str)

    def test_amenity_save_method(self):
        amenity_inst = Amenity()
        initl_upd_at = amenity_inst.updated_at
        amenity_inst.save()
        second_amenity = Amenity(id=amenity_inst.id)
        storage.reload()
        self.assertNotEqual(initl_upd_at, second_amenity.updated_at)
        time_difference = abs(second_amenity.updated_at - initl_upd_at)
        tolerance = timedelta(seconds=1)
        self.assertLessEqual(time_difference, tolerance)

    def test_amenity_additional_attributes(self):
        amenity_inst = Amenity()
        amenity_inst.custom_attribute = "Custom Value"
        amenity_inst.save()
        amenity_dict = amenity_inst.to_dict()
        self.assertIn('custom_attribute', amenity_dict)

    def test_amenity_save_with_arg(self):
        amenity_inst = Amenity()
        with self.assertRaises(TypeError):
            amenity_inst.save(None)

    def test_amenity_save_updates_file(self):
        amenity_inst = Amenity()
        amenity_inst.save()
        amenity_id = "Amenity." + amenity_inst.id
        with open("file.json", "r") as f:
            self.assertIn(amenity_id, f.read())

        second_amenity = Amenity()
        second_amenity.save()
        with open("file.json", "r") as f:
            file_content = f.read()
            self.assertIn(amenity_id, file_content)
            self.assertIn("Amenity." + second_amenity.id, file_content)


if __name__ == '__main__':
    unittest.main()
