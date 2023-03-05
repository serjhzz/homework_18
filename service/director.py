from dao.director import DirectorDAO
from log_handler import services_logger


class DirectorService:

    def __init__(self, dao: DirectorDAO):
        self.dao = dao
        self.logger = services_logger

    def get_all(self) -> list:
        """
        Get all directors from DB.
        :return: All directors.
        """
        self.logger.info('Retrieving all directors')
        return self.dao.get_all()

    def get_one(self, did: int) -> list:
        """
        Get one director from DB by ID.
        :param did: Director id.
        :return: One director.
        """
        self.logger.info(f'Retrieving director with ID {did}')
        return self.dao.get_by_id(did)

    def create(self, data):
        """
        Add new director to DB.
        :param data: Director data.
        :return: New object.
        """
        self.logger.info('Adding new director')
        return self.dao.create(data)

    def update(self, data):
        """
        Update director.
        :param data: Director data.
        :return: New object.
        """
        self.logger.info('Update director')
        return self.dao.create(data)

    def delete(self, did):
        """
        Delete one director from DB by ID.
        :param did: Director id.
        :return: None
        """
        self.logger.info('Delete director')
        return self.dao.delete(did)
