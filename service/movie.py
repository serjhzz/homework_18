from dao.movie import MovieDAO
from log_handler import services_logger


class MovieService:

    def __init__(self, dao: MovieDAO):
        self.dao = dao
        self.logger = services_logger

    def get_all(self, filters) -> list:
        self.logger.info("Retrieving all movies")
        return self.dao.get_all(filters)

    def get_one(self, mid: int) -> list:
        self.logger.info(f"Retrieving movie with ID {mid}")
        return self.dao.get_by_id(mid)

    def create(self, data):
        self.logger.info("Adding a new movie")
        return self.dao.create(data)

    def update(self, data):
        self.logger.info(f"Updated rows")
        return self.dao.update(data)

    def delete(self, mid):
        self.logger.info(f"Deleting movie with ID {mid}")
        return self.dao.delete(mid)
