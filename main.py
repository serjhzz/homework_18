from flask import Flask
from flask_restx import Api
from config import Config
from setup_db import db
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movies_ns


def create_app(config_object: Config) -> Flask:
    """
    Create a Flask app.
    :param config_object: Flask config object.
    :return: Configured Flask app
    """
    application = Flask(__name__)
    application.config.from_object(config_object)
    application.app_context().push()
    register_extensions(application)
    return application


def register_extensions(application):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movies_ns)


app = create_app(Config())

if __name__ == '__main__':
    app.run()
