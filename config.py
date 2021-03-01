import os


class Config(object):
    FLASK_ENV = 'development'
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY',
                           default=b'\xa9?\x02\xdd\xcd\x831Z\xa4\xafw\x9cX*'
                                   b'\xd4\x8a\xad\x8e\xcb\x154\xe9\x9c\xf7W5'
                                   b'\x88\xe5\xc3H\xabG')


class ProductionConfig(Config):
    FLASK_ENV = 'production'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
