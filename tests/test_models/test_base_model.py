#!/usr/bin/python3
"""Unittest for BaseModel class"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def setUp(self):
        """Sets up BaseModel for testing"""
        self.bm = BaseModel()

    def tearDown(self):
        """Tears down BaseModel testing"""
        del self.bm

    def test_instance(self):
        """Tests BaseModel instance"""
        self.assertIsInstance(self.bm, BaseModel)

    def test_id(self):
        """Tests id attribute"""
        self.assertTrue(hasattr(self.bm, "id"))
        self.assertIsInstance(self.bm.id, str)

    def test_created_at(self):
        """Tests created_at attribute"""
        self.assertTrue(hasattr(self.bm, "created_at"))
        self.assertEqual(type(self.bm.created_at).__name__, "datetime")

    def test_updated_at(self):
        """Tests updated_at attribute"""
        self.assertTrue(hasattr(self.bm, "updated_at"))
        self.assertEqual(type(self.bm.updated_at).__name__, "datetime")

    def test_save(self):
        """Tests save method"""
        self.bm.save()
        self.assertNotEqual(self.bm.created_at, self.bm.updated_at)

    def test_str(self):
        """Tests __str__ method"""
        bm_str = self.bm.__str__()
        self.assertEqual(bm_str,
                         f"[BaseModel] ({self.bm.id}) {self.bm.__dict__}")

    def test_to_dict(self):
        """Tests to_dict method"""
        bm_dict = self.bm.to_dict()
        self.assertEqual(bm_dict["__class__"], "BaseModel")
        self.assertEqual(type(bm_dict["created_at"]), str)
        self.assertEqual(type(bm_dict["updated_at"]), str)

    def test_init_from_dict(self):
        """Tests init from dictionary"""
        bm_dict = self.bm.to_dict()
        bm2 = BaseModel(**bm_dict)
        self.assertEqual(self.bm.id, bm2.id)
        self.assertEqual(self.bm.created_at, bm2.created_at)
        self.assertEqual(self.bm.updated_at, bm2.updated_at)
        self.assertEqual(self.bm.__dict__, bm2.__dict__)
