"""
URLs constants.
"""


class URL(object):
    """
    URL endpoint entity.
    """
    INDEX = "/"
    HEALTH = "/health"
    AUTH = "/api/v1/auth"
    PEOPLE = "/api/v1/people"
    PERSON = "/api/v1/people/<int:person_id>"
    MOVIES = "/api/v1/movies"
    MOVIE = "/api/v1/movies/<int:movie_id>"
    MOVIE_ACTORS = "/api/v1/movies/<int:movie_id>/actors/<int:person_id>"
    MOVIE_DIRECTORS = "/api/v1/movies/<int:movie_id>/directors/<int:person_id>"
    MOVIE_PRODUCERS = "/api/v1/movies/<int:movie_id>/producers/<int:person_id>"
    PERSON_ACTOR_ROLES = "/api/v1/people/<int:person_id>/movies/actors/<int:movie_id>"
    PERSON_DIRECTOR_ROLES = "/api/v1/people/<int:person_id>/movies/directors/<int:movie_id>"
    PERSON_PRODUCER_ROLES = "/api/v1/people/<int:person_id>/movies/producers/<int:movie_id>"
