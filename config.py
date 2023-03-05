from constants import SQLITE_DB_NAME


class Config(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = SQLITE_DB_NAME
    SQLALCHEMY_TRACK_MODIFICATIONS = False
