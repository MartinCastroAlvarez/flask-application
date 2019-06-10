"""
Testing app.api.controller.movies library.
"""

import unittest
from unittest.mock import patch

from app.api.controller import movies

from .utils.random import Random

from .mocks.queries import QueryMock
from .mocks.db import DatabaseMock
from .mocks.models import MovieMock, AliasMock


class TestGetMovieByID(unittest.TestCase):
    """
    Testing MoviesController class.
    """

    def test_arguments(self) -> None:
        """
        Test movies.MoviesController.get_by_id() arguments.
        """
        with self.assertRaises(movies.MovieIDException):
            movies.MoviesController.get_by_id()
        with self.assertRaises(movies.MovieIDException):
            movies.MoviesController.get_by_id([])

    @patch.object(movies, 'Movie', QueryMock(None))
    def test_not_found(self) -> None:
        """
        Test movies.MoviesController.get_by_id().
        Try a query without results.
        """
        with self.assertRaises(movies.MovieNotFoundException):
            movies.MoviesController.get_by_id(Random.get_int())
        with self.assertRaises(movies.MovieNotFoundException):
            movies.MoviesController.get_by_id(Random.get_str())

    @patch.object(movies, 'Movie', QueryMock(MovieMock()))
    def test_found(self) -> None:
        """
        Test movies.MoviesController.get_by_id().
        Try a query with results.
        """
        movie = movies.MoviesController.get_by_id(Random.get_int())
        self.assertTrue(movie.title)
        self.assertTrue(movie.released_at)


class TestCreateMovie(unittest.TestCase):
    """
    Testing MoviesController class.
    """

    def test_arguments(self) -> None:
        """
        Test movies.MoviesController.create() arguments.
        """
        with self.assertRaises(movies.TitleException):
            movies.MoviesController.create()
        with self.assertRaises(movies.TitleException):
            movies.MoviesController.create(title=Random.get_int())
        with self.assertRaises(movies.ReleaseDateException):
            movies.MoviesController.create(title=Random.get_str())
        with self.assertRaises(movies.ReleaseDateException):
            movies.MoviesController.create(title=Random.get_str(),
                                           released_at=Random.get_int())

    @patch.object(movies, "Movie", MovieMock)
    @patch.object(movies, "db", DatabaseMock())
    def test_created(self) -> None:
        """
        Test movies.MoviesController.create().
        Alias is alread taken.
        """
        movie = movies.MoviesController.create(title=Random.get_str(),
                                               released_at=Random.get_str())
        self.assertTrue(movie.title)
        self.assertTrue(movie.released_at)
        self.assertTrue(movie.created_at)


class TestUpdateMovie(unittest.TestCase):
    """
    Testing MoviesController class.
    """

    def test_arguments(self) -> None:
        """
        Test movies.MoviesController.update() arguments.
        """
        with self.assertRaises(movies.MovieIDException):
            movies.MoviesController.update(movie_id=Random.get_float())
        with self.assertRaises(movies.TitleException):
            movies.MoviesController.update(title=Random.get_int())
        with self.assertRaises(movies.ReleaseDateException):
            movies.MoviesController.update(title=Random.get_str(),
                                           released_at=Random.get_int())

    @patch.object(movies.MoviesController, "get_by_id", return_value=MovieMock())
    @patch.object(movies, "Movie", MovieMock)
    @patch.object(movies, "db", DatabaseMock())
    def test_updated(self, *args) -> None:
        """
        Test movies.MoviesController.update().
        """
        movie = movies.MoviesController.update(title=Random.get_str(),
                                               movie_id=Random.get_str(),
                                               released_at=Random.get_str())
        self.assertTrue(movie.title)
        self.assertTrue(movie.released_at)
        self.assertTrue(movie.created_at)

    @patch.object(movies.MoviesController, "get_by_id", return_value=None)
    @patch.object(movies, "Movie", MovieMock)
    @patch.object(movies, "db", DatabaseMock())
    def test_not_found(self, *args) -> None:
        """
        Test movies.MoviesController.update().
        """
        with self.assertRaises(movies.MovieNotFoundException):
            movies.MoviesController.update(title=Random.get_str(),
                                           movie_id=Random.get_str(),
                                           released_at=Random.get_str())


class TestDeleteMovie(unittest.TestCase):
    """
    Testing MoviesController class.
    """

    def test_arguments(self) -> None:
        """
        Test movies.MoviesController.delete() arguments.
        """
        with self.assertRaises(movies.MovieIDException):
            movies.MoviesController.delete()
        with self.assertRaises(movies.MovieIDException):
            movies.MoviesController.delete(movie_id=Random.get_float())

    @patch.object(movies.MoviesController, "get_by_id", return_value=MovieMock())
    @patch.object(movies, "Movie", MovieMock)
    @patch.object(movies, "db", DatabaseMock())
    def test_deleted(self, *args) -> None:
        """
        Test movies.MoviesController.delete().
        """
        movie = movies.MoviesController.delete(movie_id=Random.get_str())
        self.assertTrue(movie.title)
        self.assertTrue(movie.released_at)
        self.assertTrue(movie.created_at)

    @patch.object(movies.MoviesController, "get_by_id", return_value=None)
    @patch.object(movies, "Movie", MovieMock)
    @patch.object(movies, "db", DatabaseMock())
    def test_not_found(self, *args) -> None:
        """
        Test movies.MoviesController.delete().
        """
        with self.assertRaises(movies.MovieNotFoundException):
            movies.MoviesController.delete(movie_id=Random.get_str())


class TestListMovies(unittest.TestCase):
    """
    Testing MoviesController class.
    """

    def test_arguments(self) -> None:
        """
        Test movies.MoviesController.search() arguments.
        """
        with self.assertRaises(movies.PageException):
            list(movies.MoviesController.search(page=-1 * Random.get_int()))
        with self.assertRaises(movies.PageException):
            list(movies.MoviesController.search(page=Random.get_float()))
        with self.assertRaises(movies.PageException):
            list(movies.MoviesController.search(page=Random.get_str()))
        with self.assertRaises(movies.LimitException):
            list(movies.MoviesController.search(limit=-1 * Random.get_int()))
        with self.assertRaises(movies.LimitException):
            list(movies.MoviesController.search(limit=Random.get_float()))
        with self.assertRaises(movies.LimitException):
            list(movies.MoviesController.search(limit=Random.get_str()))

    @patch.object(movies, 'Movie', QueryMock(None))
    def test_not_found(self) -> None:
        """
        Test movies.MoviesController.list().
        Try a query without results.
        """
        results = list(movies.MoviesController.search())
        self.assertIsInstance(results, list)
        self.assertFalse(results)

    @patch.object(movies, 'Movie', QueryMock(MovieMock()))
    def test_not_found(self) -> None:
        """
        Test movies.MoviesController.search().
        Try a query with results.
        """
        results = list(movies.MoviesController.search())
        self.assertIsInstance(results, list)
        self.assertTrue(results)
