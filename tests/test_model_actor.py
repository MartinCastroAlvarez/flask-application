"""
Testing app.api.controller.models.role library.

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


class TestActor(unittest.TestCase):
    """
    Testing Actor Role class.
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
        # Creating movie.
        m1 = Movie()
        m1.title = Random.get_str(size=10)
        m1.released_at = Random.get_date(start="1991-10-05")
        self.session.add(m1)
        self.session.commit()
        # Creating actor.
        r1 = Actor()
        r1.movie_id = m1.id
        r1.person_id = p1.id
        self.session.add(r1)
        self.session.commit()
        # Searching by person ID.
        r2 = self.session.query(Actor).filter_by(person_id=p1.id).first()
        self.assertTrue(r2.movie_id)
        self.assertEqual(r1.movie_id, r2.movie_id)
        self.assertEqual(r1.person_id, r2.person_id)
        # Searching by movie ID.
        r3 = self.session.query(Actor).filter_by(movie_id=m1.id).first()
        self.assertTrue(r3.movie_id)
        self.assertEqual(r1.movie_id, r3.movie_id)
        self.assertEqual(r1.person_id, r3.person_id)

    def test_delete(self) -> None:
        """
        Test model creation.
        """
        # Creating person.
        p1 = Person()
        p1.first_name = Random.get_str(size=10)
        p1.last_name = Random.get_str(size=10)
        self.session.add(p1)
        self.session.commit()
        # Creating movie.
        m1 = Movie()
        m1.title = Random.get_str(size=10)
        m1.released_at = Random.get_date(start="1991-10-05")
        self.session.add(m1)
        self.session.commit()
        # Creating actor.
        r1 = Actor()
        r1.movie_id = m1.id
        r1.person_id = p1.id
        self.session.add(r1)
        self.session.commit()
        # Deleting actor.
        self.session.delete(r1)
        self.session.commit()
        # Searching by person ID.
        r2 = self.session.query(Actor).filter_by(person_id=p1.id).first()
        self.assertFalse(r2)
        # Searching by movie ID.
        r3 = self.session.query(Actor).filter_by(movie_id=m1.id).first()
        self.assertFalse(r3)

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
        # Creating movie.
        m1 = Movie()
        m1.title = Random.get_str(size=10)
        m1.released_at = Random.get_date(start="1991-10-05")
        self.session.add(m1)
        self.session.commit()
        # Creating actor.
        r1 = Actor()
        r1.movie_id = m1.id
        r1.person_id = p1.id
        self.session.add(r1)
        self.session.commit()
        # Validating created at.
        self.assertTrue(r1.created_at)
        self.assertIsInstance(r1.created_at.year, int)
        self.assertIsInstance(r1.created_at.month, int)
        self.assertIsInstance(r1.created_at.day, int)

    def test_to_str(self) -> None:
        """
        Test model string serializer.
        """
        p1 = Actor()
        print(p1)  # Should NOT fail.
