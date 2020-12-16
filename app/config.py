import os

# Secret DB credentials
dbUser = 'postgres'
dbPass = 'root'
dbHost = 'localhost'
dbPort = 5432
dbName = 'castingagency'


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def __init__(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(
        dbUser, dbPass, dbHost, dbPort, dbName)
    print("Using Development Config")


class TestingConfig(Config):
    pass


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
