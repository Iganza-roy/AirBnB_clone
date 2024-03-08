#!/usr/bin/python3
"""defining TestUser class"""
import unittest
from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    """unittests various user methods"""

    def test_user_inst_creation(self):
        user_inst = User()
        self.assertIsInstance(user_inst, User)

    def test_user_attributes(self):
        user_inst = User()
        self.assertEqual(user_inst.email, "")
        self.assertEqual(user_inst.password, "")
        self.assertEqual(user_inst.first_name, "")
        self.assertEqual(user_inst.last_name, "")

    def test_user_inheritance(self):
        user_inst = User()
        self.assertIsInstance(user_inst, BaseModel)

    def test_user_to_dict_method(self):
        user_inst = User()
        user_dict = user_inst.to_dict()

        expected_keys = set(['id', 'created_at', 'updated_at', 'email', 'password', 'first_name', 'last_name'])
        actual_keys = set(user_dict.keys())

    def test_user_str_representation(self):
        user_inst = User()
        user_str = str(user_inst)

        self.assertTrue(user_str.startswith("[User] ("))
        self.assertIn(user_inst.id, user_str)
        self.assertIn("{", user_str)
        self.assertIn("}", user_str)

    def test_user_save_method(self):
        user_inst = User()
        initl_upd_at = user_inst.updated_at
        user_inst.save()
        self.assertNotEqual(initl_upd_at, user_inst.updated_at)



if __name__ == '__main__':
    unittest.main()
