"""
Main Flask app.

This file is required by the Docker image:
https://github.com/tiangolo/uwsgi-nginx-flask-docker
"""

import logging

from config import Config
from urls import URL

from flask import Flask, url_for, redirect

import api.health
import api.auth
import api.people
import api.movies
import api.roles

from api.controller.auth import login_manager, AuthController
from api.controller.models import db

logger = logging.getLogger(__name__)


def create_app() -> Flask:
    """
    Flask Factory pattern.

    Reference:
    http://flask.pocoo.org/docs/1.0/patterns/appfactories/
    """
    app = Flask(__name__)
    app.url_map.strict_slashes = False

    # Secret Key is required by Flask-Session.
    app.secret_key = Config.get(Config.SECRET)

    # Updating logger messages.
    logger.debug("Initializing logger.")
    LOGGER_FORMAT = '%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)s] %(message)s'
    app.debug = Config.get(Config.DEBUG)
    LEVEL = logging.DEBUG if app.debug else logging.INFO
    logging.basicConfig(level=LEVEL, format=LOGGER_FORMAT)
    logger.debug("Logger initialized!")
    del LEVEL, LOGGER_FORMAT

    # Loading Login Manager.
    # It can be convenient to globally turn off authentication
    # when unit testing. To enable this, if the application
    # configuration variable LOGIN_DISABLED is set to True,
    # this decorator will be ignored.
    logger.debug("Initializing login manager.")
    app.config[Config.LOGIN_DISABLED] = Config.get(Config.LOGIN_DISABLED)
    login_manager.init_app(app)
    logger.debug("Login manager initialized!")

    # Loading DB connector.
    logger.debug("Initializing connection with DB.")
    DB_CFG = [
        Config.get(Config.DB_USER),
        Config.get(Config.DB_PASS),
        Config.get(Config.DB_HOST),
        Config.get(Config.DB_PORT),
        Config.get(Config.DB_NAME),
    ]
    uri = 'postgresql+psycopg2://{}:{}@{}:{}/{}'.format(*DB_CFG)
    app.config[Config.DB_URI] = uri
    app.config[Config.DB_TRACK] = False
    del DB_CFG, uri
    db.init_app(app)
    with app.app_context():
        db.create_all()
        db.session.commit()
    logger.debug("Connection with DB initialized!")

    # Creating an admin.
    # WARNING: This piece of code has been created for the demo.
    #          This user will be used for testing purposes.
    if Config.get(Config.ADMIN_PASSWORD):
        with app.app_context():
            logger.warning("Setting admin password.")
            AuthController.create_admin(password=Config.get(Config.ADMIN_PASSWORD),
                                        username=Config.get(Config.ADMIN_USERNAME))
            logger.warning("Admin password updated!")

    # Registering app views.
    logger.debug("Registering views.")
    app.add_url_rule(URL.HEALTH, view_func=api.health.HealthAPI.as_view('health'))
    app.add_url_rule(URL.AUTH, view_func=api.auth.AuthAPI.as_view('auth'))
    app.add_url_rule(URL.PEOPLE, view_func=api.people.PeopleAPI.as_view('people'))
    app.add_url_rule(URL.PERSON, view_func=api.people.PersonAPI.as_view('person'))
    app.add_url_rule(URL.MOVIES, view_func=api.movies.MoviesAPI.as_view('movies'))
    app.add_url_rule(URL.MOVIE, view_func=api.movies.MovieAPI.as_view('movie'))
    app.add_url_rule(URL.MOVIE_ACTORS,
                     view_func=api.roles.ActorAPI.as_view('movie_actor'))
    app.add_url_rule(URL.MOVIE_DIRECTORS,
                     view_func=api.roles.ProducerAPI.as_view('movie_producer'))
    app.add_url_rule(URL.MOVIE_PRODUCERS,
                     view_func=api.roles.DirectorAPI.as_view('movie_director'))
    app.add_url_rule(URL.PERSON_ACTOR_ROLES,
                     view_func=api.roles.ActorAPI.as_view('actor_movie'))
    app.add_url_rule(URL.PERSON_PRODUCER_ROLES,
                     view_func=api.roles.ProducerAPI.as_view('producer_movie'))
    app.add_url_rule(URL.PERSON_DIRECTOR_ROLES,
                     view_func=api.roles.DirectorAPI.as_view('director_movie'))
    logger.debug("All views registered.")

    # Adding index vies.
    @app.route(URL.INDEX)
    def index():
        """
        Redirecting all requests to the UI.
        """
        logger.debug("Redirecting all traffic to the index.")
        return redirect(url_for("health"))

    # End of app factory.
    logger.info("App started!")
    return app

app = create_app()
if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=5000)
