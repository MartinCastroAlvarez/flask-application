"""
Testing movie API.
"""

import unittest
from unittest.mock import patch

from app import api

from app.api import movies
from app.api import errors
from app.api import constants

from .utils.random import Random

from .mocks.models import MovieMock


class TestMovieEndpoint(unittest.TestCase):
    """
    Testing movie endpoint.
    """

    @patch.object(api, "jsonify", lambda x: x)
    @patch("app.api.request", json={})
    @patch("app.api.movies.request", json={})
    @patch.object(movies.MovieSerializer, "serialize", lambda x: x)
    @patch.object(movies.movies.MoviesController, "get_by_id", return_value=MovieMock())
    def test_get(self, *args):
        """
        Test GET request.
        """
        response = movies.MovieAPI().get(movie_id=Random.get_int())
        self.assertIsInstance(response, dict)
        self.assertIn(constants.Movie.SINGULAR, response)
        self.assertTrue(response[constants.Movie.SINGULAR].released_at)
        self.assertTrue(response[constants.Movie.SINGULAR].title)
        self.assertTrue(response[constants.Movie.SINGULAR].created_at)

    @patch.object(api, "jsonify", lambda x: x)
    @patch.object(movies.MovieSerializer, "serialize", lambda x: x)
    @patch("app.api.request", json={})
    @patch("app.api.movies.request", json={})
    @patch("flask_login.utils.request")
    @patch("flask_login.utils.current_app")
    @patch.object(movies.movies.MoviesController, "update", return_value=MovieMock())
    def test_put(self, *args):
        """
        Test PUT request.
        """
        response = movies.MovieAPI().put(movie_id=Random.get_int())
        self.assertIsInstance(response, dict)
        self.assertIn(constants.Movie.SINGULAR, response)
        self.assertTrue(response[constants.Movie.SINGULAR].released_at)
        self.assertTrue(response[constants.Movie.SINGULAR].title)
        self.assertTrue(response[constants.Movie.SINGULAR].created_at)

    @patch.object(api, "jsonify", lambda x: x)
    @patch("app.api.request", json={})
    def test_post(self, *args):
        """
        Test POST request.
        """
        response = movies.MovieAPI().post(movie_id=Random.get_int())
        self.assertIn(str(errors.MethodNotImplementedException.SUBCODE),
                      str(response))

    @patch.object(api, "jsonify", lambda x: x)
    @patch.object(movies.MovieSerializer, "serialize", lambda x: x)
    @patch("app.api.request", json={})
    @patch("app.api.movies.request", json={})
    @patch("flask_login.utils.request")
    @patch("flask_login.utils.current_app")
    @patch.object(movies.movies.MoviesController, "delete", return_value=MovieMock())
    def test_delete(self, *args):
        """
        Test DELETE request.
        """
        response = movies.MovieAPI().delete(movie_id=Random.get_int())
        self.assertIsInstance(response, dict)
        self.assertIn(constants.Movie.SINGULAR, response)
        self.assertTrue(response[constants.Movie.SINGULAR].released_at)
        self.assertTrue(response[constants.Movie.SINGULAR].title)
        self.assertTrue(response[constants.Movie.SINGULAR].created_at)
