from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session
        self.model = Genre

    def get_by_id(self, gid: int) -> list:
        """
        Метод получения жанра по id.
        :param gid: id жанра.
        :return: Жанр.
        """
        return self.session.query(self.model).get(gid)

    def get_all(self) -> list:
        """
        Метод получения всех жанров.
        :return: Список всех жанров.
        """
        return self.session.query(self.model).all()

    def create(self, data) -> list:
        """
        Метод добавления жанра.
        :param data: Данные жанра.
        :return: Объект жанра.
        """
        genre = self.model(**data)
        self.session.add(genre)
        self.session.commit()
        return genre

    def update(self, data):
        """
        Метод изменения жанра.
        :param data: Данные жанра.
        :return: None.
        """
        genre = self.get_by_id(data['id'])
        genre.name = data['name']
        self.session.add(genre)
        self.session.commit()

    def delete(self, did: int):
        """
        Метод удаления жанра.
        :param did: id жанра
        :return: None.
        """
        genre = self.get_by_id(did)
        self.session.delete(genre)
        self.session.commit()
