#!/usr/bin/python3
"""Unittest for User class"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for TestUser Class"""

    def setUp(self):
        """Sets up User for testing"""
        self.user = User()
        self.user.first_name = "Adel"
        self.user.last_name = "Amin"
        self.user.email = "email@test.com"
        self.user.password = "password"

    def test_user_instance(self):
        """Tests user instance"""
        self.assertIsInstance(self.user, User)

    def test_user_email(self):
        """Tests user type"""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(self.user.email, "email@test.com")

    def test_user_password(self):
        """Tests user password"""
        self.assertTrue(hasattr(self.user, "password"))
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(self.user.password, "password")

    def test_user_first_name(self):
        """Tests user first_name"""
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(self.user.first_name, "Adel")

    def test_user_last_name(self):
        """Tests user last_name"""
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertEqual(type(self.user.last_name), str)
        self.assertEqual(self.user.last_name, "Amin")

    def test_user_id(self):
        """Tests user id"""
        self.assertTrue(hasattr(self.user, "id"))
        self.assertEqual(type(self.user.id), str)

    def test_user_created_at(self):
        """Tests user created_at"""
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertEqual(type(self.user.created_at).__name__, "datetime")

    def test_user_updated_at(self):
        """Tests user updated_at"""
        self.assertTrue(hasattr(self.user, "updated_at"))
        self.assertEqual(type(self.user.updated_at).__name__, "datetime")

    def test_user_str(self):
        """Tests user __str__"""
        self.assertEqual(type(self.user.__str__()), str)

    def test_user_save(self):
        """Tests user save"""
        self.user.save()
        self.assertEqual(type(self.user.updated_at).__name__, "datetime")

    def test_user_to_dict(self):
        """Tests user to_dict"""
        self.assertEqual(type(self.user.to_dict()), dict)

    def test_kwargs(self):
        """Tests user kwargs"""
        new_user = User(**self.user.to_dict())
        self.assertEqual(self.user.id, new_user.id)
        self.assertEqual(self.user.created_at, new_user.created_at)
        self.assertEqual(self.user.updated_at, new_user.updated_at)
        self.assertNotEqual(self.user, new_user)
