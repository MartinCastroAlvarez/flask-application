"""
Authentication Views.
"""

import logging

from flask_login import login_required
from flask import request, session

from . import constants, errors, API
from .controller import users 

logger = logging.getLogger(__name__)


class AuthAPI(API):
    """
    Authentication views.
    """

    def _post(self) -> dict:
        """
        Login API.
        Error handling is performed by the parent class method.
        @raises: AuthException, InvalidPasswordAuthException,
                 UserNotFoundAuthException, AuthException,
                 PasswordFormError, UsernameFormError,
        """
        logger.debug("Authenticating")
        username = request.json.get(constants.Auth.USERNAME)
        password = request.json.get(constants.Auth.PASSWORD)
        try:
            token = users.AuthController.login(username=username, password=password)
            logger.debug("Authenticated!")
            return {
                constants.Auth.TOKEN: token,
            }
        except users.InactiveUserException:
            raise errors.AuthException()
        except users.WrongPasswordException:
            raise errors.InvalidPasswordAuthException()
        except users.UserNotFoundException:
            raise errors.UserNotFoundAuthException()
        except users.PasswordException:
            raise errors.PasswordFormError
        except users.UsernameException:
            raise errors.UsernameFormError()
        except users.AuthException:
            raise errors.AuthException()

    @login_required
    def _delete(self) -> dict:
        """
        Logout API.
        Error handling is performed by the parent class method.
        @raises: AuthException, UserNotFoundAuthException.
        """
        logger.debug("Logging out.")
        try:
            users.AuthController.logout()
        except users.UserIDException:
            raise errors.AuthException()
        except users.UserNotFoundException:
            raise errors.UserNotFoundAuthException()
        except users.AuthException:
            raise errors.AuthException()
        logger.debug("Logged out!")
