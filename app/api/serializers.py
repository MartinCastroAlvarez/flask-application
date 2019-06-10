"""
API serializers.
Views.
"""

import logging

from . import constants
from .controller import people, movies

logger = logging.getLogger(__name__)


class Serializer(object):
    """
    Parent Serializer.
    """

    @classmethod
    def to_json(cls, *args, **kwargs) -> dict:
        """
        Override (plain) serializer.
        """
        raise NotImplementedError()

    @classmethod
    def serialize(cls, *args, **kwargs) -> dict:
        """
        Override (deep) serializer.
        """
        return cls.to_json()


class PersonSerializer(Serializer):
    """
    Person serializer.
    """

    @classmethod
    def to_json(cls, person: people.Person=None) -> dict:
        """
        Person (plain) serializer.
        @raises: TypeError, ValueError.
        """
        logger.debug("Serializing person: %s.", person)
        if not person:
            raise ValueError("Invalid Person.")
        if not isinstance(person, people.Person):
            raise ValueError("Expecting Person, got:", type(person))
        s = {
            constants.Person.ID: person.id,
            constants.Person.FIRST_NAME: person.first_name,
            constants.Person.LAST_NAME: person.last_name,
            constants.Person.ACTIVE: person.is_active,
            constants.Person.CREATED_AT: str(person.created_at),
            constants.Person.ALIASES: [
                alias.value
                for alias in person.aliases
            ]
        }
        logger.debug("Person serialized: %s.", s)
        return s

    @classmethod
    def serialize(cls, person: people.Person=None) -> dict:
        """
        Person (deep) serializer.
        @raises: TypeError, ValueError.
        """
        logger.debug("Serializing person: %s.", person)
        if not person:
            raise ValueError("Invalid Person.")
        if not isinstance(person, people.Person):
            raise ValueError("Expecting Person, got:", type(person))
        s = cls.to_json(person)
        s[constants.Movie.PLURAL] = {
            constants.Actor.SINGULAR: [
                MovieSerializer.to_json(movie)
                for movie in person.movies_as_actor
            ],
            constants.Director.SINGULAR: [
                MovieSerializer.to_json(movie)
                for movie in person.movies_as_director
            ],
            constants.Producer.SINGULAR: [
                MovieSerializer.to_json(movie)
                for movie in person.movies_as_producer
            ],
        }
        logger.debug("Person serialized: %s.", s)
        return s


class MovieSerializer(Serializer):
    """
    Movie serializer.
    """

    @classmethod
    def to_json(cls, movie: movies.Movie=None) -> dict:
        """
        Movie serializer.
        @raises: TypeError, ValueError.
        """
        logger.debug("Serializing movie: %s.", movie)
        if not movie:
            raise ValueError("Invalid Movie.")
        if not isinstance(movie, movies.Movie):
            raise ValueError("Expecting Movie, got:", type(movie))
        s = {
            constants.Movie.ID: movie.id,
            constants.Movie.TITLE: movie.title,
            constants.Movie.RELEASED_AT: {
                constants.Movie.Release.DATE: str(movie.released_at),
                constants.Movie.Release.YEAR: movie.release_year,
                constants.Movie.Release.ROMAN: movie.release_roman,
            },
            constants.Movie.ACTIVE: movie.is_active,
            constants.Movie.CREATED_AT: str(movie.created_at),
        }
        logger.debug("Movie serialized: %s.", s)
        return s

    @classmethod
    def serialize(cls, movie: movies.Movie=None) -> dict:
        """
        Movie serializer.
        @raises: TypeError, ValueError.
        """
        logger.debug("Serializing movie: %s.", movie)
        if not movie:
            raise ValueError("Invalid Movie.")
        if not isinstance(movie, movies.Movie):
            raise ValueError("Expecting Movie, got:", type(movie))
        s = cls.to_json(movie=movie)
        s[constants.Actor.PLURAL] = [
            PersonSerializer.serialize(person)
            for person in movie.actors
        ]
        s[constants.Director.PLURAL] = [
            PersonSerializer.serialize(person)
            for person in movie.directors
        ]
        s[constants.Producer.PLURAL] = [
            PersonSerializer.serialize(person)
            for person in movie.producers
        ]
        logger.debug("Movie serialized: %s.", s)
        return s
