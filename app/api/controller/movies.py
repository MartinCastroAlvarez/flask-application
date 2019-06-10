"""
Movies Controller.
"""

import logging
import typing

from .models.movie import Movie
from .models import db

from . import Controller, ControllerException

logger = logging.getLogger(__name__)


class MovieException(ControllerException):
    """
    Parent class for all exceptions in this library.
    """


class TitleException(MovieException):
    """
    Raised if movie title is invalid.
    """


class PageException(MovieException):
    """
    Raised if page number is invalid.
    """


class LimitException(MovieException):
    """
    Raised if page limit is invalid.
    """


class ReleaseDateException(MovieException):
    """
    Raised if release date is invalid.
    """


class MovieIDException(MovieException):
    """
    Raised if movie ID is invalid.
    """


class MovieNotFoundException(MovieException):
    """
    Raised if movie ID is invalid.
    """


class MoviesController(Controller):
    """
    Movies controller business layer.
    """

    @staticmethod
    def get_by_id(movie_id: str=None) -> Movie:
        """
        Load movie by movie id.
        @raises: MovieIDException, MovieNotFoundException.
        """
        logger.debug("Loading movie by ID '%s'.", movie_id)
        if not movie_id or not isinstance(movie_id, (int, str)):
            raise MovieIDException()
        movie = Movie.query.filter_by(id=movie_id, is_active=True).first()
        if not movie:
            raise MovieNotFoundException()
        logger.debug("Movie found: '%s'.", movie)
        return movie

    @staticmethod
    def create(released_at: str=None,
               is_active: bool=True,
               title: str=None) -> Movie:
        """
        Create a new Movie.
        @raises: ReleaseDateException, TitleException.
        """
        logger.debug("Creating Movie: '%s'.", title)
        if not title or not isinstance(title, str):
            raise TitleException()
        if not released_at or not isinstance(released_at, str):
            raise ReleaseDateException()
        movie = Movie(title=title, released_at=released_at)
        movie.is_active = is_active
        db.session.add(movie)
        db.session.commit()
        logger.debug("Movie created: '%s'.", movie)
        return movie

    @classmethod
    def update(cls,
               title: str=None,
               movie_id: int=None,
               is_active: bool=None,
               released_at: str=None) -> Movie:
        """
        Create a new Movie.
        @raises: MovieIDException, MovieNotFoundException,
                 ReleaseDateException, TitleException.
        """
        logger.debug("Updating Movie: '%s'.", title)
        if title and not isinstance(title, str):
            raise TitleException()
        if released_at and not isinstance(released_at, str):
            raise ReleaseDateException()
        movie = cls.get_by_id(movie_id)
        if not movie:
            raise MovieNotFoundException()
        movie.title = title or movie.title
        movie.released_at = released_at or movie.released_at
        movie.is_active = is_active if is_active is not None else movie.is_active
        db.session.add(movie)
        db.session.commit()
        logger.debug("Movie updated: '%s'.", movie)
        return movie

    @classmethod
    def delete(cls, movie_id: int=None) -> Movie:
        """
        Deleting a Movie will always deactive it.
        """
        logger.debug("Deactivating Movie: '%s'.", movie_id)
        movie = cls.update(movie_id=movie_id, is_active=False)
        logger.debug("Movie deactivated: '%s'.", movie_id)
        return movie

    @staticmethod
    def search(page: int=0, limit: int=50) -> typing.Generator:
        """
        Listing & paginatin movies.
        @raises: PageException, LimitException.
        """
        logger.debug("Listing Movies page %s limit %s.", page, limit)
        if not isinstance(page, int) or page < 0:
            raise PageException()
        if not isinstance(limit, int) or limit < 1 or limit > 200:
            raise LimitException()
        query = Movie.query.paginate(page=page, max_per_page=limit)
        yield from (
            movie
            for movie in query.items
        )
        logger.debug("Listed Movies page %s limit %s. Total %s.",
                     page, limit, query.total)
