from dao.model.director import Director
from log_handler import dao_logger


class DirectorDAO:
    def __init__(self, session):
        self.session = session
        self.model = Director
        self.logger = dao_logger

    def get_by_id(self, did: int) -> list:
        """
        Метод получения режиссера по id.
        :param did: id режиссера.
        :return: Режисер.
        """
        return self.session.query(self.model).get(did)

    def get_all(self) -> list:
        """
        Метод получения всех режиссеров.
        :return: Список всех режиссеров.
        """
        return self.session.query(self.model).all()

    def create(self, data) -> list:
        """
        Метод добавления режиссера.
        :param data: Данные режиссера.
        :return: Объект режиссера.
        """
        director = self.model(**data)
        self.session.add(director)
        self.session.commit()
        return director

    def update(self, data):
        """
        Метод изменения режиссера.
        :param data: Данные режиссера.
        :return: None.
        """
        director = self.get_by_id(data['id'])
        director.name = data['name']
        self.session.add(director)
        self.session.commit()

    def delete(self, did: int):
        """
        Метод удаления режиссера.
        :param did: id режиссера
        :return: None.
        """
        director = self.get_by_id(did)
        self.session.delete(director)
        self.session.commit()
