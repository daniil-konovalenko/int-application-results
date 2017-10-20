from app import db, app
from app.models import Student

app.config.from_object('config.LoadResultsConfigLocal')

if __name__ == '__main__':
    print(f' в {app.config["SQLALCHEMY_DATABASE_URI"]}')
    for student in db.session.query(Student):
        student.grade = student.results[0].subject.grade
    
    db.session.commit()
