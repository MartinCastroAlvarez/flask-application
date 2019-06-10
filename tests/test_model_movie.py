"""
Testing app.api.controller.models.movie library.

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


class TestMovie(unittest.TestCase):
    """
    Testing Movie class.
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
        p1 = Movie()
        p1.title = Random.get_str(size=10)
        p1.released_at = Random.get_date(start="1992-10-10")
        self.session.add(p1)
        self.session.commit()
        self.assertTrue(p1.id)
        self.assertIsInstance(p1.id, int)
        # Searching by title.
        p2 = self.session.query(Movie).filter_by(title=p1.title).first()
        self.assertTrue(p2)
        self.assertEqual(p2.id, p1.id)
        # Searching by released at.
        p3 = self.session.query(Movie).filter_by(released_at=p1.released_at).first()
        self.assertTrue(p3)
        self.assertEqual(p3.id, p1.id)

    def test_update(self) -> None:
        """
        Test model update.
        """
        # Creating person.
        p1 = Movie()
        p1.title = Random.get_str(size=10)
        p1.released_at = Random.get_date(start="1992-10-10")
        p1.is_active = Random.get_bool()
        title_1 = p1.title
        released_at_1 = p1.released_at
        self.session.add(p1)
        self.session.commit()
        # Searching by title.
        p2 = self.session.query(Movie).filter_by(title=p1.title).first()
        self.assertTrue(p2)
        self.assertEqual(p2.id, p1.id)
        # Searching by released at.
        p3 = self.session.query(Movie).filter_by(released_at=p1.released_at).first()
        self.assertTrue(p3)
        self.assertEqual(p3.id, p1.id)
        # Updating person.
        p1.title = Random.get_str(size=10)
        p1.released_at = Random.get_date(start="1992-10-10")
        p1.is_active = Random.get_bool()
        title_2 = p1.title
        released_at_2 = p1.released_at
        self.session.add(p1)
        self.session.commit()
        self.assertNotEqual(title_1, title_2)
        self.assertNotEqual(released_at_1, released_at_2)
        # Searching by title.
        p4 = self.session.query(Movie).filter_by(title=title_1).first()
        self.assertFalse(p4)
        p5 = self.session.query(Movie).filter_by(title=title_2).first()
        self.assertTrue(p5)

    def test_delete(self) -> None:
        """
        Test model deletion.
        """
        # Creating person.
        p1 = Movie()
        p1.title = Random.get_str(size=10)
        p1.released_at = Random.get_date(start="1992-10-10")
        self.session.add(p1)
        self.session.commit()
        # Searching by title.
        p2 = self.session.query(Movie).filter_by(title=p1.title).first()
        self.assertTrue(p2)
        self.assertEqual(p2.id, p1.id)
        # Deleting person.
        self.session.delete(p1)
        self.session.commit()
        p3 = self.session.query(Movie).filter_by(released_at=p1.released_at).first()
        self.assertFalse(p3)

    def test_title(self) -> None:
        """
        Test model title.
        """
        p1 = Movie()
        with self.assertRaises(ValueError):
            p1.title = None
        with self.assertRaises(ValueError):
            p1.title = Random.get_int()
        with self.assertRaises(ValueError):
            p1.title = Random.get_float()
        with self.assertRaises(ValueError):
            p1.title = Random.get_str(size=1)
        with self.assertRaises(ValueError):
            p1.title = Random.get_str(size=2)
        with self.assertRaises(ValueError):
            p1.title = Random.get_str(size=2000)

    def test_created_at(self) -> None:
        """
        Test model created at.
        """
        p1 = Movie()
        p1.title = Random.get_str(size=10)
        p1.released_at = Random.get_date(start="1992-10-10")
        p1.is_active = Random.get_bool()
        self.session.add(p1)
        self.session.commit()
        self.assertTrue(p1.created_at)
        self.assertIsInstance(p1.created_at.year, int)
        self.assertIsInstance(p1.created_at.month, int)
        self.assertIsInstance(p1.created_at.day, int)

    def test_released_at(self) -> None:
        """
        Test model released at.
        """
        p1 = Movie()
        p1.released_at = Random.get_date(start="1992-10-10")
        self.assertTrue(p1.released_at)
        self.assertEqual(p1.released_at.year, p1.release_year)
        self.assertIsInstance(p1.released_at.year, int)
        self.assertIsInstance(p1.released_at.month, int)
        self.assertIsInstance(p1.released_at.day, int)

    def test_roman_year(self) -> None:
        """
        Test model roman year.
        """
        p1 = Movie()
        p1.released_at = Random.get_date("2000-01-01", "2000-12-31")
        self.assertEqual(p1.release_roman, "MM")
        p1.released_at = Random.get_date("1999-01-01", "1999-12-31")
        self.assertEqual(p1.release_roman, "MCMXCIX")
        with self.assertRaises(ValueError):
            p1.released_at = Random.get_date("4005-01-01", "4005-12-31")
            self.assertEqual(p1.release_roman, "MCMXCIX")

    def test_to_str(self) -> None:
        """
        Test model string serializer.
        """
        p1 = Movie()
        print(p1)  # Should NOT fail.
