import logging
import os

from flask import Flask, url_for
from flask_admin import Admin
from flask_admin import helpers as admin_helpers
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_security import Security, SQLAlchemyUserDatastore
from flask_sqlalchemy import SQLAlchemy
from flask_security.utils import encrypt_password


app = Flask(__name__.split('.')[0])
app.config.from_object(os.environ.get('APP_SETTINGS', 'config.DevelopmentConfig'))

db = SQLAlchemy(app)

admin = Admin(app, name='intresults', template_mode='bootstrap3')

gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def create_superuser():
    """Creates superuses in db"""
    user_role = Role(name='user')
    superuser_role = Role(name='superuser')
    with app.app_context():
        db.session.add(user_role)
        db.session.add(superuser_role)
        
        superuser = user_datastore.create_user(
            first_name='Admin',
            email='admin',
            password=encrypt_password('admin'),
            roles=[user_role, superuser_role]
        )
        db.session.commit()
    

from app.models import User, Role

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)



# define a context processor for merging flask-admin's template context into the
# flask-security views.
@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template=admin.base_template,
        admin_view=admin.index_view,
        h=admin_helpers,
        get_url=url_for
    )


from app import views, admin_views
