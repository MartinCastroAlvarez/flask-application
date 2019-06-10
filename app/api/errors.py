"""
Application error codes.

Any client can rely on error codes and subcodes
to show different errors to the user.
There is no dependency on error text, for i18n purposes.
"""

import logging

logger = logging.getLogger()


class MariaException(Exception):
    """
    Maria App parent exception.
    Raised only when an unexpeted error occurs.
    """
    CODE = 500
    SUBCODE = 5000
    MESSAGE = "Unexpected error ocurred."

    def __init__(self, *errors) -> None:
        """
        Initializing exception with custom errors.
        """
        self.__errors = errors
        logger.error("Error on API layer. [%s] %s", self, errors)

    @property
    def code(self) -> int:
        """
        Status code getter.
        """
        return self.CODE

    @property
    def subcode(self) -> int:
        """
        Subcode getter.
        """
        return self.SUBCODE

    def to_str(self) -> str:
        """
        String serializer.
        """
        return " ".join([
            self.MESSAGE,
            "".join([
                str(error)
                for error in self.__errors
            ])
        ]).strip()

    def to_json(self) -> dict:
        """
        JSON serializer.
        """
        return {
            self.subcode: self.to_str(),
        }


class MethodNotImplementedException(MariaException):
    """
    Raised if API method is not implemented.
    """
    CODE = 405
    SUBCODE = 5001
    MESSAGE = "Method not allowed."


class EndpointNotFoundException(MariaException):
    """
    Raised if API endpoint is not implemented.
    """
    CODE = 404
    SUBCODE = 5002
    MESSAGE = "Endpoint not found."


class AuthException(MariaException):
    """
    Exceptions related to autentication.
    """
    CODE = 403
    SUBCODE = 3000
    MESSAGE = "Authentication error."


class UserNotFoundAuthException(AuthException):
    """
    Raise when username doesn't exist in DB.
    """
    SUBCODE = 3001
    MESSAGE = "Username not found."


class InvalidPasswordAuthException(AuthException):
    """
    Raise when password is invalid.
    """
    SUBCODE = 3002
    MESSAGE = "Invalid password."


class FormException(MariaException):
    """
    Exceptions related to form validations.
    """
    CODE = 400
    SUBCODE = 4000
    MESSAGE = "Bad input."


class FirstNameFormException(FormException):
    """
    Raised when first name is invalid.
    """
    SUBCODE = 4001
    MESSAGE = "First name is invalid."


class LastNameFormException(FormException):
    """
    Raised when last name is invalid.
    """
    SUBCODE = 4002
    MESSAGE = "Last name is invalid."


class AliasFormException(FormException):
    """
    Raised when alias is invalid.
    """
    SUBCODE = 4003
    MESSAGE = "Alias is invalid."


class TitleFormException(FormException):
    """
    Raised when title is invalid.
    """
    SUBCODE = 4004
    MESSAGE = "Title is invalid."


class UsernameFormError(FormException):
    """
    Raised when username is invalid.
    """
    SUBCODE = 4005
    MESSAGE = "Username is invalid."


class PasswordFormError(FormException):
    """
    Raised when password is invalid.
    """
    SUBCODE = 4006
    MESSAGE = "Password is invalid."


class PersonNotFoundException(FormException):
    """
    Raised when person doesn't exist.
    """
    CODE = 404
    SUBCODE = 4007
    MESSAGE = "Person does not exist."


class PageFormException(FormException):
    """
    Raised when page number is not valid.
    """
    SUBCODE = 4008
    MESSAGE = "Invalid page number."


class LimitFormException(FormException):
    """
    Raised when page limit is not valid.
    """
    SUBCODE = 4009
    MESSAGE = "Invalid page limit."


class ReleaseDateFormException(FormException):
    """
    Raised when released date is not valid.
    """
    SUBCODE = 4010
    MESSAGE = "Invalid release date."


class MovieNotFoundException(FormException):
    """
    Raised when movie doesn't exist.
    """
    CODE = 404
    SUBCODE = 401
    MESSAGE = "Person does not exist."


class AliasTakenException(FormException):
    """
    Raised if person alias is already taken.
    """
    CODE = 409
    SUBCODE = 9001
    MESSAGE = "Alias is already taken."
