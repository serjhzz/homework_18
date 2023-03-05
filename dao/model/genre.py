from setup_db import db
from marshmallow import Schema, fields


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)

    def __repr__(self):
        return f'Genre: {self.id} - {self.name}'


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()


genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)
