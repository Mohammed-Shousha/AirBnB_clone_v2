#!/usr/bin/python3
"""Unittest for Review class"""

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for TestReview Class"""

    def setUp(self):
        """Sets up Review for testing"""
        self.review = Review()

    def tearDown(self):
        """Tears down Review testing"""
        del self.review

    def test_review_instance(self):
        """Tests review instance"""
        self.assertIsInstance(self.review, Review)

    def test_review_place_id(self):
        """Tests review place_id"""
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertEqual(type(self.review.place_id), str)
        self.assertEqual(self.review.place_id, "")

    def test_review_user_id(self):
        """Tests review user_id"""
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertEqual(type(self.review.user_id), str)
        self.assertEqual(self.review.user_id, "")

    def test_review_text(self):
        """Tests review text"""
        self.assertTrue(hasattr(self.review, "text"))
        self.assertEqual(type(self.review.text), str)
        self.assertEqual(self.review.text, "")

    def test_review_id(self):
        """Tests review id"""
        self.assertTrue(hasattr(self.review, "id"))
        self.assertEqual(type(self.review.id), str)

    def test_review_created_at(self):
        """Tests review created_at"""
        self.assertTrue(hasattr(self.review, "created_at"))
        self.assertEqual(type(self.review.created_at).__name__, "datetime")

    def test_review_updated_at(self):
        """Tests review updated_at"""
        self.assertTrue(hasattr(self.review, "updated_at"))
        self.assertEqual(type(self.review.updated_at).__name__, "datetime")

    def test_review_str(self):
        """Tests review __str__"""
        self.assertEqual(type(self.review.__str__()), str)

    def test_review_save(self):
        """Tests review save"""
        self.review.save()
        self.assertEqual(type(self.review.updated_at).__name__, "datetime")

    def test_review_to_dict(self):
        """Tests review to_dict"""
        self.assertEqual(type(self.review.to_dict()), dict)

    def test_review_kwargs(self):
        """Tests review kwargs"""
        new_review = Review(name="New Cairo")
        self.assertEqual(type(new_review).__name__, "Review")
        self.assertTrue(hasattr(new_review, "name"))
        self.assertEqual(new_review.name, "New Cairo")
