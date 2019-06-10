"""
Testing app.api.controller.models.person library.

Reference:
https://stackoverflow.com/questions/14719507
"""

import unittest

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from app.api.controller.models.person import Person, Alias
from app.api.controller.models.movie import Movie
from app.api.controller.models.role import Actor, Director, Producer

from .utils.random import Random


class TestPerson(unittest.TestCase):
    """
    Testing Person class.
    """

    def setUp(self) -> None:
        """
        Mocking database before test.
        """
        self.engine = create_engine('sqlite:///:memory:')
        self.session = sessionmaker(bind=self.engine)()
        Person.metadata.create_all(self.engine)
        Alias.metadata.create_all(self.engine)
        Producer.metadata.create_all(self.engine)
        Director.metadata.create_all(self.engine)
        Movie.metadata.create_all(self.engine)

    def tearDown(self) -> None:
        """
        Deleting all objects after test.
        """
        Person.metadata.drop_all(self.engine)
        Alias.metadata.drop_all(self.engine)
        Producer.metadata.drop_all(self.engine)
        Director.metadata.drop_all(self.engine)
        Movie.metadata.drop_all(self.engine)

    def test_create(self) -> None:
        """
        Test model creation.
        """
        # Creating person.
        p1 = Person()
        p1.first_name = Random.get_str(size=10)
        p1.last_name = Random.get_str(size=10)
        self.session.add(p1)
        self.session.commit()
        self.assertTrue(p1.id)
        self.assertIsInstance(p1.id, int)
        # Searching by first name.
        p2 = self.session.query(Person).filter_by(first_name=p1.first_name).first()
        self.assertTrue(p2)
        self.assertEqual(p2.id, p1.id)
        # Searching by last name.
        p3 = self.session.query(Person).filter_by(last_name=p1.last_name).first()
        self.assertTrue(p3)
        self.assertEqual(p3.id, p1.id)

    def test_update(self) -> None:
        """
        Test model update.
        """
        # Creating person.
        p1 = Person()
        p1.first_name = Random.get_str(size=10)
        p1.last_name = Random.get_str(size=10)
        p1.is_active = Random.get_bool()
        first_name_1 = p1.first_name
        last_name_1 = p1.last_name
        self.session.add(p1)
        self.session.commit()
        # Searching by first name.
        p2 = self.session.query(Person).filter_by(first_name=p1.first_name).first()
        self.assertTrue(p2)
        self.assertEqual(p2.id, p1.id)
        # Searching by last name.
        p3 = self.session.query(Person).filter_by(last_name=p1.last_name).first()
        self.assertTrue(p3)
        self.assertEqual(p3.id, p1.id)
        # Updating person.
        p1.first_name = Random.get_str(size=10)
        p1.last_name = Random.get_str(size=10)
        p1.is_active = Random.get_bool()
        first_name_2 = p1.first_name
        last_name_2 = p1.last_name
        self.session.add(p1)
        self.session.commit()
        self.assertNotEqual(first_name_1, first_name_2)
        self.assertNotEqual(last_name_1, last_name_2)
        # Searching by first name.
        p4 = self.session.query(Person).filter_by(first_name=first_name_1).first()
        self.assertFalse(p4)
        p5 = self.session.query(Person).filter_by(first_name=first_name_2).first()
        self.assertTrue(p5)

    def test_delete(self) -> None:
        """
        Test model deletion.
        """
        # Creating person.
        p1 = Person()
        p1.first_name = Random.get_str(size=10)
        p1.last_name = Random.get_str(size=10)
        self.session.add(p1)
        self.session.commit()
        # Searching by first name.
        p2 = self.session.query(Person).filter_by(first_name=p1.first_name).first()
        self.assertTrue(p2)
        self.assertEqual(p2.id, p1.id)
        # Deleting person.
        self.session.delete(p1)
        self.session.commit()
        p3 = self.session.query(Person).filter_by(last_name=p1.last_name).first()
        self.assertFalse(p3)

    def test_first_name(self) -> None:
        """
        Test model first name.
        """
        p1 = Person()
        with self.assertRaises(ValueError):
            p1.first_name = None
        with self.assertRaises(ValueError):
            p1.first_name = Random.get_int()
        with self.assertRaises(ValueError):
            p1.first_name = Random.get_float()
        with self.assertRaises(ValueError):
            p1.first_name = Random.get_str(size=1)
        with self.assertRaises(ValueError):
            p1.first_name = Random.get_str(size=2)
        with self.assertRaises(ValueError):
            p1.first_name = Random.get_str(size=2000)

    def test_last_name(self) -> None:
        """
        Test model last name.
        """
        p1 = Person()
        with self.assertRaises(ValueError):
            p1.last_name = None
        with self.assertRaises(ValueError):
            p1.last_name = Random.get_int()
        with self.assertRaises(ValueError):
            p1.last_name = Random.get_float()
        with self.assertRaises(ValueError):
            p1.last_name = Random.get_str(size=1)
        with self.assertRaises(ValueError):
            p1.last_name = Random.get_str(size=2)
        with self.assertRaises(ValueError):
            p1.last_name = Random.get_str(size=5000)

    def test_created_at(self) -> None:
        """
        Test model created at.
        """
        p1 = Person()
        p1.first_name = Random.get_str(size=10)
        p1.last_name = Random.get_str(size=10)
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
        p1 = Person()
        print(p1)  # Should NOT fail.
