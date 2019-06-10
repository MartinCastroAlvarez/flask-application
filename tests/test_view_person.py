"""
Testing person API.
"""

import unittest
from unittest.mock import patch

from app import api

from app.api import people
from app.api import errors
from app.api import constants

from .utils.random import Random

from .mocks.models import PersonMock


class TestPersonEndpoint(unittest.TestCase):
    """
    Testing person endpoint.
    """

    @patch.object(api, "jsonify", lambda x: x)
    @patch("app.api.request", json={})
    @patch("app.api.people.request", json={})
    @patch.object(people.PersonSerializer, "serialize", lambda x: x)
    @patch.object(people.people.PeopleController, "get_by_id", return_value=PersonMock())
    def test_get(self, *args):
        """
        Test GET request.
        """
        response = people.PersonAPI().get(person_id=Random.get_int())
        self.assertIsInstance(response, dict)
        self.assertIn(constants.Person.SINGULAR, response)
        self.assertTrue(response[constants.Person.SINGULAR].first_name)
        self.assertTrue(response[constants.Person.SINGULAR].last_name)
        self.assertTrue(response[constants.Person.SINGULAR].created_at)

    @patch.object(api, "jsonify", lambda x: x)
    @patch.object(people.PersonSerializer, "serialize", lambda x: x)
    @patch("app.api.request", json={})
    @patch("app.api.people.request", json={})
    @patch("flask_login.utils.request")
    @patch("flask_login.utils.current_app")
    @patch.object(people.people.PeopleController, "update", return_value=PersonMock())
    def test_put(self, *args):
        """
        Test PUT request.
        """
        response = people.PersonAPI().put(person_id=Random.get_int())
        self.assertIsInstance(response, dict)
        self.assertIn(constants.Person.SINGULAR, response)
        self.assertTrue(response[constants.Person.SINGULAR].first_name)
        self.assertTrue(response[constants.Person.SINGULAR].last_name)
        self.assertTrue(response[constants.Person.SINGULAR].created_at)

    @patch.object(api, "jsonify", lambda x: x)
    @patch("app.api.request", json={})
    def test_post(self, *args):
        """
        Test POST request.
        """
        response = people.PersonAPI().post(person_id=Random.get_int())
        self.assertIn(str(errors.MethodNotImplementedException.SUBCODE),
                      str(response))

    @patch.object(api, "jsonify", lambda x: x)
    @patch.object(people.PersonSerializer, "serialize", lambda x: x)
    @patch("app.api.request", json={})
    @patch("app.api.people.request", json={})
    @patch("flask_login.utils.request")
    @patch("flask_login.utils.current_app")
    @patch.object(people.people.PeopleController, "delete", return_value=PersonMock())
    def test_delete(self, *args):
        """
        Test DELETE request.
        """
        response = people.PersonAPI().delete(person_id=Random.get_int())
        self.assertIsInstance(response, dict)
        self.assertIn(constants.Person.SINGULAR, response)
        self.assertTrue(response[constants.Person.SINGULAR].first_name)
        self.assertTrue(response[constants.Person.SINGULAR].last_name)
        self.assertTrue(response[constants.Person.SINGULAR].created_at)
