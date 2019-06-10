"""
Models mocks.
"""

from . import Mock


class PersonMock(Mock):
    """
    Person mock.
    """

    def __init__(self, *args, **kwargs) -> None:
        """
        Model constructor.
        """
        self.id = "PersonMock"
        self.first_name = "PersonMock"
        self.last_name = "PersonMock"
        self.created_at = "PersonMock"
        self.is_active = True


class AliasMock(Mock):
    """
    Alias mock.
    """

    def __init__(self, *args, **kwargs) -> None:
        """
        Model constructor.
        """
        self.id = "PersonMock"
        self.person_id = "PersonMock"
        self.created_at = "PersonMock"
        self.value = "PersonMock"


class MovieMock(Mock):
    """
    Movie mock.
    """

    def __init__(self, *args, **kwargs) -> None:
        """
        Model constructor.
        """
        self.id = "PersonMock"
        self.title = "PersonMock"
        self.released_at = "PersonMock"
        self.created_at = "PersonMock"
        self.is_active = True


class ActorMock(Mock):
    """
    Actor mock.
    """

    def __init__(self, *args, **kwargs):
        """
        Model constructor.
        """
        self.person_id = "PersonMock"
        self.movie_id = "PersonMock"
        self.created_at = "PersonMock"


class DirectorMock(Mock):
    """
    Director mock.
    """

    def __init__(self, *args, **kwargs) -> None:
        """
        Model constructor.
        """
        self.person_id = "PersonMock"
        self.movie_id = "PersonMock"
        self.created_at = "PersonMock"


class ProducerMock(Mock):
    """
    Producer mock.
    """

    def __init__(self, *args, **kwargs) -> None:
        """
        Model constructor.
        """
        self.person_id = "PersonMock"
        self.movie_id = "PersonMock"
        self.created_at = "PersonMock"


class UserMock(Mock):
    """
    User mock.
    """

    SESSION = {
        "_id": "MockSession",
    }

    def __init__(self,
                 *args,
                 _is_password_valid=True,
                 _is_active=True,
                 **kwargs) -> None:
        """
        Model constructor.
        """
        self.id = "PersonMock"
        self.username = "PersonMock"
        self.password = "PersonMock"
        self.created_at = "PersonMock"
        self.is_active = _is_active
        self.__is_password_valid = _is_password_valid

    def is_password_valid(self, *args, **kwargs) -> bool:
        """
        Validate if password is valid.
        """
        return self.__is_password_valid
