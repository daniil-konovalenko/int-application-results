WTF_CSRF_ENABLED = True
SECRET_KEY = 'whateverplfdjassasdd'

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
