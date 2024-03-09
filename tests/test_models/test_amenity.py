#!/usr/bin/python3
"""defining TestAmenity class"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel

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
        self.assertNotEqual(initl_upd_at, amenity_inst.updated_at)



if __name__ == '__main__':
    unittest.main()
