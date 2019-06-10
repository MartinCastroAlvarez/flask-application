"""
People Views.
"""

import logging

from flask_login import login_required
from flask import request

from . import constants, errors, API
from .controller import people
from .serializers import PersonSerializer

logger = logging.getLogger(__name__)


class PeopleAPI(API):
    """
    People API.
    """

    @login_required
    def _post(self) -> dict:
        """
        Create Person.
        Error handling is performed by the parent class method.
        @raises: FirstNameException, LastNameFormException,
                 AliasTakenException,  AliasFormException.
        """
        first_name = request.json.get(constants.Person.FIRST_NAME)
        last_name = request.json.get(constants.Person.LAST_NAME)
        aliases = request.json.get(constants.Person.ALIASES, [])
        is_active = request.json.get(constants.Person.ACTIVE, True)
        try:
            person = people.PeopleController.create(first_name=first_name,
                                                    last_name=last_name,
                                                    is_active=is_active,
                                                    aliases=aliases)
            logger.debug("Person created!")
            return {
                constants.Person.SINGULAR: PersonSerializer.serialize(person),
            }
        except people.FirstNameException:
            raise errors.FirstNameFormException()
        except people.LastNameException:
            raise errors.LastNameFormException()
        except people.AliasException as e:
            raise errors.AliasFormException(e)
        except people.AliasTakenException:
            raise errors.AliasTakenException()

    def _get(self) -> dict:
        """
        Searching for People.
        Error handling is performed by the parent class method.
        @raises: LimitFormException, PageFormException.
        """
        logger.debug("Searching for People.")
        page = int(request.args.get(constants.Pagination.PAGE, 1))
        limit = int(request.args.get(constants.Pagination.LIMIT, 30))
        try:
            results = people.PeopleController.search(page=page, limit=limit)
            logger.debug("People listed!")
            return {
                constants.Person.PLURAL: [
                    PersonSerializer.serialize(person)
                    for person in results
                ]
            }
        except people.PageException:
            raise errors.PageFormException()
        except people.LimitException:
            raise errors.LimitFormException()


class PersonAPI(API):
    """
    Person API.
    """

    @login_required
    def _put(self, person_id: int) -> dict:
        """
        Update Person.
        Error handling is performed by the parent class method.
        @raises: FirstNameException, LastNameFormException,
                 AliasTakenException,  AliasFormException,
                 PersonNotFoundException.
        """
        logger.debug("Updating Person.")
        first_name = request.json.get(constants.Person.FIRST_NAME)
        last_name = request.json.get(constants.Person.LAST_NAME)
        aliases = request.json.get(constants.Person.ALIASES, [])
        is_active = request.json.get(constants.Person.ACTIVE, True)
        try:
            person = people.PeopleController.update(first_name=first_name,
                                                    last_name=last_name,
                                                    person_id=person_id,
                                                    is_active=is_active,
                                                    aliases=aliases)
            logger.debug("Person Updated!")
            return {
                constants.Person.SINGULAR: PersonSerializer.serialize(person),
            }
        except people.FirstNameException:
            raise errors.FirstNameFormException()
        except people.LastNameException:
            raise errors.LastNameFormException()
        except people.PersonIDException:
            raise errors.PersonNotFoundException()
        except people.PersonNotFoundException:
            raise errors.PersonNotFoundException()
        except people.AliasException as e:
            raise errors.AliasFormException(e)
        except people.AliasTakenException:
            raise errors.AliasTakenException()

    def _get(self, person_id: int) -> dict:
        """
        Getting Person.
        Error handling is performed by the parent class method.
        @raises: PersonNotFoundException.
        """
        logger.debug("Getting Person.")
        try:
            person = people.PeopleController.get_by_id(person_id=person_id)
            logger.debug("Person loaded!")
            return {
                constants.Person.SINGULAR: PersonSerializer.serialize(person),
            }
        except people.PersonIDException:
            raise errors.PersonNotFoundException()
        except people.PersonNotFoundException:
            raise errors.PersonNotFoundException()

    @login_required
    def _delete(self, person_id: int) -> dict:
        """
        Deleting Person.
        Error handling is performed by the parent class method.
        @raises: PersonNotFoundException.
        """
        logger.debug("Deleting Person.")
        try:
            person = people.PeopleController.delete(person_id=person_id)
            logger.debug("Person deleted!")
            return {
                constants.Person.SINGULAR: PersonSerializer.serialize(person),
            }
        except people.PersonIDException:
            raise errors.PersonNotFoundException()
        except people.PersonNotFoundException:
            raise errors.PersonNotFoundException()
