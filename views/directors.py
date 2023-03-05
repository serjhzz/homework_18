from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from implemented import director_service
from log_handler import views_logger

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsViews(Resource):
    """
    DirectorsView Class Based View (CBV).
    """

    def get(self) -> tuple:
        """
        GET request handler for all directors.
        :return: Directors json.
        """
        views_logger.info('Getting all directors...')
        directors = director_service.get_all()
        result = DirectorSchema(many=True).dump(directors)
        views_logger.info('Returned %s directors', len(directors))
        return result, 200


@director_ns.route('/<int:did>/')
class DirectorViews(Resource):
    """
    DirectorView Class Based View (CBV).
    """

    def get(self, did: int) -> tuple:
        """
        GET request handler for one director by director id.
        :param did: Director id.
        :return: Director json.
        """
        views_logger.info('Getting director with id %d...', did)
        director = director_service.get_one(did)
        result = DirectorSchema(many=True).dump(director)
        views_logger.info('Returned director: %s', director)
        return result, 200
