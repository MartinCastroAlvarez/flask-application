"""
Testing app.api.controller.people library.
"""

import unittest
from unittest.mock import patch

from app.api.controller import people

from .utils.random import Random

from .mocks.queries import QueryMock
from .mocks.models import AliasMock
from .mocks.db import DatabaseMock


class TestGetAliasesByPersonID(unittest.TestCase):
    """
    Testing PeopleController Aliases class.
    """

    def test_arguments(self) -> None:
        """
        Test people.PeopleController.get_aliases_by_person_id() arguments.
        """
        with self.assertRaises(people.PersonIDException):
            list(people.PeopleController.get_aliases_by_person_id())
        with self.assertRaises(people.PersonIDException):
            list(people.PeopleController.get_aliases_by_person_id([]))

    @patch.object(people, 'Alias', QueryMock(None))
    def test_not_found(self) -> None:
        """
        Test people.PeopleController.get_aliases_by_person_id().
        Try a query without results.
        """
        aid = Random.get_int()
        aliases = people.PeopleController.get_aliases_by_person_id(aid)
        aliases = list(aliases)
        self.assertIsInstance(aliases, list)
        self.assertFalse(aliases)
        aid = Random.get_str()
        aliases = people.PeopleController.get_aliases_by_person_id(aid)
        aliases = list(aliases)
        self.assertIsInstance(aliases, list)
        self.assertFalse(aliases)

    @patch.object(people, 'Alias', QueryMock(AliasMock()))
    def test_found(self) -> None:
        """
        Test people.PeopleController.get_aliases_by_person_id().
        Try a query with results.
        """
        aid = Random.get_int()
        aliases = people.PeopleController.get_aliases_by_person_id(aid)
        aliases = list(aliases)
        self.assertIsInstance(aliases, list)
        self.assertTrue(aliases[0].value)
        self.assertTrue(aliases[0].person_id)


class TestGetAliasesByValue(unittest.TestCase):
    """
    Testing PeopleController Aliases class.
    """

    def test_arguments(self) -> None:
        """
        Test people.PeopleController.get_aliases_by_value() arguments.
        """
        with self.assertRaises(people.AliasException):
            list(people.PeopleController.get_aliases_by_value())
        with self.assertRaises(people.AliasException):
            list(people.PeopleController.get_aliases_by_value(1, 2))

    @patch.object(people, 'Alias', QueryMock(None))
    def test_not_found(self) -> None:
        """
        Test people.PeopleController.get_aliases_by_value().
        Try a query without results.
        """
        values = Random.get_str(), Random.get_str()
        aliases = people.PeopleController.get_aliases_by_value(*values)
        aliases = list(aliases)
        self.assertIsInstance(aliases, list)
        self.assertFalse(aliases)

    @patch.object(people, 'Alias', QueryMock(AliasMock()))
    def test_found(self) -> None:
        """
        Test people.PeopleController.get_aliases_by_value().
        Try a query with results.
        """
        values = Random.get_str(), Random.get_str()
        aliases = people.PeopleController.get_aliases_by_value(*values)
        aliases = list(aliases)
        self.assertIsInstance(aliases, list)
        self.assertTrue(aliases[0].value)
        self.assertTrue(aliases[0].person_id)


class TestAddAliasesToPerson(unittest.TestCase):
    """
    Testing PeopleController Aliases class.
    """

    def test_arguments(self) -> None:
        """
        Test people.PeopleController.add_alias_to_person_by_id() args.
        """
        with self.assertRaises(people.PersonIDException):
            people.PeopleController.add_alias_to_person_by_id()
        with self.assertRaises(people.AliasException):
            people.PeopleController.add_alias_to_person_by_id(Random.get_str())
        with self.assertRaises(people.AliasException):
            people.PeopleController.add_alias_to_person_by_id(1, 2)

    @patch.object(people, 'Alias', AliasMock)
    @patch.object(people, "db", DatabaseMock())
    def test_added(self) -> None:
        """
        Test people.PeopleController.add_alias_to_person_by_id().
        """
        person_id = Random.get_str()
        value = Random.get_str()
        query = dict(person_id=person_id, alias=value)
        alias = people.PeopleController.add_alias_to_person_by_id(**query)
        self.assertIsInstance(alias, AliasMock)
        self.assertTrue(alias.value)
        self.assertTrue(alias.person_id)
