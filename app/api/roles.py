"""
Movies Views.
"""

import logging

from flask_login import login_required
from flask import request

from . import constants, errors, API
from .controller import movies, people, roles
from .serializers import MovieSerializer, PersonSerializer

logger = logging.getLogger(__name__)


class ActorAPI(API):
    """
    Movie Actors API.
    """

    @login_required
    def _post(self, person_id: int, movie_id: int) -> dict:
        """
        Adding Actor to Movie.
        Error handling is performed by the parent class method.
        @raises: PersonNotFoundException, MovieNotFoundException.
        """
        logger.debug("Adding Actor to Movie.")
        try:
            person, movie = roles.RolesController.add_actor(person_id=person_id,
                                                            movie_id=movie_id)
            logger.debug("Added Actor to Movie!")
            return {
                constants.Person.SINGULAR: PersonSerializer.serialize(person),
                constants.Movie.SINGULAR: MovieSerializer.serialize(movie),
            }
        except people.PersonIDException:
            raise errors.PersonNotFoundException()
        except people.PersonNotFoundException:
            raise errors.PersonNotFoundException()
        except movies.MovieIDException:
            raise errors.MovieNotFoundException()
        except movies.MovieNotFoundException:
            raise errors.MovieNotFoundException()

    @login_required
    def _delete(self, person_id: int, movie_id: int) -> dict:
        """
        Deleting Actor from Movie.
        Error handling is performed by the parent class method.
        @raises: PersonNotFoundException, MovieNotFoundException.
        """
        logger.debug("Deleting Actor from Movie.")
        try:
            person, movie = roles.RolesController.delete_actor(person_id=person_id,
                                                               movie_id=movie_id)
            logger.debug("Deleted Actor from Movie!")
            return {
                constants.Person.SINGULAR: PersonSerializer.serialize(person),
                constants.Movie.SINGULAR: MovieSerializer.serialize(movie),
            }
        except people.PersonIDException:
            raise errors.PersonNotFoundException()
        except people.PersonNotFoundException:
            raise errors.PersonNotFoundException()
        except movies.MovieIDException:
            raise errors.MovieNotFoundException()
        except movies.MovieNotFoundException:
            raise errors.MovieNotFoundException()


class DirectorAPI(API):
    """
    Movie Directors API.
    """

    @login_required
    def _post(self, person_id: int, movie_id: int) -> dict:
        """
        Adding Director to Movie.
        Error handling is performed by the parent class method.
        @raises: PersonNotFoundException, MovieNotFoundException.
        """
        logger.debug("Adding Director to Movie.")
        try:
            person, movie = roles.RolesController.add_director(person_id=person_id,
                                                               movie_id=movie_id)
            logger.debug("Added Director to Movie!")
            return {
                constants.Person.SINGULAR: PersonSerializer.serialize(person),
                constants.Movie.SINGULAR: MovieSerializer.serialize(movie),
            }
        except people.PersonIDException:
            raise errors.PersonNotFoundException()
        except people.PersonNotFoundException:
            raise errors.PersonNotFoundException()
        except movies.MovieIDException:
            raise errors.MovieNotFoundException()
        except movies.MovieNotFoundException:
            raise errors.MovieNotFoundException()

    @login_required
    def _delete(self, person_id: int, movie_id: int) -> dict:
        """
        Deleting Director from Movie.
        Error handling is performed by the parent class method.
        @raises: PersonNotFoundException, MovieNotFoundException.
        """
        logger.debug("Deleting Director from Movie.")
        try:
            person, movie = roles.RolesController.delete_director(person_id=person_id,
                                                                  movie_id=movie_id)
            logger.debug("Deleted Director from Movie!")
            return {
                constants.Person.SINGULAR: PersonSerializer.serialize(person),
                constants.Movie.SINGULAR: MovieSerializer.serialize(movie),
            }
        except people.PersonIDException:
            raise errors.PersonNotFoundException()
        except people.PersonNotFoundException:
            raise errors.PersonNotFoundException()
        except movies.MovieIDException:
            raise errors.MovieNotFoundException()
        except movies.MovieNotFoundException:
            raise errors.MovieNotFoundException()


class ProducerAPI(API):
    """
    Movie Producers API.
    """

    @login_required
    def _post(self, person_id: int, movie_id: int) -> dict:
        """
        Adding Producers to Movie.
        Error handling is performed by the parent class method.
        @raises: PersonNotFoundException, MovieNotFoundException.
        """
        logger.debug("Adding Producer to Movie.")
        try:
            person, movie = roles.RolesController.add_producer(person_id=person_id,
                                                               movie_id=movie_id)
            logger.debug("Added Producer to Movie!")
            return {
                constants.Person.SINGULAR: PersonSerializer.serialize(person),
                constants.Movie.SINGULAR: MovieSerializer.serialize(movie),
            }
        except people.PersonIDException:
            raise errors.PersonNotFoundException()
        except people.PersonNotFoundException:
            raise errors.PersonNotFoundException()
        except movies.MovieIDException:
            raise errors.MovieNotFoundException()
        except movies.MovieNotFoundException:
            raise errors.MovieNotFoundException()

    @login_required
    def _delete(self, person_id: int, movie_id: int) -> dict:
        """
        Deleting Producer from Movie.
        Error handling is performed by the parent class method.
        @raises: PersonNotFoundException, MovieNotFoundException.
        """
        logger.debug("Deleting Producer from Movie.")
        try:
            person, movie = roles.RolesController.delete_producer(person_id=person_id,
                                                                  movie_id=movie_id)
            logger.debug("Deleted Producer from Movie!")
            return {
                constants.Person.SINGULAR: PersonSerializer.serialize(person),
                constants.Movie.SINGULAR: MovieSerializer.serialize(movie),
            }
        except people.PersonIDException:
            raise errors.PersonNotFoundException()
        except people.PersonNotFoundException:
            raise errors.PersonNotFoundException()
        except movies.MovieIDException:
            raise errors.MovieNotFoundException()
        except movies.MovieNotFoundException:
            raise errors.MovieNotFoundException()
