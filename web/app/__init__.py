from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_admin import Admin

import logging


app = Flask(__name__.split('.')[0])
app.config.from_object('config')

db = SQLAlchemy(app)

admin = Admin(app, name='intresults', template_mode='bootstrap3')

gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)



from app import views, admin_views
