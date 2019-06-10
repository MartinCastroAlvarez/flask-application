"""
Person Model.
"""

from . import db

from sqlalchemy.orm import relationship, validates
from sqlalchemy.schema import ForeignKey


class Person(db.Model):
    """
    Person Model.
    """

    __tablename__ = 'entity_person'

    id = db.Column(db.Integer, primary_key=True)
    is_active = db.Column(db.Boolean, default=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    movies_as_actor = relationship('Movie', secondary='movie_actor')
    movies_as_producer = relationship('Movie', secondary='movie_producer')
    movies_as_director = relationship('Movie', secondary='movie_director')
    aliases = relationship('Alias')

    def __str__(self) -> str:
        """
        String serializer.
        """
        return "<Person: '{} {}'>".format(self.first_name, self.last_name)

    @validates("first_name")
    def validate_first_name(self, key: str, value: str):
        """
        Validating first name.
        @raises: ValueError, TypeError.
        """
        if not value:
            raise ValueError("Invalid value.")
        if not isinstance(value, str):
            raise ValueError("Expecting str, got:", type(value))
        if len(value) > 255:
            raise ValueError("Too long:", value)
        if len(value) < 5:
            raise ValueError("Too short:", value)
        return value

    @validates("last_name")
    def validate_last_name(self, key: str, value: str):
        """
        Validating last name.
        @raises: ValueError, TypeError.
        """
        if not value:
            raise ValueError("Invalid value.")
        if not isinstance(value, str):
            raise ValueError("Expecting str, got:", type(value))
        if len(value) > 255:
            raise ValueError("Too long:", value)
        if len(value) < 5:
            raise ValueError("Too short:", value)
        return value


class Alias(db.Model):
    """
    Person Alias Model.
    """

    __tablename__ = 'entity_person_alias'

    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer,
                          ForeignKey("entity_person.id"),
                          nullable=False)
    value = db.Column(db.String(255),
                      nullable=False,
                      unique=True,
                      index=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __str__(self) -> str:
        """
        String serializer.
        """
        return "<Alias: '{}'>".format(self.value)

    @validates("value")
    def validate_value(self, key: str, value: str):
        """
        Validating value.
        @raises: ValueError, TypeError.
        """
        if not value:
            raise ValueError("Invalid value.")
        if not isinstance(value, str):
            raise ValueError("Expecting str, got:", type(value))
        if len(value) > 255:
            raise ValueError("Too long:", value)
        if len(value) < 5:
            raise ValueError("Too short:", value)
        return value
