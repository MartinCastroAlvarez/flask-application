"""
DB mocks.
"""

import logging

from . import Mock

logger = logging.getLogger(__name__)


class DatabaseMock(Mock):
    """
    Mock for db connector.
    """

    @property
    def session(self) -> object:
        """
        db.session mocker.
        """
        return self

    def commit(self, *args, **kwargs) -> None:
        """
        db.session.commit() mocker
        """
        logger.debug("Commiting DB changes.")

    def rollback(self, *args, **kwargs) -> None:
        """
        db.session.rollback() mocker
        """
        logger.debug("Rollback called on DB changes.")

    def add(self, *args, **kwargs) -> None:
        """
        db.session.add() mocker
        """
        logger.debug("Adding to db session.")

    def delete(self, *args, **kwargs) -> None:
        """
        db.session.delete() mocker
        """
        logger.debug("Deleting from db session.")
