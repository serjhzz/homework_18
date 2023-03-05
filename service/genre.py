from dao.genre import GenreDAO
from log_handler import services_logger


class GenreService:

    def __init__(self, dao: GenreDAO):
        self.dao = dao
        self.logger = services_logger

    def get_all(self) -> list:
        """
        Get all genres from DB.
        :return: All genres.
        """
        self.logger.info('Retrieving all genres')
        return self.dao.get_all()

    def get_one(self, gid: int) -> list:
        """
        Get one genre by genre ID.
        :param gid: Genre id.
        :return: One genre.
        """
        self.logger.info(f'Retrieving genre with ID {gid}')
        return self.dao.get_by_id(gid)

    def create(self, data):
        """
        Add new genre to DB.
        :param data: Genre data.
        :return: New object.
        """
        self.logger.info('Adding new genre')
        return self.dao.create(data)

    def update(self, data):
        """
        Update genre.
        :param data: Genre data.
        :return: New object.
        """
        self.logger.info('Update genre')
        return self.dao.create(data)

    def delete(self, gid):
        """
        Delete one genre from DB by ID.
        :param gid: Genre id.
        :return: None
        """
        self.logger.info('Delete genre')
        return self.dao.delete(gid)
