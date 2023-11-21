#!/usr/bin/python3
"""Unittest for City class"""

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for TestCity Class"""

    def setUp(self):
        """Sets up City for testing"""
        self.city = City()

    def tearDown(self):
        """Tears down City testing"""
        del self.city

    def test_city_instance(self):
        """Tests city instance"""
        self.assertIsInstance(self.city, City)

    def test_city_name(self):
        """Tests city name"""
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(self.city.name, "")

    def test_city_state_id(self):
        """Tests city state_id"""
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertEqual(type(self.city.state_id), str)
        self.assertEqual(self.city.state_id, "")

    def test_city_id(self):
        """Tests city id"""
        self.assertTrue(hasattr(self.city, "id"))
        self.assertEqual(type(self.city.id), str)

    def test_city_created_at(self):
        """Tests city created_at"""
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertEqual(type(self.city.created_at).__name__, "datetime")

    def test_city_updated_at(self):
        """Tests city updated_at"""
        self.assertTrue(hasattr(self.city, "updated_at"))
        self.assertEqual(type(self.city.updated_at).__name__, "datetime")

    def test_city_str(self):
        """Tests city __str__"""
        self.assertEqual(type(self.city.__str__()), str)

    def test_city_save(self):
        """Tests city save"""
        self.city.save()
        self.assertEqual(type(self.city.updated_at).__name__, "datetime")

    def test_city_to_dict(self):
        """Tests city to_dict"""
        self.assertEqual(type(self.city.to_dict()), dict)

    def test_city_kwargs(self):
        """Tests city kwargs"""
        new_city = City(name="New Cairo")
        self.assertEqual(type(new_city).__name__, "City")
        self.assertTrue(hasattr(new_city, "name"))
        self.assertEqual(new_city.name, "New Cairo")
