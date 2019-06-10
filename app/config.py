"""
Application config constants.

Configuration is passed to this app via
the environment variables defined in this file.
"""

import os

import logging

logger = logging.getLogger(__name__)


class Config(object):
    """
    App config constants.
    """

    DEBUG = "DEBUG"
    SECRET = "SECRET"

    ADMIN_PASSWORD = "ADMIN_PASSWORD"
    ADMIN_USERNAME = "ADMIN_USERNAME"

    LOGIN_DISABLED = "LOGIN_DISABLED"

    DB_USER = "DB_USER"
    DB_PASS = "DB_PASS"
    DB_HOST = "DB_HOST"
    DB_PORT = "DB_PORT"
    DB_NAME = "DB_NAME"

    DB_URI = "SQLALCHEMY_DATABASE_URI"
    DB_TRACK = "SQLALCHEMY_TRACK_MODIFICATIONS"

    @staticmethod
    def get(name: str, default: str=None) -> str:
        """
        Retrieve config value from OS env.

        @raises: TypeError, ValueError.
        """
        if not name:
            raise ValueError("Invalid name:", name)
        if not isinstance(name, str):
            raise TypeError("Expecting str, got:", type(name))
        if default is not None and not isinstance(default, str):
            raise TypeError("Expecting str, got:", type(default))
        value = os.environ.get(name, default)
        logger.debug("Config variable '%s' is: %s", name, value)
        return value
