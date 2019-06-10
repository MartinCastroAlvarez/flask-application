"""
Role Model.
"""

from . import db

from sqlalchemy.schema import ForeignKey


class Role(db.Model):
    """
    Movie role model.
    """

    __abstract__ = True


class Actor(Role):
    """
    Movie Actor model.
    """

    __tablename__ = 'movie_actor'

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    person_id = db.Column(db.Integer,
                          ForeignKey("entity_person.id"),
                          primary_key=True)
    movie_id = db.Column(db.Integer,
                         ForeignKey("entity_movie.id"),
                         primary_key=True)

    def __str__(self) -> str:
        """
        String serializer.
        """
        return "<Actor: Movie {}, Person {}>".format(self.movie_id,
                                                     self.person_id)


class Director(Role):
    """
    Movie Director model.
    """

    __tablename__ = 'movie_director'

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    person_id = db.Column(db.Integer,
                          ForeignKey("entity_person.id"),
                          primary_key=True)
    movie_id = db.Column(db.Integer,
                         ForeignKey("entity_movie.id"),
                         primary_key=True)

    def __str__(self) -> str:
        """
        String serializer.
        """
        return "<Director: Movie {}, Person {}>".format(self.movie_id,
                                                        self.person_id)


class Producer(Role):
    """
    Movie Producer model.
    """

    __tablename__ = 'movie_producer'

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    person_id = db.Column(db.Integer,
                          ForeignKey("entity_person.id"),
                          primary_key=True)
    movie_id = db.Column(db.Integer,
                         ForeignKey("entity_movie.id"),
                         primary_key=True)

    def __str__(self) -> str:
        """
        String serializer.
        """
        return "<Producer: Movie {}, Person {}>".format(self.movie_id,
                                                        self.person_id)
