"""
Testing app.api.controller.users library.
"""

import unittest

from unittest.mock import patch
from unittest.mock import MagicMock

from app.api.controller import users

from .utils.random import Random

from .mocks.queries import QueryMock
from .mocks.db import DatabaseMock
from .mocks.models import UserMock


class TestGetUserByID(unittest.TestCase):
    """
    Testing AuthController class.
    """

    def test_arguments(self) -> None:
        """
        Test auth.AuthController.get_by_id() arguments.
        """
        with self.assertRaises(users.UserIDException):
            users.AuthController.get_by_id()
        with self.assertRaises(users.UserIDException):
            users.AuthController.get_by_id([])

    @patch.object(users, 'User', QueryMock(None))
    def test_not_found(self) -> None:
        """
        Test auth.AuthController.get_by_id().
        Try a query without results.
        """
        with self.assertRaises(users.UserNotFoundException):
            users.AuthController.get_by_id(Random.get_int())
        with self.assertRaises(users.UserNotFoundException):
            users.AuthController.get_by_id(Random.get_str())

    @patch.object(users, 'User', QueryMock(UserMock()))
    def test_found(self) -> None:
        """
        Test auth.AuthController.get_by_id().
        Try a query with results.
        """
        user = users.AuthController.get_by_id(Random.get_str())
        self.assertTrue(user.username)
        self.assertTrue(user.password)


class TestGetUserByName(unittest.TestCase):
    """
    Testing AuthController class.
    """

    def test_arguments(self) -> None:
        """
        Test auth.AuthController.get_by_name() arguments.
        """
        with self.assertRaises(users.UsernameException):
            users.AuthController.get_by_name()
        with self.assertRaises(users.UsernameException):
            users.AuthController.get_by_name([])
        with self.assertRaises(users.UsernameException):
            users.AuthController.get_by_name(Random.get_int())

    @patch.object(users, 'User', QueryMock(None))
    def test_not_found(self) -> None:
        """
        Test auth.AuthController.get_by_name().
        Try a query without results.
        """
        with self.assertRaises(users.UserNotFoundException):
            users.AuthController.get_by_name(Random.get_str())

    @patch.object(users, 'User', QueryMock(UserMock()))
    def test_found(self) -> None:
        """
        Test auth.AuthController.get_by_name().
        Try a query with results.
        """
        user = users.AuthController.get_by_name(Random.get_str())
        self.assertTrue(user.username)
        self.assertTrue(user.password)


class TestLogin(unittest.TestCase):
    """
    Testing AuthController class.
    """

    def test_arguments(self) -> None:
        """
        Test auth.AuthController.login() arguments.
        """
        with self.assertRaises(users.PasswordException):
            users.AuthController.login()
        with self.assertRaises(users.PasswordException):
            users.AuthController.login([])
        with self.assertRaises(users.PasswordException):
            users.AuthController.login(Random.get_int())
        with self.assertRaises(users.UsernameException):
            users.AuthController.login(password=Random.get_str())
        with self.assertRaises(users.UsernameException):
            users.AuthController.login(password=Random.get_str(),
                                       username=None)
        with self.assertRaises(users.UsernameException):
            users.AuthController.login(password=Random.get_str(),
                                       username=Random.get_int())

    @patch.object(users.AuthController,
                  "get_by_name",
                  return_value=UserMock(_is_password_valid=False))
    def test_wrong_password(self, *args) -> None:
        """
        Test auth.AuthController.login().
        The password provided is wrong.
        """
        with self.assertRaises(users.WrongPasswordException):
            users.AuthController.login(password=Random.get_str(),
                                       username=Random.get_str())

    @patch.object(users.AuthController,
                  "get_by_name",
                  return_value=UserMock(_is_active=False))
    def test_inactive_user(self, *args) -> None:
        """
        Test auth.AuthController.login().
        The user is inactive.
        """
        with self.assertRaises(users.InactiveUserException):
            users.AuthController.login(password=Random.get_str(),
                                       username=Random.get_str())

    @patch.object(users, 'login_user', MagicMock())
    @patch.object(users, 'db', DatabaseMock())
    @patch.object(users, 'session', UserMock.SESSION)
    @patch.object(users.AuthController,
                  "get_by_name",
                  return_value=UserMock(_is_password_valid=True))
    def test_valid_login(self, *args) -> None:
        """
        Test auth.AuthController.login().
        Credentials are OK.
        """
        token = users.AuthController.login(password=Random.get_str(),
                                           username=Random.get_str())
        self.assertIsInstance(token, str)
        self.assertTrue(token)


class TestLogout(unittest.TestCase):
    """
    Testing AuthController class.
    """

    @patch.object(users, 'logout_user', MagicMock())
    @patch.object(users, 'db', DatabaseMock())
    @patch.object(users, 'session', UserMock.SESSION)
    def test_valid_logout(self) -> None:
        """
        Test auth.AuthController.logout().
        Session is OK.
        """
        users.AuthController.logout()


class TestCreateAdmin(unittest.TestCase):
    """
    Testing AuthController class.
    """

    def test_arguments(self) -> None:
        """
        Test auth.AuthController.create_admin() arguments.
        """
        with self.assertRaises(users.UsernameException):
            users.AuthController.create_admin()
        with self.assertRaises(users.UsernameException):
            users.AuthController.create_admin([])
        with self.assertRaises(users.UsernameException):
            users.AuthController.create_admin(Random.get_int())
        with self.assertRaises(users.PasswordException):
            users.AuthController.create_admin(username=Random.get_str())
        with self.assertRaises(users.PasswordException):
            users.AuthController.create_admin(username=Random.get_str(),
                                              password=None)
        with self.assertRaises(users.PasswordException):
            users.AuthController.create_admin(username=Random.get_str(),
                                              password=Random.get_int())

    @patch.object(users, "db", DatabaseMock())
    @patch.object(users.AuthController, "get_by_name", return_value=UserMock())
    def test_create_admin(self, *args) -> None:
        """
        Test auth.AuthController.create_admin().
        The admin already exists. Hence, it is updated.
        """
        admin = users.AuthController.create_admin(password=Random.get_str(),
                                                  username=Random.get_str())
        self.assertTrue(admin.username)
        self.assertTrue(admin.password)

    @patch.object(users, "User", UserMock)
    @patch.object(users, "db", DatabaseMock())
    def test_user_not_found(self) -> None:
        """
        Test auth.AuthController.create_admin().
        The admin does not exist. Hence, it is created.
        """
        with patch.object(users.AuthController, "get_by_name") as mock:
            mock.side_effect = users.UserNotFoundException()
            admin = users.AuthController.create_admin(password=Random.get_str(),
                                                      username=Random.get_str())
            self.assertTrue(admin.username)
            self.assertTrue(admin.password)
