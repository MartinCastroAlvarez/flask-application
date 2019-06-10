"""
Testing movies API.
"""

import unittest
from unittest.mock import patch

from app import api

from app.api import movies
from app.api import errors
from app.api import constants

from .utils.random import Random

from .mocks.models import MovieMock


class TestMoviesEndpoint(unittest.TestCase):
    """
    Testing movies endpoint.
    """

    @patch.object(api, "jsonify", lambda x: x)
    @patch("app.api.request", json={})
    @patch("app.api.movies.request", json={})
    @patch.object(movies.MovieSerializer, "serialize", lambda x: x)
    @patch.object(movies.movies.MoviesController, "search",
                  return_value=[MovieMock(), MovieMock(), MovieMock()])
    def test_get(self, *args):
        """
        Test GET request.
        """
        response = movies.MoviesAPI().get()
        self.assertIsInstance(response, dict)
        self.assertIn(constants.Movie.PLURAL, response)
        self.assertTrue(response[constants.Movie.PLURAL][0].released_at)
        self.assertTrue(response[constants.Movie.PLURAL][1].title)
        self.assertTrue(response[constants.Movie.PLURAL][2].created_at)

    @patch.object(api, "jsonify", lambda x: x)
    @patch.object(movies.MovieSerializer, "serialize", lambda x: x)
    @patch("app.api.request", json={})
    @patch("app.api.movies.request", json={})
    @patch("flask_login.utils.request")
    @patch("flask_login.utils.current_app")
    @patch.object(movies.movies.MoviesController, "create", return_value=MovieMock())
    def test_post(self, *args):
        """
        Test POST request.
        """
        response = movies.MoviesAPI().post()
        self.assertIsInstance(response, dict)
        self.assertIn(constants.Movie.SINGULAR, response)
        self.assertTrue(response[constants.Movie.SINGULAR].released_at)
        self.assertTrue(response[constants.Movie.SINGULAR].title)
        self.assertTrue(response[constants.Movie.SINGULAR].created_at)

    @patch.object(api, "jsonify", lambda x: x)
    @patch("app.api.request", json={})
    def test_put(self, *args):
        """
        Test PUT request.
        """
        response = movies.MoviesAPI().put()
        self.assertIn(str(errors.MethodNotImplementedException.SUBCODE),
                      str(response))

    @patch.object(api, "jsonify", lambda x: x)
    @patch("app.api.request", json={})
    def test_delete(self, *args):
        """
        Test DELETE request.
        """
        response = movies.MoviesAPI().delete()
        self.assertIn(str(errors.MethodNotImplementedException.SUBCODE),
                      str(response))

    @patch.object(api, "jsonify", lambda x: x)
    @patch.object(movies.MovieSerializer, "serialize", lambda x: x)
    @patch("app.api.request", json={})
    @patch("app.api.movies.request", json={})
    @patch("flask_login.utils.request")
    @patch("flask_login.utils.current_app")
    def test_post_bad_released_at(self, *args):
        """
        Test POST request with bad first name.
        """
        with patch.object(movies.movies.MoviesController, "create") as mock:
            mock.side_effect = movies.movies.TitleException
            response = movies.MoviesAPI().post()
            self.assertIn(str(errors.TitleFormException.SUBCODE),
                          str(response))

    @patch.object(api, "jsonify", lambda x: x)
    @patch.object(movies.MovieSerializer, "serialize", lambda x: x)
    @patch("app.api.request", json={})
    @patch("app.api.movies.request", json={})
    @patch("flask_login.utils.request")
    @patch("flask_login.utils.current_app")
    def test_post_bad_title(self, *args):
        """
        Test POST request with bad last name.
        """
        with patch.object(movies.movies.MoviesController, "create") as mock:
            mock.side_effect = movies.movies.ReleaseDateException
            response = movies.MoviesAPI().post()
            self.assertIn(str(errors.ReleaseDateFormException.SUBCODE),
                          str(response))

    @patch.object(api, "jsonify", lambda x: x)
    @patch.object(movies.MovieSerializer, "serialize", lambda x: x)
    @patch("app.api.request", json={})
    @patch("app.api.movies.request", json={})
    @patch("flask_login.utils.request")
    @patch("flask_login.utils.current_app")
    def test_get_bad_page(self, *args):
        """
        Test GET request with bad page.
        """
        with patch.object(movies.movies.MoviesController, "search") as mock:
            mock.side_effect = movies.movies.PageException
            response = movies.MoviesAPI().get()
            self.assertIn(str(errors.PageFormException.SUBCODE),
                          str(response))

    @patch.object(api, "jsonify", lambda x: x)
    @patch.object(movies.MovieSerializer, "serialize", lambda x: x)
    @patch("app.api.request", json={})
    @patch("app.api.movies.request", json={})
    @patch("flask_login.utils.request")
    @patch("flask_login.utils.current_app")
    def test_get_bad_limit(self, *args):
        """
        Test GET request with bad limit.
        """
        with patch.object(movies.movies.MoviesController, "search") as mock:
            mock.side_effect = movies.movies.LimitException
            response = movies.MoviesAPI().get()
            self.assertIn(str(errors.LimitFormException.SUBCODE),
                          str(response))
