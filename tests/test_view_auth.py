"""
Testing auth API.
"""

import unittest
from unittest.mock import patch

from app import api

from app.api import auth 
from app.api import errors
from app.api import constants

from .utils.random import Random


class TestHealthEndpoint(unittest.TestCase):
    """
    Testing auth endpoint.
    """

    @patch.object(api, "jsonify", lambda x: x)
    @patch("app.api.request", json={})
    def test_get(self, *args):
        """
        Test GET request.
        """
        response = auth.AuthAPI().get()
        self.assertIn(str(errors.MethodNotImplementedException.SUBCODE),
                      str(response))

    @patch.object(api, "jsonify", lambda x: x)
    @patch("app.api.request", json={})
    @patch("app.api.auth.request", json={})
    @patch.object(auth.users.AuthController, "login", return_value=Random.get_str())
    def test_post(self, *args):
        """
        Test POST request.
        """
        response = auth.AuthAPI().post()
        self.assertIsInstance(response, dict)
        self.assertIn(constants.Auth.TOKEN, str(response))

    @patch.object(api, "jsonify", lambda x: x)
    @patch("app.api.request", json={})
    def test_put(self, *args):
        """
        Test PUT request.
        """
        response = auth.AuthAPI().put()
        self.assertIn(str(errors.MethodNotImplementedException.SUBCODE),
                      str(response))

    @patch.object(api, "jsonify", lambda x: x)
    @patch("flask_login.utils.request")
    @patch("flask_login.utils.current_app")
    @patch("app.api.request", json={})
    @patch.object(auth.users.AuthController, "logout", return_value=Random.get_str())
    def test_delete(self, *args):
        """
        Test DELETE request.
        """
        response = auth.AuthAPI().delete()
        self.assertIsInstance(response, dict)
        self.assertFalse(response)

    @patch.object(api, "jsonify", lambda x: x)
    @patch("flask_login.utils.request")
    @patch("flask_login.utils.current_app")
    @patch("app.api.request", json={})
    def test_delete_user_id(self, *args):
        """
        Test DELETE request with bad user ID.
        """
        with patch.object(auth.users.AuthController, "logout") as mock:
            mock.side_effect = auth.users.UserIDException
            response = auth.AuthAPI().delete()
            self.assertIn(str(errors.AuthException.SUBCODE),
                          str(response))

    @patch.object(api, "jsonify", lambda x: x)
    @patch("flask_login.utils.request")
    @patch("flask_login.utils.current_app")
    @patch("app.api.request", json={})
    def test_delete_not_found(self, *args):
        """
        Test DELETE request if user is not found.
        """
        with patch.object(auth.users.AuthController, "logout") as mock:
            mock.side_effect = auth.users.UserNotFoundException
            response = auth.AuthAPI().delete()
            self.assertIn(str(errors.UserNotFoundAuthException.SUBCODE),
                          str(response))

    @patch.object(api, "jsonify", lambda x: x)
    @patch("flask_login.utils.request")
    @patch("flask_login.utils.current_app")
    @patch("app.api.request", json={})
    def test_delete_error(self, *args):
        """
        Test DELETE request if something goes wrong.
        """
        with patch.object(auth.users.AuthController, "logout") as mock:
            mock.side_effect = auth.users.AuthException
            response = auth.AuthAPI().delete()
            self.assertIn(str(errors.AuthException.SUBCODE),
                          str(response))

    @patch.object(api, "jsonify", lambda x: x)
    @patch("app.api.request", json={})
    @patch("app.api.auth.request", json={})
    def test_post_user_id(self, *args):
        """
        Test POST request with bad user ID.
        """
        with patch.object(auth.users.AuthController, "login") as mock:
            mock.side_effect = auth.users.UserIDException
            response = auth.AuthAPI().post()
            self.assertIn(str(errors.AuthException.SUBCODE),
                          str(response))

    @patch.object(api, "jsonify", lambda x: x)
    @patch("app.api.request", json={})
    @patch("app.api.auth.request", json={})
    def test_post_user_inactive(self, *args):
        """
        Test POST request if user is inactive.
        """
        with patch.object(auth.users.AuthController, "login") as mock:
            mock.side_effect = auth.users.InactiveUserException
            response = auth.AuthAPI().post()
            self.assertIn(str(errors.AuthException.SUBCODE),
                          str(response))

    @patch.object(api, "jsonify", lambda x: x)
    @patch("app.api.request", json={})
    @patch("app.api.auth.request", json={})
    def test_post_wrong_password(self, *args):
        """
        Test POST request if password is invalid.
        """
        with patch.object(auth.users.AuthController, "login") as mock:
            mock.side_effect = auth.users.WrongPasswordException
            response = auth.AuthAPI().post()
            self.assertIn(str(errors.InvalidPasswordAuthException.SUBCODE),
                          str(response))

    @patch.object(api, "jsonify", lambda x: x)
    @patch("app.api.request", json={})
    @patch("app.api.auth.request", json={})
    def test_post_empty_password(self, *args):
        """
        Test POST request if password is empty.
        """
        with patch.object(auth.users.AuthController, "login") as mock:
            mock.side_effect = auth.users.PasswordException
            response = auth.AuthAPI().post()
            self.assertIn(str(errors.PasswordFormError.SUBCODE),
                          str(response))

    @patch.object(api, "jsonify", lambda x: x)
    @patch("app.api.request", json={})
    @patch("app.api.auth.request", json={})
    def test_post_empty_username(self, *args):
        """
        Test POST request if username is empty.
        """
        with patch.object(auth.users.AuthController, "login") as mock:
            mock.side_effect = auth.users.UsernameException
            response = auth.AuthAPI().post()
            self.assertIn(str(errors.UsernameFormError.SUBCODE),
                          str(response))

    @patch.object(api, "jsonify", lambda x: x)
    @patch("app.api.request", json={})
    @patch("app.api.auth.request", json={})
    def test_post_user_not_found(self, *args):
        """
        Test POST request if user is not found.
        """
        with patch.object(auth.users.AuthController, "login") as mock:
            mock.side_effect = auth.users.UserNotFoundException
            response = auth.AuthAPI().post()
            self.assertIn(str(errors.UserNotFoundAuthException.SUBCODE),
                          str(response))

    @patch.object(api, "jsonify", lambda x: x)
    @patch("app.api.request", json={})
    @patch("app.api.auth.request", json={})
    def test_unknown_error(self, *args):
        """
        Test POST request if user is not found.
        """
        with patch.object(auth.users.AuthController, "login") as mock:
            mock.side_effect = RuntimeError()
            response = auth.AuthAPI().post()
            self.assertIn(str(errors.MariaException.SUBCODE),
                          str(response))
