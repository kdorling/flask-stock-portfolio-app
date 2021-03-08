import os


# Determines the folder of the top-level directory of this project
BASEDIR = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    FLASK_ENV = 'development'
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY',
                           default=b'\xa9?\x02\xdd\xcd\x831Z\xa4\xafw\x9cX*'
                                   b'\xd4\x8a\xad\x8e\xcb\x154\xe9\x9c\xf7W5'
                                   b'\x88\xe5\xc3H\xabG')

    default_database_path = os.path.join(BASEDIR, 'instance', 'app.db')
    default_database_uri = f'sqlite:///{default_database_path}'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL',
                                        default=default_database_uri)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    FLASK_ENV = 'production'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True

    default_test_database_path = os.path.join(BASEDIR, 'instance', 'test.db')
    default_test_database_uri = f'sqlite:///{default_test_database_path}'
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URI',
                                        default=default_test_database_uri)
