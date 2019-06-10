"""
Testing role API.
"""

import unittest
from unittest.mock import patch

from app import api

from app.api import roles
from app.api import errors
from app.api import constants

from .utils.random import Random

from .mocks.models import PersonMock, MovieMock, ActorMock, DirectorMock, ProducerMock


class TestActorRoleAPI(unittest.TestCase):
    """
    Testing Actor endpoint.
    """

    @patch.object(api, "jsonify", lambda x: x)
    @patch("app.api.request", json={})
    @patch("app.api.people.request", json={})
    @patch("flask_login.utils.request")
    @patch("flask_login.utils.current_app")
    @patch.object(roles.PersonSerializer, "serialize", lambda x: x)
    @patch.object(roles.MovieSerializer, "serialize", lambda x: x)
    @patch.object(roles.roles.RolesController, "add_actor",
                  return_value=[PersonMock(), MovieMock()])
    def test_post(self, *args):
        """
        Test POST request.
        """
        response = roles.ActorAPI().post(person_id=Random.get_int(),
                                        movie_id=Random.get_int())
        self.assertIsInstance(response, dict)
        self.assertIn(constants.Person.SINGULAR, response)
        self.assertTrue(response[constants.Person.SINGULAR].first_name)
        self.assertTrue(response[constants.Person.SINGULAR].last_name)
        self.assertTrue(response[constants.Person.SINGULAR].created_at)
        self.assertIn(constants.Movie.SINGULAR, response)
        self.assertTrue(response[constants.Movie.SINGULAR].title)
        self.assertTrue(response[constants.Movie.SINGULAR].released_at)

    @patch.object(api, "jsonify", lambda x: x)
    @patch("app.api.request", json={})
    @patch("app.api.people.request", json={})
    @patch("flask_login.utils.request")
    @patch("flask_login.utils.current_app")
    @patch.object(roles.PersonSerializer, "serialize", lambda x: x)
    @patch.object(roles.MovieSerializer, "serialize", lambda x: x)
    @patch.object(roles.roles.RolesController, "delete_actor",
                  return_value=[PersonMock(), MovieMock()])
    def test_delete(self, *args):
        """
        Test DELETE request.
        """
        response = roles.ActorAPI().delete(person_id=Random.get_int(),
                                           movie_id=Random.get_int())
        self.assertIsInstance(response, dict)
        self.assertIn(constants.Person.SINGULAR, response)
        self.assertTrue(response[constants.Person.SINGULAR].first_name)
        self.assertTrue(response[constants.Person.SINGULAR].last_name)
        self.assertTrue(response[constants.Person.SINGULAR].created_at)
        self.assertIn(constants.Movie.SINGULAR, response)
        self.assertTrue(response[constants.Movie.SINGULAR].title)
        self.assertTrue(response[constants.Movie.SINGULAR].released_at)

    @patch.object(api, "jsonify", lambda x: x)
    @patch("app.api.request", json={})
    def test_get(self, *args):
        """
        Test GET request.
        """
        response = roles.ActorAPI().get(person_id=Random.get_int(),
                                        movie_id=Random.get_int())
        self.assertIn(str(errors.MethodNotImplementedException.SUBCODE),
                      str(response))

    @patch.object(api, "jsonify", lambda x: x)
    @patch("app.api.request", json={})
    def test_put(self, *args):
        """
        Test PUT request.
        """
        response = roles.ActorAPI().put(person_id=Random.get_int(),
                                        movie_id=Random.get_int())
        self.assertIn(str(errors.MethodNotImplementedException.SUBCODE),
                      str(response))


class TestDirectorRoleAPI(unittest.TestCase):
    """
    Testing Director endpoint.
    """

    @patch.object(api, "jsonify", lambda x: x)
    @patch("app.api.request", json={})
    @patch("app.api.people.request", json={})
    @patch("flask_login.utils.request")
    @patch("flask_login.utils.current_app")
    @patch.object(roles.PersonSerializer, "serialize", lambda x: x)
    @patch.object(roles.MovieSerializer, "serialize", lambda x: x)
    @patch.object(roles.roles.RolesController, "add_director",
                  return_value=[PersonMock(), MovieMock()])
    def test_post(self, *args):
        """
        Test POST request.
        """
        response = roles.DirectorAPI().post(person_id=Random.get_int(),
                                            movie_id=Random.get_int())
        self.assertIsInstance(response, dict)
        self.assertIn(constants.Person.SINGULAR, response)
        self.assertTrue(response[constants.Person.SINGULAR].first_name)
        self.assertTrue(response[constants.Person.SINGULAR].last_name)
        self.assertTrue(response[constants.Person.SINGULAR].created_at)
        self.assertIn(constants.Movie.SINGULAR, response)
        self.assertTrue(response[constants.Movie.SINGULAR].title)
        self.assertTrue(response[constants.Movie.SINGULAR].released_at)

    @patch.object(api, "jsonify", lambda x: x)
    @patch("app.api.request", json={})
    @patch("app.api.people.request", json={})
    @patch("flask_login.utils.request")
    @patch("flask_login.utils.current_app")
    @patch.object(roles.PersonSerializer, "serialize", lambda x: x)
    @patch.object(roles.MovieSerializer, "serialize", lambda x: x)
    @patch.object(roles.roles.RolesController, "delete_director",
                  return_value=[PersonMock(), MovieMock()])
    def test_delete(self, *args):
        """
        Test DELETE request.
        """
        response = roles.DirectorAPI().delete(person_id=Random.get_int(),
                                              movie_id=Random.get_int())
        self.assertIsInstance(response, dict)
        self.assertIn(constants.Person.SINGULAR, response)
        self.assertTrue(response[constants.Person.SINGULAR].first_name)
        self.assertTrue(response[constants.Person.SINGULAR].last_name)
        self.assertTrue(response[constants.Person.SINGULAR].created_at)
        self.assertIn(constants.Movie.SINGULAR, response)
        self.assertTrue(response[constants.Movie.SINGULAR].title)
        self.assertTrue(response[constants.Movie.SINGULAR].released_at)

    @patch.object(api, "jsonify", lambda x: x)
    @patch("app.api.request", json={})
    def test_get(self, *args):
        """
        Test GET request.
        """
        response = roles.DirectorAPI().get(person_id=Random.get_int(),
                                           movie_id=Random.get_int())
        self.assertIn(str(errors.MethodNotImplementedException.SUBCODE),
                      str(response))

    @patch.object(api, "jsonify", lambda x: x)
    @patch("app.api.request", json={})
    def test_put(self, *args):
        """
        Test PUT request.
        """
        response = roles.DirectorAPI().put(person_id=Random.get_int(),
                                           movie_id=Random.get_int())
        self.assertIn(str(errors.MethodNotImplementedException.SUBCODE),
                      str(response))


class TestProducerRoleAPI(unittest.TestCase):
    """
    Testing Producer endpoint.
    """

    @patch.object(api, "jsonify", lambda x: x)
    @patch("app.api.request", json={})
    @patch("app.api.people.request", json={})
    @patch("flask_login.utils.request")
    @patch("flask_login.utils.current_app")
    @patch.object(roles.PersonSerializer, "serialize", lambda x: x)
    @patch.object(roles.MovieSerializer, "serialize", lambda x: x)
    @patch.object(roles.roles.RolesController, "add_producer",
                  return_value=[PersonMock(), MovieMock()])
    def test_post(self, *args):
        """
        Test POST request.
        """
        response = roles.ProducerAPI().post(person_id=Random.get_int(),
                                            movie_id=Random.get_int())
        self.assertIsInstance(response, dict)
        self.assertIn(constants.Person.SINGULAR, response)
        self.assertTrue(response[constants.Person.SINGULAR].first_name)
        self.assertTrue(response[constants.Person.SINGULAR].last_name)
        self.assertTrue(response[constants.Person.SINGULAR].created_at)
        self.assertIn(constants.Movie.SINGULAR, response)
        self.assertTrue(response[constants.Movie.SINGULAR].title)
        self.assertTrue(response[constants.Movie.SINGULAR].released_at)

    @patch.object(api, "jsonify", lambda x: x)
    @patch("app.api.request", json={})
    @patch("app.api.people.request", json={})
    @patch("flask_login.utils.request")
    @patch("flask_login.utils.current_app")
    @patch.object(roles.PersonSerializer, "serialize", lambda x: x)
    @patch.object(roles.MovieSerializer, "serialize", lambda x: x)
    @patch.object(roles.roles.RolesController, "delete_producer",
                  return_value=[PersonMock(), MovieMock()])
    def test_delete(self, *args):
        """
        Test DELETE request.
        """
        response = roles.ProducerAPI().delete(person_id=Random.get_int(),
                                              movie_id=Random.get_int())
        self.assertIsInstance(response, dict)
        self.assertIn(constants.Person.SINGULAR, response)
        self.assertTrue(response[constants.Person.SINGULAR].first_name)
        self.assertTrue(response[constants.Person.SINGULAR].last_name)
        self.assertTrue(response[constants.Person.SINGULAR].created_at)
        self.assertIn(constants.Movie.SINGULAR, response)
        self.assertTrue(response[constants.Movie.SINGULAR].title)
        self.assertTrue(response[constants.Movie.SINGULAR].released_at)

    @patch.object(api, "jsonify", lambda x: x)
    @patch("app.api.request", json={})
    def test_get(self, *args):
        """
        Test GET request.
        """
        response = roles.ProducerAPI().get(person_id=Random.get_int(),
                                           movie_id=Random.get_int())
        self.assertIn(str(errors.MethodNotImplementedException.SUBCODE),
                      str(response))

    @patch.object(api, "jsonify", lambda x: x)
    @patch("app.api.request", json={})
    def test_put(self, *args):
        """
        Test PUT request.
        """
        response = roles.ProducerAPI().put(person_id=Random.get_int(),
                                           movie_id=Random.get_int())
        self.assertIn(str(errors.MethodNotImplementedException.SUBCODE),
                      str(response))
