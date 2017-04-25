import os

basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = 'whateverplfdjassasdd'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')



DEBUG = True
SQLALCHEMY_ECHO = True
DB_NAME='postgres'
DB_USER='postgres'
DB_PASS='postgres'
DB_SERVICE='postgres'
DB_PORT=5432

SQLALCHEMY_DATABASE_URI = (f'postgresql://{DB_USER}:{DB_PASS}@'
                           f'{DB_SERVICE}:{DB_PORT}/{DB_NAME}')

SQLALCHEMY_TRACK_MODIFICATIONS = False
