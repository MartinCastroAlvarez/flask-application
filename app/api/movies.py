"""
Movies Views.
"""

import logging

from flask_login import login_required
from flask import request

from . import constants, errors, API
from .controller import movies
from .serializers import MovieSerializer

logger = logging.getLogger(__name__)


class MoviesAPI(API):
    """
    Movies API.
    """

    @login_required
    def _post(self) -> dict:
        """
        Create Movie.
        Error handling is performed by the parent class method.
        @raises: TitleFormException, ReleaseDateFormException,
        """
        title = request.json.get(constants.Movie.TITLE)
        released_at = request.json.get(constants.Movie.RELEASED_AT)
        is_active = request.json.get(constants.Movie.ACTIVE, True)
        try:
            movie = movies.MoviesController.create(title=title,
                                                   released_at=released_at,
                                                   is_active=is_active)
            logger.debug("Movie created!")
            return {
                constants.Movie.SINGULAR: MovieSerializer.serialize(movie),
            }
        except movies.TitleException:
            raise errors.TitleFormException()
        except movies.ReleaseDateException:
            raise errors.ReleaseDateFormException()

    def _get(self) -> dict:
        """
        Searching for Movies.
        Error handling is performed by the parent class method.
        @raises: LimitFormException, PageFormException.
        """
        logger.debug("Searching for Movies.")
        page = int(request.args.get(constants.Pagination.PAGE, 1))
        limit = int(request.args.get(constants.Pagination.LIMIT, 30))
        try:
            results = movies.MoviesController.search(page=page, limit=limit)
            logger.debug("Movies listed!")
            return {
                constants.Movie.PLURAL: [
                    MovieSerializer.serialize(movie)
                    for movie in results
                ]
            }
        except movies.PageException:
            raise errors.PageFormException()
        except movies.LimitException:
            raise errors.LimitFormException()


class MovieAPI(API):
    """
    Movie API.
    """

    @login_required
    def _put(self, movie_id: int) -> dict:
        """
        Update Movie.
        Error handling is performed by the parent class method.
        @raises: TitleFormException, ReleaseDateFormException,
                 MovieNotFoundException.
        """
        logger.debug("Updating Movie.")
        title = request.json.get(constants.Movie.TITLE)
        released_at = request.json.get(constants.Movie.RELEASED_AT)
        is_active = request.json.get(constants.Movie.ACTIVE, True)
        try:
            movie = movies.MoviesController.update(title=title,
                                                   released_at=released_at,
                                                   movie_id=movie_id,
                                                   is_active=is_active)
            logger.debug("Movie Updated!")
            return {
                constants.Movie.SINGULAR: MovieSerializer.serialize(movie),
            }
        except movies.TitleException:
            raise errors.TitleFormException()
        except movies.ReleaseDateException:
            raise errors.ReleaseDateFormException()
        except movies.MovieIDException:
            raise errors.MovieNotFoundException()
        except movies.MovieNotFoundException:
            raise errors.MovieNotFoundException()

    def _get(self, movie_id: int) -> dict:
        """
        Getting Movie.
        Error handling is performed by the parent class method.
        @raises: MovieNotFoundException.
        """
        logger.debug("Getting Movie.")
        try:
            movie = movies.MoviesController.get_by_id(movie_id=movie_id)
            logger.debug("Movie loaded!")
            return {
                constants.Movie.SINGULAR: MovieSerializer.serialize(movie),
            }
        except movies.MovieIDException:
            raise errors.MovieNotFoundException()
        except movies.MovieNotFoundException:
            raise errors.MovieNotFoundException()

    @login_required
    def _delete(self, movie_id: int) -> dict:
        """
        Deleting Movie.
        Error handling is performed by the parent class method.
        @raises: MovieNotFoundException.
        """
        logger.debug("Deleting Movie.")
        try:
            movie = movies.MoviesController.delete(movie_id=movie_id)
            logger.debug("Movie deleted!")
            return {
                constants.Movie.SINGULAR: MovieSerializer.serialize(movie),
            }
        except movies.MovieIDException:
            raise errors.MovieNotFoundException()
        except movies.MovieNotFoundException:
            raise errors.MovieNotFoundException()
