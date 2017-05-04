from app import app
from app import db
from app.models import Subject

app.config.from_object('config.LoadResultsConfig')

subjects = [
    Subject(name='Тест по математике', grade=7, max_score=14,
            always_count=True),
    Subject(name='Математика', grade=7, max_score=20),
    Subject(name='Филология', grade=7, max_score=20),
    Subject(name='История', grade=7, max_score=20),
    Subject(name='Биология', grade=7, max_score=20),
    Subject(name='Химия', grade=7, max_score=20),
    Subject(name='География', grade=7, max_score=20),
    
    Subject(name='Тест по математике', grade=8, max_score=20,
            always_count=True),
    Subject(name='Математика', grade=8, max_score=20),
    Subject(name='Филология', grade=8, max_score=20),
    Subject(name='История', grade=8, max_score=20),
    Subject(name='Биология', grade=8, max_score=20),
    Subject(name='Химия', grade=8, max_score=20),
    Subject(name='География', grade=8, max_score=20),
    Subject(name='Английский язык', grade=8, max_score=20),

]

db.session.add_all(subjects)
db.session.commit()
