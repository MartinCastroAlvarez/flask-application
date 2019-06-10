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


class TestAlias(unittest.TestCase):
    """
    Testing Alias class.
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
        # Creating Alias.
        a1 = Alias()
        a1.person_id = p1.id
        a1.value = Random.get_str(10)
        self.session.add(a1)
        self.session.commit()
        self.assertTrue(a1.id)
        self.assertIsInstance(a1.id, int)
        # Searching by value.
        a2 = self.session.query(Alias).filter_by(value=a1.value).first()
        self.assertTrue(a2)
        self.assertEqual(a2.id, a1.id)
        # Searching by person ID.
        a3 = self.session.query(Alias).filter_by(person_id=p1.id).first()
        self.assertTrue(a3)
        self.assertEqual(a3.id, a1.id)

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
        # Creating Alias.
        a1 = Alias()
        a1.person_id = p1.id
        a1.value = Random.get_str(10)
        self.session.add(a1)
        self.session.commit()
        # Searching by value.
        a2 = self.session.query(Alias).filter_by(value=a1.value).first()
        self.assertTrue(a2)
        self.assertEqual(a2.id, a1.id)
        # Deleting alias.
        self.session.delete(a2)
        self.session.commit()
        # Searching by value.
        a2 = self.session.query(Alias).filter_by(value=a1.value).first()
        self.assertFalse(a2)

    def test_value(self) -> None:
        """
        Test model last name.
        """
        a1 = Alias()
        with self.assertRaises(ValueError):
            a1.value = None
        with self.assertRaises(ValueError):
            a1.value = Random.get_int()
        with self.assertRaises(ValueError):
            a1.value = Random.get_float()
        with self.assertRaises(ValueError):
            a1.value = Random.get_str(size=1)
        with self.assertRaises(ValueError):
            a1.value = Random.get_str(size=2)
        with self.assertRaises(ValueError):
            a1.value = Random.get_str(size=2000)

    def test_update(self) -> None:
        """
        Test model update.
        """
        # Creating person.
        p1 = Person()
        p1.first_name = Random.get_str(size=10)
        p1.last_name = Random.get_str(size=10)
        self.session.add(p1)
        self.session.commit()
        # Creating Alias.
        a1 = Alias()
        a1.person_id = p1.id
        a1.value = Random.get_str(10)
        a1_value = a1.value
        self.session.add(a1)
        self.session.commit()
        # Updating alias.
        a1.value = Random.get_str(10)
        a2_value = a1.value
        self.session.add(a1)
        self.session.commit()
        # Searching by value.
        a2 = self.session.query(Alias).filter_by(value=a1_value).first()
        self.assertFalse(a2)
        a3 = self.session.query(Alias).filter_by(value=a2_value).first()
        self.assertTrue(a3)
        self.assertEqual(a3.id, a1.id)

    def test_created_at(self) -> None:
        """
        Test model created at.
        """
        # Creating person.
        p1 = Person()
        p1.first_name = Random.get_str(size=10)
        p1.last_name = Random.get_str(size=10)
        self.session.add(p1)
        self.session.commit()
        # Creating Alias.
        a1 = Alias()
        a1.person_id = p1.id
        a1.value = Random.get_str(10)
        a1_value = a1.value
        self.session.add(a1)
        self.session.commit()
        # Validating created at.
        self.assertTrue(a1.created_at)
        self.assertIsInstance(a1.created_at.year, int)
        self.assertIsInstance(a1.created_at.month, int)
        self.assertIsInstance(a1.created_at.day, int)

    def test_to_str(self) -> None:
        """
        Test model string serializer.
        """
        p1 = Alias()
        print(p1)  # Should NOT fail.
