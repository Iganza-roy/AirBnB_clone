#!/usr/bin/python3
"""defining TestPlace class"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """unittests various place methods"""

    def test_place_inst_creation(self):
        place_inst = Place()
        self.assertIsInstance(place_inst, Place)

    def test_place_attributes(self):
        place_inst = Place()
        self.assertEqual(place_inst.city_id, "")
        self.assertEqual(place_inst.user_id, "")
        self.assertEqual(place_inst.name, "")
        self.assertEqual(place_inst.description, "")
        self.assertEqual(place_inst.number_rooms, 0)
        self.assertEqual(place_inst.number_bathrooms, 0)
        self.assertEqual(place_inst.max_guest, 0)
        self.assertEqual(place_inst.price_by_night, 0)
        self.assertEqual(place_inst.latitude, 0.0)
        self.assertEqual(place_inst.longitude, 0.0)
        self.assertEqual(place_inst.amenity_ids, [])

    def test_place_inheritance(self):
        place_inst = Place()
        self.assertIsInstance(place_inst, BaseModel)

    def test_place_to_dict_method(self):
        place_inst = Place()
        place_dict = place_inst.to_dict()

        expected_keys = set([
            'id', 'created_at', 'updated_at', 'city_id',
            'user_id', 'name', 'description', 'number_rooms',
            'number_bathrooms', 'max_guest', 'price_by_night', 'latitude',
            'longitude', 'amenity_ids'
        ])
        actual_keys = set(place_dict.keys())

    def test_place_str_representation(self):
        place_inst = Place()
        place_str = str(place_inst)

        self.assertTrue(place_str.startswith("[Place] ("))
        self.assertIn(place_inst.id, place_str)
        self.assertIn("{", place_str)
        self.assertIn("}", place_str)

    def test_place_save_method(self):
        place_inst = Place()
        initl_upd_at = place_inst.updated_at
        place_inst.save()
        self.assertNotEqual(initl_upd_at, place_inst.updated_at)


if __name__ == '__main__':
    unittest.main()
