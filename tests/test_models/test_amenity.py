#!/usr/bin/python3
"""Unittest for Amenity class"""

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for TestAmenity Class"""

    def setUp(self):
        """Sets up Amenity for testing"""
        self.amenity = Amenity()

    def tearDown(self):
        """Tears down Amenity testing"""
        del self.amenity

    def test_amenity_instance(self):
        """Tests amenity instance"""
        self.assertIsInstance(self.amenity, Amenity)

    def test_amenity_name(self):
        """Tests amenity name"""
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(type(self.amenity.name), str)
        self.assertEqual(self.amenity.name, "")

    def test_amenity_id(self):
        """Tests amenity id"""
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertEqual(type(self.amenity.id), str)

    def test_amenity_created_at(self):
        """Tests amenity created_at"""
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertEqual(type(self.amenity.created_at).__name__, "datetime")

    def test_amenity_updated_at(self):
        """Tests amenity updated_at"""
        self.assertTrue(hasattr(self.amenity, "updated_at"))
        self.assertEqual(type(self.amenity.updated_at).__name__, "datetime")

    def test_amenity_str(self):
        """Tests amenity __str__"""
        self.assertEqual(type(self.amenity.__str__()), str)

    def test_amenity_save(self):
        """Tests amenity save"""
        self.amenity.save()
        self.assertEqual(type(self.amenity.updated_at).__name__, "datetime")

    def test_amenity_to_dict(self):
        """Tests amenity to_dict"""
        self.assertEqual(type(self.amenity.to_dict()), dict)

    def test_amenity_kwargs(self):
        """Tests amenity kwargs"""
        self.new_amenity = Amenity(name="Free Wifi")
        self.assertEqual(type(self.new_amenity).__name__, "Amenity")
        self.assertTrue(hasattr(self.new_amenity, "name"))
        self.assertEqual(self.new_amenity.name, "Free Wifi")
