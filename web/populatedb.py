from app.models import Student, Result, Subject
from app import db

vanya = Student(first_name="Иваан", last_name="Окаянный", year=2017,
                assigned_id=5351)

petya = Student(first_name="Петр", last_name="Великий", year=2017,
                assigned_id=5352)

db.session.add(vanya)
db.session.add(petya)

math = Subject(name='Математика', max_score=22)
phys = Subject(name='Физика', max_score=25)

db.session.add(math)
db.session.add(phys)

results = [
    Result(subject=math, student=vanya, score=21),
    Result(subject=phys, student=vanya, score=23),
    Result(subject=math, student=petya, score=0),
    Result(subject=phys, student=petya, score=1),
]
db.session.add_all(results)
db.session.commit()
