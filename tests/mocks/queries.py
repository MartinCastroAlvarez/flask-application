"""
Queries mocks.
"""

import logging

from . import Mock

logger = logging.getLogger(__name__)


class QueryMock(Mock):
    """
    Mock for Model.query.filter() or Model.query.filter_by().
    """

    def __init__(self, *args) -> None:
        """
        Mocker initializer.
        """
        self.__return_value = args

    @property
    def query(self) -> Mock:
        """
        Query mocker.
        """
        return self

    def filter(self, *args, **kwargs) -> Mock:
        """
        Filter mocker.
        """
        return self

    def filter_by(self, *args, **kwargs) -> Mock:
        """
        Filter mocker.
        """
        return self

    def first(self) -> Mock:
        """
        Mocking Person.query.filter(..).first().
        """
        logger.debug("Getting first element in query.")
        if not self.__return_value or not self.__return_value[0]:
            return None
        return self.__return_value[0]

    @property
    def total(self) -> int:
        """
        Query.pagination.total mock.
        """
        return len(self.all())

    @property
    def items(self) -> list:
        """
        Query.pagination.items mock.
        """
        return self.all()

    def all(self) -> list:
        """
        Mocking Person.query.filter(..).all().
        """
        logger.debug("Getting all elements in query.")
        if not self.__return_value or not self.__return_value[0]:
            return []
        if not isinstance(self.__return_value, (tuple, list, set)):
            return [self.__return_value, ]
        return self.__return_value

    def in_(self, *args, **kwargs) -> None:
        """
        Mocking Model.in_() filter.
        """
        return None

    def paginate(self, *args, **kwargs) -> Mock:
        """
        Mocking Model.query.paginate filter.
        """
        return self

    @property
    def value(self) -> Mock:
        """
        Mocking Model.in_() filter.
        """
        return self
