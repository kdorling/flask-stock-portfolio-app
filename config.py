import os
from datetime import timedelta


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

    BCRYPT_LOG_ROUNDS = 15

    WTF_CSRF_ENABLED = True

    REMEMBER_COOKIE_DURATION = timedelta(days=14)

    # Flask-Mail Configuration
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', default='')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', default='')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_USERNAME', default='')


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

    BCRYPT_LOG_ROUNDS = 4

    WTF_CSRF_ENABLED = False
