"""
Business Layer.
"""

import typing

import logging

logger = logging.getLogger()


class ControllerException(Exception):
    """
    Parent class for all exceptions in this folder.
    """

    def __init__(self, *errors) -> None:
        """
        Initializing exception with custom errors.
        """
        self.__errors = errors
        logger.error("Error on Controller business layer. [%s] %s", self, errors)


class Controller(object):
    """
    Application Controller.
    """
