"""
Application API constants.

Users expect these strings in the response.
As a consequence, using a different constant
will require a new API version.
"""


class Health(object):
    """
    Health constants.
    """
    STATUS = "status"
    ALIVE = "alive"
    WARNING = "warning"


class Error(object):
    """
    Error constants.
    """
    SINGULAR = "error"
    PLURAL = "errors"


class Pagination(object):
    """
    Pagination constants.
    """
    LIMIT = "limit"
    PAGE = "page"


class Auth(object):
    """
    Authentication constants.
    """
    USERNAME = "username"
    PASSWORD = "password"
    TOKEN = "token"


class Person(object):
    """
    Person constants.
    """
    SINGULAR = "person"
    PLURAL = "people"
    ID = "id"
    CREATED_AT = "created_at"
    FIRST_NAME = "first_name"
    LAST_NAME = "last_name"
    ACTIVE = "is_active"
    ALIASES = "aliases"


class Movie(object):
    """
    Movie constants.
    """
    SINGULAR = "movie"
    PLURAL = "movies"
    ID = "id"
    ACTIVE = "is_active"
    TITLE = "title"
    CREATED_AT = "created_at"
    RELEASED_AT = "released_at"

    class Release(object):
        """
        Movie Release constants.
        """
        YEAR = "year"
        DATE = "date"
        ROMAN = "roman"


class Actor(object):
    """
    Movie Actor/Actress constants.
    """
    SINGULAR = "actor"
    PLURAL = "actors"


class Producer(object):
    """
    Movie Producer constants.
    """
    SINGULAR = "producer"
    PLURAL = "producers"


class Director(object):
    """
    Movie Director constants.
    """
    SINGULAR = "director"
    PLURAL = "directors"
