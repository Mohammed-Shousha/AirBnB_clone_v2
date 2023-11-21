#!/usr/bin/python3
"""Unittest for Place class"""

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for TestPlace Class"""

    def setUp(self):
        """Sets up Place for testing"""
        self.place = Place()

    def tearDown(self):
        """Tears down Place testing"""
        del self.place

    def test_place_instance(self):
        """Tests place instance"""
        self.assertIsInstance(self.place, Place)

    def test_place_city_id(self):
        """Tests place city_id"""
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertEqual(type(self.place.city_id), str)
        self.assertEqual(self.place.city_id, "")

    def test_place_user_id(self):
        """Tests place user_id"""
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertEqual(type(self.place.user_id), str)
        self.assertEqual(self.place.user_id, "")

    def test_place_name(self):
        """Tests place name"""
        self.assertTrue(hasattr(self.place, "name"))
        self.assertEqual(type(self.place.name), str)
        self.assertEqual(self.place.name, "")

    def test_place_description(self):
        """Tests place description"""
        self.assertTrue(hasattr(self.place, "description"))
        self.assertEqual(type(self.place.description), str)
        self.assertEqual(self.place.description, "")

    def test_place_number_rooms(self):
        """Tests place number_rooms"""
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertEqual(type(self.place.number_rooms), int)
        self.assertEqual(self.place.number_rooms, 0)

    def test_place_number_bathrooms(self):
        """Tests place number_bathrooms"""
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertEqual(type(self.place.number_bathrooms), int)
        self.assertEqual(self.place.number_bathrooms, 0)

    def test_place_max_guest(self):
        """Tests place max_guest"""
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertEqual(type(self.place.max_guest), int)
        self.assertEqual(self.place.max_guest, 0)

    def test_place_price_by_night(self):
        """Tests place price_by_night"""
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertEqual(type(self.place.price_by_night), int)
        self.assertEqual(self.place.price_by_night, 0)

    def test_place_latitude(self):
        """Tests place latitude"""
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertEqual(type(self.place.latitude), float)
        self.assertEqual(self.place.latitude, 0.0)

    def test_place_longitude(self):
        """Tests place longitude"""
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertEqual(type(self.place.longitude), float)
        self.assertEqual(self.place.longitude, 0.0)

    def test_place_amenity_ids(self):
        """Tests place amenity_ids"""
        self.assertTrue(hasattr(self.place, "amenity_ids"))
        self.assertEqual(type(self.place.amenity_ids), list)
        self.assertEqual(self.place.amenity_ids, [])

    def test_place_id(self):
        """Tests place id"""
        self.assertTrue(hasattr(self.place, "id"))
        self.assertEqual(type(self.place.id), str)

    def test_place_created_at(self):
        """Tests place created_at"""
        self.assertTrue(hasattr(self.place, "created_at"))
        self.assertEqual(type(self.place.created_at).__name__, "datetime")

    def test_place_updated_at(self):
        """Tests place updated_at"""
        self.assertTrue(hasattr(self.place, "updated_at"))
        self.assertEqual(type(self.place.updated_at).__name__, "datetime")

    def test_place_str(self):
        """Tests place __str__"""
        self.assertEqual(type(self.place.__str__()), str)

    def test_place_save(self):
        """Tests place save"""
        self.place.save()
        self.assertEqual(type(self.place.updated_at).__name__, "datetime")

    def test_place_to_dict(self):
        """Tests place to_dict"""
        self.assertEqual(type(self.place.to_dict()), dict)

    def test_place_kwargs(self):
        """Tests place kwargs"""
        new_place = Place(name="New Place")
        self.assertEqual(type(new_place).__name__, "Place")
        self.assertTrue(hasattr(new_place, "name"))
        self.assertEqual(new_place.name, "New Place")
