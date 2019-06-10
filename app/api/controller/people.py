"""
People Controller.
"""

import logging
import typing

from .models.person import Person, Alias
from .models import db

from . import Controller, ControllerException

logger = logging.getLogger(__name__)


class PersonException(ControllerException):
    """
    Parent class for all exceptions in this library.
    """


class FirstNameException(PersonException):
    """
    Raised if first name is invalid.
    """


class PageException(PersonException):
    """
    Raised if page number is invalid.
    """


class LimitException(PersonException):
    """
    Raised if page limit is invalid.
    """


class LastNameException(PersonException):
    """
    Raised if last name is invalid.
    """


class PersonIDException(PersonException):
    """
    Raised if person ID is invalid.
    """


class PersonNotFoundException(PersonException):
    """
    Raised if person ID is invalid.
    """


class AliasException(PersonException):
    """
    Raised if alias is invalid.
    """


class AliasTakenException(PersonException):
    """
    Raised if alias is already taken.
    """


class PeopleController(Controller):
    """
    People controller business layer.
    """

    @staticmethod
    def get_by_id(person_id: str=None) -> Person:
        """
        Load person by person id.
        @raises: PersonIDException, PersonNotFoundException.
        """
        logger.debug("Loading person by ID '%s'.", person_id)
        if not person_id or not isinstance(person_id, (int, str)):
            raise PersonIDException()
        person = Person.query.filter_by(id=person_id, is_active=True).first()
        if not person:
            raise PersonNotFoundException()
        logger.debug("Person found: '%s'.", person)
        return person

    @staticmethod
    def get_aliases_by_person_id(person_id: int=None) -> typing.Generator:
        """
        For a given person ID, returns a list of aliases.
        @raises: PersonIDException.
        """
        logger.debug("Loading person aliases by ID '%s'.", person_id)
        if not person_id or not isinstance(person_id, (int, str)):
            raise PersonIDException()
        query = Alias.query.filter_by(person_id=person_id)
        yield from (
            alias
            for alias in query.all()
        )
        logger.debug("All aliases found for person ID '%s'.", person_id)

    @staticmethod
    def get_aliases_by_value(*aliases) -> typing.Generator:
        """
        For a list of aliases, returns the existing Alias objects.
        @raises: AliasException.
        """
        logger.debug("Loading aliases by name: '%s'.", aliases)
        bad_aliases = [
            alias
            for alias in aliases
            if not alias or not isinstance(alias, str)
        ]
        if bad_aliases:
            raise AliasException(bad_aliases)
        if not aliases:
            raise AliasException()
        query = Alias.query.filter(Alias.value.in_(aliases))
        yield from (
            alias
            for alias in query.all()
        )
        logger.debug("Aliases by name loaded: '%s'.", aliases)

    @classmethod
    def create(cls,
               first_name: str=None,
               aliases: list=None,
               is_active: bool=True,
               last_name: str=None) -> Person:
        """
        Create a new Person.
        @raises: FirstNameException, LastNameException,
                 AliasTakenException, AliasException.
        """
        logger.debug("Creating Person: '%s %s'.", first_name, last_name)
        if not first_name or not isinstance(first_name, str):
            raise FirstNameException()
        if not last_name or not isinstance(last_name, str):
            raise LastNameException()
        if not aliases or not isinstance(aliases, list):
            raise AliasException()
        # Check if any of the aliases is taken.
        aliases_taken = [
            alias.value
            for alias in cls.get_aliases_by_value(*aliases)
        ]
        if aliases_taken:
            raise AliasTakenException(aliases_taken)
        # Creating person.
        person = Person(first_name=first_name, last_name=last_name)
        person.is_active = is_active
        db.session.add(person)
        db.session.commit()
        # Adding aliases.
        for alias in aliases:
            new_alias = cls.add_alias_to_person_by_id(person_id=person.id,
                                                      alias=alias)
        db.session.commit()
        logger.debug("Person created: '%s'.", person)
        return person

    @staticmethod
    def add_alias_to_person_by_id(person_id: int=None,
                                  alias: str=None) -> Alias:
        """
        Add Alias to Person.
        WARNING: The change is not commited.
        @raises: PersonIDException, AliasException.
        """
        logger.debug("Adding alias '%s' to person ID '%s'.",
                     alias, person_id)
        if not person_id or not isinstance(person_id, (int, str)):
            raise PersonIDException()
        if not alias or not isinstance(alias, str):
            raise AliasException(alias)
        new_alias = Alias(person_id=person_id, value=alias)
        db.session.add(new_alias)
        logger.debug("Added alias '%s' to person ID '%s'.", alias, person_id)
        return new_alias

    @classmethod
    def update(cls,
               first_name: str=None,
               aliases: list=None,
               person_id: int=None,
               is_active: bool=None,
               last_name: str=None) -> Person:
        """
        Create a new Person.
        @raises: FirstNameException, LastNameException,
                 PersonIDException, PersonNotFoundException,
                 AliasTakenException, AliasException.
        """
        logger.debug("Updating Person: '%s %s'.", first_name, last_name)
        if first_name and not isinstance(first_name, str):
            raise FirstNameException()
        if last_name and not isinstance(last_name, str):
            raise LastNameException()
        if aliases and not isinstance(aliases, list):
            raise AliasException()
        # Check if any of the aliases is taken.
        if aliases:
            aliases_taken = [
                alias.value
                for alias in cls.get_aliases_by_value(*aliases)
                if alias.person_id != person_id
            ]
            if aliases_taken:
                raise AliasTakenException(aliases_taken)
        # Searching for person by ID.
        person = cls.get_by_id(person_id)
        if not person:
            raise PersonNotFoundException()
        # Updating Person.
        person.first_name = first_name or person.first_name
        person.last_name = last_name or person.last_name
        person.is_active = is_active if is_active is not None else person.is_active
        db.session.add(person)
        db.session.commit()
        # Adding aliases.
        if aliases:
            for alias in aliases:
                new_alias = cls.add_alias_to_person_by_id(person_id=person.id,
                                                          alias=alias)
        db.session.commit()
        logger.debug("Person updated: '%s'.", person)
        return person

    @classmethod
    def delete(cls, person_id: int=None) -> Person:
        """
        Deleting a Person will always deactive it.
        """
        logger.debug("Deactivating Person: '%s'.", person_id)
        person = cls.update(person_id=person_id, is_active=False)
        logger.debug("Person deactivated: '%s'.", person_id)
        return person

    @staticmethod
    def search(page: int=0, limit: int=50) -> typing.Generator:
        """
        Listing & paginatin people.
        @raises: PageException, LimitException.
        """
        logger.debug("Listing People page %s limit %s.", page, limit)
        if not isinstance(page, int) or page < 0:
            raise PageException()
        if not isinstance(limit, int) or limit < 1 or limit > 200:
            raise LimitException()
        query = Person.query.paginate(page=page, max_per_page=limit)
        yield from (
            person
            for person in query.items
        )
        logger.debug("Listed People page %s limit %s. Total %s.",
                     page, limit, query.total)
