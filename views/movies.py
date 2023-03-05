from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from implemented import movie_service
from log_handler import views_logger

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        views_logger.info('Request received: %s - %s', request.method, request.url)
        director = request.args.get('director_id')
        genre = request.args.get('genre_id')
        year = request.args.get('year')
        filters = {
            'director_id': director,
            'genre_id': genre,
            'year': year,
        }
        movies = movie_service.get_all(filters)
        result = MovieSchema(many=True).dump(movies)
        views_logger.info('Response sent: %s', result)
        return result, 200

    def post(self):
        views_logger.info('Request received: %s %s', request.method, request.url)
        data = request.json
        movie_service.create(data)
        views_logger.info('Response sent: Success')
        return "", 201


@movies_ns.route('/<int:mid>/')
class MovieView(Resource):
    def get(self, mid):
        views_logger.info('Request received: %s %s', request.method, request.url)
        movie = movie_service.get_one(mid)
        movie_data = MovieSchema().dump(movie)
        views_logger.info('Response sent: %s', movie_data)
        return movie_data, 200

    def put(self, mid):
        views_logger.info('Request received: %s %s', request.method, request.url)
        data = request.json
        data['id'] = mid
        movie_service.update(data)
        views_logger.info('Response sent: Success')
        return '', 204

    def delete(self, mid):
        views_logger.info('Request received: %s %s', request.method, request.url)
        movie_service.delete(mid)
        views_logger.info('Response sent: No Content')
        return '', 204
