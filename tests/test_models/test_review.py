#!/usr/bin/python3
"""defining TestReview class"""
import unittest
from models.review import Review
from models.base_model import BaseModel

class TestReview(unittest.TestCase):
    """unittests various user methods"""

    def test_review_inst_creation(self):
        review_inst = Review()
        self.assertIsInstance(review_inst, Review)

    def test_review_attributes(self):
        review_inst = Review()
        self.assertEqual(review_inst.place_id, "")
        self.assertEqual(review_inst.user_id, "")
        self.assertEqual(review_inst.text, "")

    def test_review_inheritance(self):
        review_inst = Review()
        self.assertIsInstance(review_inst, BaseModel)

    def test_review_to_dict_method(self):
        review_inst = Review()
        review_dict = review_inst.to_dict()

        expected_keys = set([
            'id', 'created_at', 'updated_at', 'place_id', 'user_id', 'text'
        ])
        actual_keys = set(review_dict.keys())

    def test_review_str_representation(self):
        review_inst = Review()
        review_str = str(review_inst)

        self.assertTrue(review_str.startswith("[Review] ("))
        self.assertIn(review_inst.id, review_str)
        self.assertIn("{", review_str)
        self.assertIn("}", review_str)

    def test_review_save_method(self):
        review_inst = Review()
        initl_upd_at = review_inst.updated_at
        review_inst.save()
        self.assertNotEqual(initl_upd_at, review_inst.updated_at)



if __name__ == '__main__':
    unittest.main()
