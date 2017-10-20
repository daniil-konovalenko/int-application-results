from app.models import Student, Result, Subject
from app import db
from random import randint

vanya = Student(first_name="Иван", last_name="Петров", year=2017,
                assigned_id=5351)

petya = Student(first_name="Петр", last_name="Васечкин", year=2017,
                assigned_id=5352)

students = [vanya, petya]

db.session.add_all(students)

math = Subject(name='Математика', max_score=22)
phys = Subject(name='Физика', max_score=25)
bio = Subject(name='Биология', max_score=20)
geo = Subject(name='География', max_score=20)
math_test = Subject(name='Математика (тест)', max_score=20)

subjects = [math_test, math, phys, bio, geo]

db.session.add_all(subjects)

results = []

for student in students:
    for subject in subjects:
        score = randint(0, subject.max_score)
        results.append(Result(student=student, score=score, subject=subject))

db.session.add_all(results)
db.session.commit()
