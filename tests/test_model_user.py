"""
Testing app.api.controller.models.user library.

Reference:
https://stackoverflow.com/questions/14719507
"""

import unittest

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from app.api.controller.models.user import User

from .utils.random import Random


class TestUser(unittest.TestCase):
    """
    Testing User class.
    """

    def setUp(self) -> None:
        """
        Mocking database before test.
        """
        self.engine = create_engine('sqlite:///:memory:')
        self.session = sessionmaker(bind=self.engine)()
        User.metadata.create_all(self.engine)

    def tearDown(self) -> None:
        """
        Deleting all objects after test.
        """
        User.metadata.drop_all(self.engine)

    def test_create(self) -> None:
        """
        Test model creation.
        """
        # Creating user.
        p1 = User()
        p1.username = Random.get_str(size=10)
        p1.password = Random.get_str(size=10)
        p1.is_active = Random.get_bool()
        self.session.add(p1)
        self.session.commit()
        self.assertTrue(p1.id)
        self.assertIsInstance(p1.id, int)
        # Searching by username.
        p2 = self.session.query(User).filter_by(username=p1.username).first()
        self.assertTrue(p2)
        self.assertEqual(p2.id, p1.id)

    def test_update(self) -> None:
        """
        Test model update.
        """
        # Creating person.
        p1 = User()
        p1.username = Random.get_str(size=10)
        p1.password = Random.get_str(size=10)
        p1.is_active = Random.get_bool()
        username_1 = p1.username
        self.session.add(p1)
        self.session.commit()
        # Searching by username.
        p2 = self.session.query(User).filter_by(username=p1.username).first()
        self.assertTrue(p2)
        self.assertEqual(p2.id, p1.id)
        # Updating person.
        p1.username = Random.get_str(size=10)
        p1.is_active = Random.get_bool()
        username_2 = p1.username
        self.session.add(p1)
        self.session.commit()
        self.assertNotEqual(username_1, username_2)
        # Searching by username.
        p4 = self.session.query(User).filter_by(username=username_1).first()
        self.assertFalse(p4)
        p5 = self.session.query(User).filter_by(username=username_2).first()
        self.assertTrue(p5)

    def test_delete(self) -> None:
        """
        Test model deletion.
        """
        # Creating person.
        p1 = User()
        p1.username = Random.get_str(size=10)
        p1.password = Random.get_str(size=10)
        self.session.add(p1)
        self.session.commit()
        # Searching by username.
        p2 = self.session.query(User).filter_by(username=p1.username).first()
        self.assertTrue(p2)
        self.assertEqual(p2.id, p1.id)
        # Deleting person.
        self.session.delete(p1)
        self.session.commit()
        p3 = self.session.query(User).filter_by(username=p1.username).first()
        self.assertFalse(p3)

    def test_username(self) -> None:
        """
        Test model user.
        """
        p1 = User()
        with self.assertRaises(ValueError):
            p1.username = None
        with self.assertRaises(ValueError):
            p1.username = Random.get_int()
        with self.assertRaises(ValueError):
            p1.username = Random.get_float()
        with self.assertRaises(ValueError):
            p1.username = Random.get_str(size=1)
        with self.assertRaises(ValueError):
            p1.username = Random.get_str(size=2)
        with self.assertRaises(ValueError):
            p1.username = Random.get_str(size=2000)

    def test_password(self) -> None:
        """
        Test model user.
        """
        p1 = User()
        with self.assertRaises(ValueError):
            p1.password = None
        with self.assertRaises(ValueError):
            p1.password = Random.get_int()
        with self.assertRaises(ValueError):
            p1.password = Random.get_float()
        with self.assertRaises(ValueError):
            p1.password = Random.get_str(size=1)
        with self.assertRaises(ValueError):
            p1.password = Random.get_str(size=2)
        with self.assertRaises(ValueError):
            p1.password = Random.get_str(size=2000)

    def test_created_at(self) -> None:
        """
        Test model created at.
        """
        p1 = User()
        p1.username = Random.get_str(size=10)
        p1.password = Random.get_str(size=10)
        p1.is_active = Random.get_bool()
        self.session.add(p1)
        self.session.commit()
        self.assertTrue(p1.created_at)
        self.assertIsInstance(p1.created_at.year, int)
        self.assertIsInstance(p1.created_at.month, int)
        self.assertIsInstance(p1.created_at.day, int)

    def test_to_str(self) -> None:
        """
        Test model string serializer.
        """
        p1 = User()
        print(p1)  # Should NOT fail.

    def test_password_hash(self) -> None:
        """
        Test model password hash.
        """
        password = Random.get_str(size=10)
        p1 = User()
        p1.username = Random.get_str(size=10)
        p1.password = password
        p1.is_active = Random.get_bool()
        self.assertNotEqual(p1.password, password)
        self.assertFalse(p1.is_password_valid(Random.get_str(size=12)))
        self.assertTrue(p1.is_password_valid(password))
        with self.assertRaises(TypeError):
            User._User__hash(Random.get_int())
        with self.assertRaises(ValueError):
            User._User__hash(None)

    def test_password_hash_arguments(self) -> None:
        """
        Test model password hash arguments.
        """
        p1 = User()
        with self.assertRaises(ValueError):
            p1.is_password_valid()
        with self.assertRaises(TypeError):
            p1.is_password_valid(Random.get_int())
        with self.assertRaises(TypeError):
            p1.is_password_valid(Random.get_float())
