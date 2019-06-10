"""
User Model.

Password is hashed using hashlib.SHA256.
They are not stored as raw text in the DB.
"""

import hashlib

from . import db

from flask_login import UserMixin
from sqlalchemy.orm import validates


class User(db.Model, UserMixin):
    """
    User Model.
    """

    __tablename__ = 'entity_user'

    id = db.Column(db.Integer, primary_key=True)
    is_active = db.Column(db.Boolean, default=True, index=True)
    username = db.Column(db.String(255), nullable=False, index=True)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __str__(self) -> str:
        """
        String serializer.
        """
        return "<User: '{}'>".format(self.username)

    @staticmethod
    def __hash(x: str) -> str:
        """
        Hases a string.
        @raises: ValueError, TypeError.
        """
        if not x:
            raise ValueError("Invalid value.")
        if not isinstance(x, str):
            raise TypeError("Expecting str, got:", type(x))
        return hashlib.sha256(x.encode()).hexdigest()

    def is_password_valid(self, password: str=None) -> bool:
        """
        Validates if user password matches.
        @raises: ValueError, TypeError.
        """
        if not password:
            raise ValueError("Invalid password.")
        if not isinstance(password, str):
            raise TypeError("Expecting str, got:", type(password))
        return self.__hash(password) == self.password

    @validates("username")
    def validate_username(self, key: str, value: str):
        """
        Validating username.
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

    @validates("password")
    def validate_password(self, key: str, value: str):
        """
        Validating password.
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
        return self.__hash(value)
