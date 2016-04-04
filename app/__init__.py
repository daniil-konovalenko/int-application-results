from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

subjects = {
    "math_test": {"name": "Математика (тест)", "max_score": 13},
    "math_test_18": {"name": "Математика (тест)", "max_score": 18},
    "math": {"name": "Математика", "max_score": 20},
    "philology": {"name": "Филология", "max_score": 20},
    "history": {"name": "История", "max_score": 20},
    "science": {"name": "Естествознание", "max_score": 20},
    "biology": {"name": "Биология", "max_score": 20},
    "chemistry": {"name": "Химия", "max_score": 20},
    "english": {"name": "Английский язык", "max_score": 20},
    "geography": {"name": "География", "max_score": 20},

}

app = Flask(__name__.split('.')[0])
app.config.from_object('config')
db = SQLAlchemy(app)

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


from app import views, models