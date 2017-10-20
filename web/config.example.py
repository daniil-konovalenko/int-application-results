import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    SECURITY_URL_PREFIX = "/admin"
    SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
    SECURITY_PASSWORD_SALT = "ATGUOHAELKiubahiughaerGOJAEGj"
    
    # Flask-Security URLs, overridden because they don't put a / at the end
    SECURITY_LOGIN_URL = "/login/"
    SECURITY_LOGOUT_URL = "/logout/"
    SECURITY_REGISTER_URL = "/register/"
    
    SECURITY_POST_LOGIN_VIEW = "/admin/"
    SECURITY_POST_LOGOUT_VIEW = "/admin/"
    SECURITY_POST_REGISTER_VIEW = "/admin/"
    
    # Flask-Security features
    SECURITY_REGISTERABLE = True
    SECURITY_SEND_REGISTER_EMAIL = False
    
    WTF_CSRF_ENABLED = True
    SECRET_KEY = 'put your own secret key here'
    SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    DB_NAME = 'postgres'
    DB_USER = 'postgres'
    DB_PASS = 'postgres'
    DB_SERVICE = 'localhost'
    DB_PORT = 5433
    
    SQLALCHEMY_DATABASE_URI = (f'postgresql://{DB_USER}:{DB_PASS}@'
                               f'{DB_SERVICE}:{DB_PORT}/{DB_NAME}')


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_ECHO = False
    DB_NAME = 'postgres'
    DB_USER = 'postgres'
    DB_PASS = 'postgres'
    DB_SERVICE = 'postgres'
    DB_PORT = 5432
    
    SQLALCHEMY_DATABASE_URI = (f'postgresql://{DB_USER}:{DB_PASS}@'
                               f'{DB_SERVICE}:{DB_PORT}/{DB_NAME}')
