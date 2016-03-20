from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

subjects = {
    "math_test": "Математика (тест)",
    "math": "Математика",
    "philology": "Филология",
    "history": "История",
    "science": "Естествознание",
}

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


from app import views, models