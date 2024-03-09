#!/usr/bin/python3
"""defining TestCity class"""
import unittest
from models.city import City
from models.base_model import BaseModel

class TestCity(unittest.TestCase):
    """unittests various user methods"""

    def test_city_inst_creation(self):
        city_inst = City()
        self.assertIsInstance(city_inst, City)

    def test_city_attributes(self):
        city_inst = City()
        self.assertEqual(city_inst.name, "")

    def test_city_inheritance(self):
        city_inst = City()
        self.assertIsInstance(city_inst, BaseModel)

    def test_city_to_dict_method(self):
        city_inst = City()
        city_dict = city_inst.to_dict()

        expected_keys = set(['id', 'created_at', 'updated_at', 'city_id', 'name'])
        actual_keys = set(city_dict.keys())

    def test_city_str_representation(self):
        city_inst = City()
        city_str = str(city_inst)

        self.assertTrue(city_str.startswith("[City] ("))
        self.assertIn(city_inst.id, city_str)
        self.assertIn("{", city_str)
        self.assertIn("}", city_str)

    def test_city_save_method(self):
        city_inst = City()
        initl_upd_at = city_inst.updated_at
        city_inst.save()
        self.assertNotEqual(initl_upd_at, city_inst.updated_at)



if __name__ == '__main__':
    unittest.main()
