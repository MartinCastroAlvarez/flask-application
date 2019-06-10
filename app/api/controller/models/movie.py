"""
Movie Model.
"""

from . import db
from .utils import Roman

from sqlalchemy.orm import relationship, validates
from sqlalchemy.schema import ForeignKey


class Movie(db.Model):
    """
    Movie Model.
    """

    __tablename__ = 'entity_movie'

    id = db.Column(db.Integer, primary_key=True)
    is_active = db.Column(db.Boolean, default=True)
    title = db.Column(db.String(255), nullable=False)
    released_at = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    actors = relationship('Person', secondary='movie_actor')
    directors = relationship('Person', secondary='movie_director')
    producers = relationship('Person', secondary='movie_producer')

    def __str__(self) -> str:
        """
        String serializer.
        """
        return "<Movie: '{}'>".format(self.title)

    @property
    def release_year(self) -> int:
        """
        Release year getter.
        """
        return self.released_at.year

    @property
    def release_roman(self) -> int:
        """
        Release year in Roman.
        """
        return Roman(self.released_at.year).get_roman()

    @validates("title")
    def validate_title(self, key: str, value: str):
        """
        Validating title.
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
