#!/usr/bin/python3
"""defining TestState class"""
import unittest
from models.state import State
from models.base_model import BaseModel

class TestState(unittest.TestCase):
    """unittests various user methods"""

    def test_state_inst_creation(self):
        state_inst = State()
        self.assertIsInstance(state_inst, State)

    def test_state_attributes(self):
        state_inst = State()
        self.assertEqual(state_inst.name, "")

    def test_state_inheritance(self):
        state_inst = State()
        self.assertIsInstance(state_inst, BaseModel)

    def test_state_to_dict_method(self):
        state_inst = State()
        state_dict = state_inst.to_dict()

        expected_keys = set(['id', 'created_at', 'updated_at', 'name'])
        actual_keys = set(state_dict.keys())

    def test_state_str_representation(self):
        state_inst = State()
        state_str = str(state_inst)

        self.assertTrue(state_str.startswith("[State] ("))
        self.assertIn(state_inst.id, state_str)
        self.assertIn("{", state_str)
        self.assertIn("}", state_str)

    def test_state_save_method(self):
        state_inst = State()
        initl_upd_at = state_inst.updated_at
        state_inst.save()
        self.assertNotEqual(initl_upd_at, state_inst.updated_at)



if __name__ == '__main__':
    unittest.main()
