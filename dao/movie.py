from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session
        self.model = Movie

    def get_all(self, filters) -> list:
        """
        Метод получения всех фильмов.
        :param filters: Фильтр для поиска по жанрам и режиссерам.
        :return: Список всех фильмов.
        """
        if filters['director_id']:
            return self.session.query(self.model).filter(
                self.model.director_id == filters['director_id']
            ).all()
        elif filters['genre_id']:
            return self.session.query(self.model).filter(
                self.model.genre_id == filters['genre_id']
            ).all()
        elif filters['year']:
            return self.session.query(self.model).filter(
                self.model.year == filters['year']
            ).all()

        return self.session.query(self.model).all()

    def get_by_id(self, mid: int) -> list:
        """
        Метод получения фильма по id.
        :param mid: id фильма.
        :return: Фильм.
        """
        return self.session.query(self.model).get(mid)

    def create(self, data) -> list:
        """
        Метод добавления фильма.
        :param data: Данные фильма.
        :return: Объект фильма.
        """
        movie = self.model(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def update(self, data):
        """
        Метод изменения фильма.
        :param data: Данные фильма.
        :return: None.
        """
        mid = data.pop('id')
        movie = self.get_by_id(mid)
        for field_name, field_value in data.items():
            setattr(movie, field_name, field_value)
        self.session.add(movie)
        self.session.commit()

    def delete(self, mid: int):
        """
        Метод удаления фильма.
        :param mid: id фильма
        :return: None.
        """
        movie = self.get_by_id(mid)
        self.session.delete(movie)
        self.session.commit()
