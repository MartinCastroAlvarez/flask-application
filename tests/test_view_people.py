"""
Testing people API.
"""

import unittest
from unittest.mock import patch

from app import api

from app.api import people
from app.api import errors
from app.api import constants

from .utils.random import Random

from .mocks.models import PersonMock


class TestPeopleEndpoint(unittest.TestCase):
    """
    Testing people endpoint.
    """

    @patch.object(api, "jsonify", lambda x: x)
    @patch("app.api.request", json={})
    @patch("app.api.people.request", json={})
    @patch.object(people.PersonSerializer, "serialize", lambda x: x)
    @patch.object(people.people.PeopleController, "search",
                  return_value=[PersonMock(), PersonMock(), PersonMock()])
    def test_get(self, *args):
        """
        Test GET request.
        """
        response = people.PeopleAPI().get()
        self.assertIsInstance(response, dict)
        self.assertIn(constants.Person.PLURAL, response)
        self.assertTrue(response[constants.Person.PLURAL][0].first_name)
        self.assertTrue(response[constants.Person.PLURAL][1].last_name)
        self.assertTrue(response[constants.Person.PLURAL][2].created_at)

    @patch.object(api, "jsonify", lambda x: x)
    @patch.object(people.PersonSerializer, "serialize", lambda x: x)
    @patch("app.api.request", json={})
    @patch("app.api.people.request", json={})
    @patch("flask_login.utils.request")
    @patch("flask_login.utils.current_app")
    @patch.object(people.people.PeopleController, "create", return_value=PersonMock())
    def test_post(self, *args):
        """
        Test POST request.
        """
        response = people.PeopleAPI().post()
        self.assertIsInstance(response, dict)
        self.assertIn(constants.Person.SINGULAR, response)
        self.assertTrue(response[constants.Person.SINGULAR].first_name)
        self.assertTrue(response[constants.Person.SINGULAR].last_name)
        self.assertTrue(response[constants.Person.SINGULAR].created_at)

    @patch.object(api, "jsonify", lambda x: x)
    @patch("app.api.request", json={})
    def test_put(self, *args):
        """
        Test PUT request.
        """
        response = people.PeopleAPI().put()
        self.assertIn(str(errors.MethodNotImplementedException.SUBCODE),
                      str(response))

    @patch.object(api, "jsonify", lambda x: x)
    @patch("app.api.request", json={})
    def test_delete(self, *args):
        """
        Test DELETE request.
        """
        response = people.PeopleAPI().delete()
        self.assertIn(str(errors.MethodNotImplementedException.SUBCODE),
                      str(response))

    @patch.object(api, "jsonify", lambda x: x)
    @patch.object(people.PersonSerializer, "serialize", lambda x: x)
    @patch("app.api.request", json={})
    @patch("app.api.people.request", json={})
    @patch("flask_login.utils.request")
    @patch("flask_login.utils.current_app")
    def test_post_bad_first_name(self, *args):
        """
        Test POST request with bad first name.
        """
        with patch.object(people.people.PeopleController, "create") as mock:
            mock.side_effect = people.people.FirstNameException
            response = people.PeopleAPI().post()
            self.assertIn(str(errors.FirstNameFormException.SUBCODE),
                          str(response))

    @patch.object(api, "jsonify", lambda x: x)
    @patch.object(people.PersonSerializer, "serialize", lambda x: x)
    @patch("app.api.request", json={})
    @patch("app.api.people.request", json={})
    @patch("flask_login.utils.request")
    @patch("flask_login.utils.current_app")
    def test_post_bad_last_name(self, *args):
        """
        Test POST request with bad last name.
        """
        with patch.object(people.people.PeopleController, "create") as mock:
            mock.side_effect = people.people.LastNameException
            response = people.PeopleAPI().post()
            self.assertIn(str(errors.LastNameFormException.SUBCODE),
                          str(response))

    @patch.object(api, "jsonify", lambda x: x)
    @patch.object(people.PersonSerializer, "serialize", lambda x: x)
    @patch("app.api.request", json={})
    @patch("app.api.people.request", json={})
    @patch("flask_login.utils.request")
    @patch("flask_login.utils.current_app")
    def test_post_bad_alias(self, *args):
        """
        Test POST request with bad alias.
        """
        with patch.object(people.people.PeopleController, "create") as mock:
            mock.side_effect = people.people.AliasException
            response = people.PeopleAPI().post()
            self.assertIn(str(errors.AliasFormException.SUBCODE),
                          str(response))

    @patch.object(api, "jsonify", lambda x: x)
    @patch.object(people.PersonSerializer, "serialize", lambda x: x)
    @patch("app.api.request", json={})
    @patch("app.api.people.request", json={})
    @patch("flask_login.utils.request")
    @patch("flask_login.utils.current_app")
    def test_post_alias_taken(self, *args):
        """
        Test POST request with alias taken.
        """
        with patch.object(people.people.PeopleController, "create") as mock:
            mock.side_effect = people.people.AliasTakenException
            response = people.PeopleAPI().post()
            self.assertIn(str(errors.AliasTakenException.SUBCODE),
                          str(response))

    @patch.object(api, "jsonify", lambda x: x)
    @patch.object(people.PersonSerializer, "serialize", lambda x: x)
    @patch("app.api.request", json={})
    @patch("app.api.people.request", json={})
    @patch("flask_login.utils.request")
    @patch("flask_login.utils.current_app")
    def test_get_bad_page(self, *args):
        """
        Test GET request with bad page.
        """
        with patch.object(people.people.PeopleController, "search") as mock:
            mock.side_effect = people.people.PageException
            response = people.PeopleAPI().get()
            self.assertIn(str(errors.PageFormException.SUBCODE),
                          str(response))

    @patch.object(api, "jsonify", lambda x: x)
    @patch.object(people.PersonSerializer, "serialize", lambda x: x)
    @patch("app.api.request", json={})
    @patch("app.api.people.request", json={})
    @patch("flask_login.utils.request")
    @patch("flask_login.utils.current_app")
    def test_get_bad_limit(self, *args):
        """
        Test GET request with bad limit.
        """
        with patch.object(people.people.PeopleController, "search") as mock:
            mock.side_effect = people.people.LimitException
            response = people.PeopleAPI().get()
            self.assertIn(str(errors.LimitFormException.SUBCODE),
                          str(response))
