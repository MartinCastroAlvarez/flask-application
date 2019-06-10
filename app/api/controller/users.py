"""
Authentication Controller.

Reference:
https://flask-login.readthedocs.io/en/latest/
"""

import logging

from flask_login import LoginManager, login_user, logout_user
from flask import session

from .models.user import User
from .models import db

from . import Controller, ControllerException

logger = logging.getLogger(__name__)

login_manager = LoginManager()


class AuthException(ControllerException):
    """
    Parent class for all exceptions in this library.
    """


class UsernameException(AuthException):
    """
    Raised if username is invalid.
    """


class UserIDException(AuthException):
    """
    Raised if user ID is invalid.
    """


class PasswordException(AuthException):
    """
    Raised if password is invalid.
    """


class UserNotFoundException(AuthException):
    """
    Raised if user does not exist.
    """


class WrongPasswordException(AuthException):
    """
    Raised if password does not match.
    """


class InactiveUserException(AuthException):
    """
    Raised if user is inactive.
    """


class AuthController(Controller):
    """
    Auth controller business layer.
    """

    @staticmethod
    @login_manager.user_loader
    def get_by_id(user_id: str=None) -> User:
        """
        Load user by user id.
        @raises: UserIDException, UserNotFoundException.
        """
        logger.debug("Loading user by ID '%s'.", user_id)
        if not user_id or not isinstance(user_id, (int, str)):
            raise UserIDException()
        user = User.query.filter_by(id=user_id, is_active=True).first()
        if not user:
            raise UserNotFoundException()
        logger.debug("User found: '%s'.", user)
        return user

    @staticmethod
    def get_by_name(username: str=None) -> User:
        """
        Load user by username.
        @raises: UsernameException, UserNotFoundException.
        """
        logger.debug("Loading username by name '%s'.", username)
        if not username or not isinstance(username, str):
            raise UsernameException()
        user = User.query.filter_by(username=username, is_active=True).first()
        if not user:
            raise UserNotFoundException()
        logger.debug("User found: '%s'.", user)
        return user

    @classmethod
    def login(cls,username: str=None, password: str=None) -> str:
        """
        Login user.
        Returns the session token.
        @raises: UsernameException, PasswordException,
                 WrongPasswordException, UserNotFoundException,
                 InactiveUserException.
        """
        logger.debug("Authenticating as '%s'.", username)
        if not password or not isinstance(password, str):
            raise PasswordException()
        user = cls.get_by_name(username)
        if not user.is_password_valid(password):
            logger.warning("Password for '%s' is invalid!", username)
            raise WrongPasswordException()
        logger.debug("Password for '%s' is valid!", username)
        if not user.is_active:
            logger.warning("User '%s' is inactive!", username)
            raise InactiveUserException()
        logger.debug("User '%s' is active!", username)
        login_user(user, remember=True)
        logger.debug("User '%s' authenticated.", username)
        return session['_id']

    @staticmethod
    def logout() -> None:
        """
        Logs a user out. (You do not need to pass the
        actual user.) This will also clean up the remember
        me cookie if it exists.
        """
        logger.debug("Calling logout as '%s'.", session)
        logout_user()
        logger.debug("Logged out as '%s'.", session)

    @classmethod
    def create_admin(cls, username: str=None, password: str=None) -> User:
        """
        Creating an admin user, or updating the existing one.

        @raises: PasswordException, UsernameException
        """
        logger.debug("Upserting admin.")
        if not username or not isinstance(username, str):
            raise UsernameException()
        if not password or not isinstance(password, str):
            raise PasswordException()
        try:
            logger.debug("Admin user found!")
            admin = cls.get_by_name(username=username)
        except UserNotFoundException:
            logger.debug("Admin does not exist. Creating a new one.")
            admin = User(username=username)
        admin.password = password
        db.session.add(admin)
        db.session.commit()
        logger.debug("Admin upserted!")
        return admin
