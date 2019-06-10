"""
Actors Controller.
"""

import logging

from sqlalchemy.exc import IntegrityError

from .models.role import Actor, Director, Producer
from .models import db

from . import Controller

from . import people, movies

logger = logging.getLogger(__name__)


class RolesController(Controller):
    """
    Roles controller business layer.
    """

    @staticmethod
    def add_actor(person_id: int, movie_id: int) -> tuple:
        """
        Add Person to Movie as Actor.
        No custom exceptions raised. Custom exceptions
        are handled by movies.py and people.py.
        """
        logger.debug("Adding '%s' to '%s' as Actor.", person_id, movie_id)
        movie = movies.MoviesController.get_by_id(movie_id=movie_id)
        person = people.PeopleController.get_by_id(person_id=person_id)
        role = Actor(movie_id=movie.id, person_id=person.id)
        try:
            db.session.add(role)
            db.session.commit()
        except IntegrityError:
            pass
        logger.debug("Added '%s' to '%s' as Actor!", person_id, movie_id)
        return person, movie

    @staticmethod
    def add_director(person_id: int, movie_id: int) -> tuple:
        """
        Add Person to Movie as Director.
        No custom exceptions raised. Custom exceptions
        are handled by movies.py and people.py.
        """
        logger.debug("Adding '%s' to '%s' as Director.", person_id, movie_id)
        movie = movies.MoviesController.get_by_id(movie_id=movie_id)
        person = people.PeopleController.get_by_id(person_id=person_id)
        role = Director(movie_id=movie.id, person_id=person.id)
        try:
            db.session.add(role)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
        logger.debug("Added '%s' to '%s' as Director!", person_id, movie_id)
        return person, movie

    @staticmethod
    def add_producer(person_id: int, movie_id: int) -> tuple:
        """
        Add Person to Movie as Producer.
        No custom exceptions raised. Custom exceptions
        are handled by movies.py and people.py.
        """
        logger.debug("Adding '%s' to '%s' as Producer.", person_id, movie_id)
        movie = movies.MoviesController.get_by_id(movie_id=movie_id)
        person = people.PeopleController.get_by_id(person_id=person_id)
        role = Producer(movie_id=movie.id, person_id=person.id)
        try:
            db.session.add(role)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
        logger.debug("Added '%s' to '%s' as Producer!", person_id, movie_id)
        return person, movie

    @staticmethod
    def delete_producer(person_id: int, movie_id: int) -> tuple:
        """
        Delete Person from Movie as Producer.
        No custom exceptions raised. Custom exceptions
        are handled by movies.py and people.py.
        """
        logger.debug("Deleting '%s' from '%s' as Producer.", person_id, movie_id)
        movie = movies.MoviesController.get_by_id(movie_id=movie_id)
        person = people.PeopleController.get_by_id(person_id=person_id)
        role = Producer.query.filter_by(movie_id=movie.id, person_id=person.id).first()
        if role:
            db.session.delete(role)
            db.session.commit()
        logger.debug("Deleted '%s' from '%s' as Producer!", person_id, movie_id)
        return person, movie

    @staticmethod
    def delete_director(person_id: int, movie_id: int) -> tuple:
        """
        Delete Person from Movie as Director.
        No custom exceptions raised. Custom exceptions
        are handled by movies.py and people.py.
        """
        logger.debug("Deleting '%s' from '%s' as Director.", person_id, movie_id)
        movie = movies.MoviesController.get_by_id(movie_id=movie_id)
        person = people.PeopleController.get_by_id(person_id=person_id)
        role = Director.query.filter_by(movie_id=movie.id, person_id=person.id).first()
        if role:
            db.session.delete(role)
            db.session.commit()
        logger.debug("Deleted '%s' from '%s' as Director!", person_id, movie_id)
        return person, movie

    @staticmethod
    def delete_actor(person_id: int, movie_id: int) -> tuple:
        """
        Delete Person from Movie as Actor.
        No custom exceptions raised. Custom exceptions
        are handled by movies.py and people.py.
        """
        logger.debug("Deleting '%s' from '%s' as Actor.", person_id, movie_id)
        movie = movies.MoviesController.get_by_id(movie_id=movie_id)
        person = people.PeopleController.get_by_id(person_id=person_id)
        role = Actor.query.filter_by(movie_id=movie.id, person_id=person.id).first()
        if role:
            db.session.delete(role)
            db.session.commit()
        logger.debug("Deleted '%s' from '%s' as Actor!", person_id, movie_id)
        return person, movie
