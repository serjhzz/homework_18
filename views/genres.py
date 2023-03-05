from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import genre_service
from log_handler import views_logger

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresViews(Resource):
    """
    GenresView Class Based View (CBV).
    """

    def get(self) -> tuple:
        """
        GET request handler for all genres.
        :return: Genres json.
        """
        views_logger.info('Retrieving all genres')
        genres = genre_service.get_all()
        result = GenreSchema(many=True).dump(genres)
        views_logger.debug('Retrieved %s genres', len(genres))
        return result, 200


@genre_ns.route('/<int:gid>/')
class GenreViews(Resource):
    """
    GenreView Class Based View (CBV).
    """

    def get(self, gid: int) -> tuple:
        """
        GET request handler for one genre by id.
        :param gid: Genre id.
        :return: Genre json.
        """
        views_logger.info('Retrieving genre with id %s', gid)
        genre = genre_service.get_one(gid)
        result = GenreSchema(many=True).dump(genre)
        views_logger.debug('Retrieved genre: %s', genre)
        return result, 200
