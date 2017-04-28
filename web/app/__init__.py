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

from .admin_index_view import UploadView
from .forms import LocalizedLoginForm

app = Flask(__name__.split('.')[0])
app.config.from_object(os.environ.get('APP_SETTINGS', 'config.DevelopmentConfig'))

db = SQLAlchemy(app)

admin = Admin(app, name='intresults', template_mode='bootstrap3',
              base_template='my_master.html')

gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def init_roles():
    user_role = Role(name='user')
    superuser_role = Role(name='superuser')
    with app.app_context():
        db.session.add(user_role)
        db.session.add(superuser_role)
        db.session.commit()

@manager.command
def create_user(login, password, first_name=None, last_name=None, superuser=False):
    """Creates user in db"""
    user_role = Role(name='user')
    superuser_role = Role(name='superuser')
    
    with app.app_context():
        superuser = user_datastore.create_user(
            first_name=first_name,
            last_name=last_name,
            email=login,
            password=encrypt_password(password),
            roles=[user_role, superuser_role] if superuser else [user_role]
        )
        db.session.commit()
    

from app.models import User, Role

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore, login_form=LocalizedLoginForm)



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
