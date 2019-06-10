"""
Testing app.api.controller.people library.
"""

import unittest
from unittest.mock import patch

from app.api.controller import people

from .utils.random import Random

from .mocks.queries import QueryMock
from .mocks.db import DatabaseMock
from .mocks.models import PersonMock, AliasMock


class TestGetPersonByID(unittest.TestCase):
    """
    Testing PeopleController class.
    """

    def test_arguments(self) -> None:
        """
        Test people.PeopleController.get_by_id() arguments.
        """
        with self.assertRaises(people.PersonIDException):
            people.PeopleController.get_by_id()
        with self.assertRaises(people.PersonIDException):
            people.PeopleController.get_by_id([])

    @patch.object(people, 'Person', QueryMock(None))
    def test_not_found(self) -> None:
        """
        Test people.PeopleController.get_by_id().
        Try a query without results.
        """
        with self.assertRaises(people.PersonNotFoundException):
            people.PeopleController.get_by_id(Random.get_int())
        with self.assertRaises(people.PersonNotFoundException):
            people.PeopleController.get_by_id(Random.get_str())

    @patch.object(people, 'Person', QueryMock(PersonMock()))
    def test_found(self) -> None:
        """
        Test people.PeopleController.get_by_id().
        Try a query with results.
        """
        person = people.PeopleController.get_by_id(Random.get_int())
        self.assertTrue(person.first_name)
        self.assertTrue(person.last_name)


class TestCreatePerson(unittest.TestCase):
    """
    Testing PeopleController class.
    """

    def test_arguments(self) -> None:
        """
        Test people.PeopleController.create() arguments.
        """
        with self.assertRaises(people.FirstNameException):
            people.PeopleController.create()
        with self.assertRaises(people.FirstNameException):
            people.PeopleController.create(first_name=Random.get_int())
        with self.assertRaises(people.LastNameException):
            people.PeopleController.create(first_name=Random.get_str())
        with self.assertRaises(people.LastNameException):
            people.PeopleController.create(first_name=Random.get_str(),
                                           last_name=Random.get_int())
        with self.assertRaises(people.AliasException):
            people.PeopleController.create(first_name=Random.get_str(),
                                           last_name=Random.get_str())
        with self.assertRaises(people.AliasException):
            people.PeopleController.create(first_name=Random.get_str(),
                                           last_name=Random.get_str(),
                                           aliases=Random.get_int())

    @patch.object(people.PeopleController,
                  "get_aliases_by_value",
                  return_value=[AliasMock(), AliasMock()])
    def test_alias_taken(self, _) -> None:
        """
        Test people.PeopleController.create().
        Alias is already taken.
        """
        with self.assertRaises(people.AliasTakenException):
            people.PeopleController.create(first_name=Random.get_str(),
                                           last_name=Random.get_str(),
                                           aliases=[Random.get_str()])

    @patch.object(people.PeopleController, "get_aliases_by_value", return_value=[])
    @patch.object(people.PeopleController, "add_alias_to_person_by_id")
    @patch.object(people, "Person", PersonMock)
    @patch.object(people, "db", DatabaseMock())
    def test_created(self, _1, _2) -> None:
        """
        Test people.PeopleController.create().
        """
        person = people.PeopleController.create(first_name=Random.get_str(),
                                                last_name=Random.get_str(),
                                                aliases=[Random.get_str()])
        self.assertTrue(person.first_name)
        self.assertTrue(person.last_name)
        self.assertTrue(person.created_at)


class TestUpdatePerson(unittest.TestCase):
    """
    Testing PeopleController class.
    """

    def test_arguments(self) -> None:
        """
        Test people.PeopleController.update() arguments.
        """
        with self.assertRaises(people.PersonIDException):
            people.PeopleController.update(person_id=Random.get_float())
        with self.assertRaises(people.FirstNameException):
            people.PeopleController.update(first_name=Random.get_int())
        with self.assertRaises(people.LastNameException):
            people.PeopleController.update(first_name=Random.get_str(),
                                           last_name=Random.get_int())
        with self.assertRaises(people.AliasException):
            people.PeopleController.update(first_name=Random.get_str(),
                                           last_name=Random.get_str(),
                                           aliases=Random.get_int())

    @patch.object(people.PeopleController,
                  "get_aliases_by_value",
                  return_value=[AliasMock(), AliasMock()])
    def test_alias_taken(self, _1) -> None:
        """
        Test people.PeopleController.update().
        Alias is already taken.
        """
        with self.assertRaises(people.AliasTakenException):
            people.PeopleController.update(first_name=Random.get_str(),
                                           last_name=Random.get_str(),
                                           aliases=[Random.get_str()])

    @patch.object(people.PeopleController, "get_by_id", return_value=PersonMock())
    @patch.object(people.PeopleController, "get_aliases_by_value", return_value=[])
    @patch.object(people.PeopleController, "add_alias_to_person_by_id")
    @patch.object(people, "Person", PersonMock)
    @patch.object(people, "db", DatabaseMock())
    def test_updated(self, _1, _2, _3) -> None:
        """
        Test people.PeopleController.update().
        """
        person = people.PeopleController.update(first_name=Random.get_str(),
                                                person_id=Random.get_str(),
                                                last_name=Random.get_str(),
                                                aliases=[Random.get_str()])
        self.assertTrue(person.first_name)
        self.assertTrue(person.last_name)
        self.assertTrue(person.created_at)

    @patch.object(people.PeopleController, "get_by_id", return_value=None)
    @patch.object(people.PeopleController, "get_aliases_by_value", return_value=[])
    @patch.object(people, "Person", PersonMock)
    @patch.object(people, "db", DatabaseMock())
    def test_not_found(self, _1, _2) -> None:
        """
        Test people.PeopleController.update().
        """
        with self.assertRaises(people.PersonNotFoundException):
            people.PeopleController.update(first_name=Random.get_str(),
                                           person_id=Random.get_str(),
                                           last_name=Random.get_str(),
                                           aliases=[Random.get_str()])


class TestDeletePerson(unittest.TestCase):
    """
    Testing PeopleController class.
    """

    def test_arguments(self) -> None:
        """
        Test people.PeopleController.delete() arguments.
        """
        with self.assertRaises(people.PersonIDException):
            people.PeopleController.delete()
        with self.assertRaises(people.PersonIDException):
            people.PeopleController.delete(person_id=Random.get_float())

    @patch.object(people.PeopleController, "get_by_id", return_value=PersonMock())
    @patch.object(people, "Person", PersonMock)
    @patch.object(people, "db", DatabaseMock())
    def test_deleted(self, _1) -> None:
        """
        Test people.PeopleController.delete().
        """
        person = people.PeopleController.delete(person_id=Random.get_str())
        self.assertTrue(person.first_name)
        self.assertTrue(person.last_name)
        self.assertTrue(person.created_at)

    @patch.object(people.PeopleController, "get_by_id", return_value=None)
    @patch.object(people, "Person", PersonMock)
    @patch.object(people, "db", DatabaseMock())
    def test_not_found(self, _1) -> None:
        """
        Test people.PeopleController.delete().
        """
        with self.assertRaises(people.PersonNotFoundException):
            people.PeopleController.delete(person_id=Random.get_str())


class TestListPeople(unittest.TestCase):
    """
    Testing PeopleController class.
    """

    def test_arguments(self) -> None:
        """
        Test people.PeopleController.search() arguments.
        """
        with self.assertRaises(people.PageException):
            list(people.PeopleController.search(page=-1 * Random.get_int()))
        with self.assertRaises(people.PageException):
            list(people.PeopleController.search(page=Random.get_float()))
        with self.assertRaises(people.PageException):
            list(people.PeopleController.search(page=Random.get_str()))
        with self.assertRaises(people.LimitException):
            list(people.PeopleController.search(limit=-1 * Random.get_int()))
        with self.assertRaises(people.LimitException):
            list(people.PeopleController.search(limit=Random.get_float()))
        with self.assertRaises(people.LimitException):
            list(people.PeopleController.search(limit=Random.get_str()))

    @patch.object(people, 'Person', QueryMock(None))
    def test_not_found(self) -> None:
        """
        Test people.PeopleController.list().
        Try a query without results.
        """
        results = list(people.PeopleController.search())
        self.assertIsInstance(results, list)
        self.assertFalse(results)

    @patch.object(people, 'Person', QueryMock(PersonMock()))
    def test_not_found(self) -> None:
        """
        Test people.PeopleController.search().
        Try a query with results.
        """
        results = list(people.PeopleController.search())
        self.assertIsInstance(results, list)
        self.assertTrue(results)
