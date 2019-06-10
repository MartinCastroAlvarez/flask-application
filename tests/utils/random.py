"""
Unit Test Randomness Utilities.
"""

import uuid
import string
import random
import datetime


class Random(object):
    """
    Randomness utilities.
    """

    DATE_FORMAT = '%Y-%m-%d'

    @classmethod
    def get_date(cls,
                 start: datetime.date=None,
                 end: datetime.date=None) -> datetime.date:
        """
        Get random date in range.
        @raises: TypeError, ValueError, NotImplementedError, RuntimeError.
        """
        if not start:
            raise ValueError("Invalid start date.")
        if not end:
            end = datetime.date.today()
        if isinstance(start, str):
            start = datetime.datetime.strptime(start, cls.DATE_FORMAT).date()
        if isinstance(end, str):
            end = datetime.datetime.strptime(end, cls.DATE_FORMAT).date()
        if not isinstance(end, datetime.date):
            raise ValueError("Expecting date, got:", type(end))
        if not isinstance(start, datetime.date):
            raise ValueError("Expecting date, got:", type(start))
        if start >= end:
            raise NotImplementedError(start, end)
        days = (end - start).days
        if not days:
            raise RuntimeError(start, end, days)
        return start + datetime.timedelta(days=cls.get_int(size=days))

    @staticmethod
    def get_str(size: int=10) -> str:
        """
        Generates a random string.
        https://stackoverflow.com/questions/2257441
        @raises: TypeError, ValueError.
        """
        if not isinstance(size, int):
            raise TypeError("Expecting int, got:", type(size))
        if size < 1:
            raise ValueError("Invalid size:", size)
        return ''.join(
            random.choice(string.ascii_uppercase + string.digits)
            for _ in range(size)
        )

    @staticmethod
    def get_int(size: int=10) -> int:
        """
        Generates a random integer.
        @raises: TypeError, ValueError.
        """
        if not isinstance(size, int):
            raise TypeError("Expecting int, got:", type(size))
        if size < 1:
            raise ValueError("Invalid size:", size)
        return random.randint(1, size)

    @staticmethod
    def get_float(size: int=10) -> float:
        """
        Generates a random float.
        @raises: TypeError, ValueError.
        """
        if not isinstance(size, int):
            raise TypeError("Expecting int, got:", type(size))
        if size < 1:
            raise ValueError("Invalid size:", size)
        return random.uniform(1, size)

    @staticmethod
    def get_probability() -> float:
        """
        Generates a random probability.
        """
        return random.uniform(0, 1)

    @staticmethod
    def get_bool() -> bool:
        """
        Generates a random boolean.
        """
        return random.choice([True, False])

    @staticmethod
    def get_choice(values: list) -> object:
        """
        Returns a random value from a list.
        @raises: ValueError.
        """
        if not isinstance(values, (list, tuple)):
            raise TypeError("Expecting list, got:", type(values))
        return random.choice(list_of_values)

    @staticmethod
    def get_random_event(probability: float):
        """
        Returns True if the random probability
        is higher than $probability.
        @raises: TypeError, ValueError.
        """
        if not isinstance(probability, float):
            raise TypeError("Expecting float, got:", type(probability))
        if size < 0 or size > 1:
            raise ValueError("Invalid probability:", probability)
        return random_probability() <= probability

    @staticmethod
    def get_uuid():
        """
        Generates a unique UUID.
        """
        return uuid.uuid4().hex
