from app import db


class Student(db.Model):
    __tablename__ = 'students'
    
    id = db.Column(db.Integer, primary_key=True)
    assigned_id = db.Column(db.Integer)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    year = db.Column(db.Integer)
    
    results = db.relationship("Result", back_populates='student')
    
    def __repr__(self):
        return (f"<Student("
                f"first name: {self.first_name}, "
                f"last name: {self.last_name}, "
                f"year: {self.year}, "
                f"id: {self.assigned_id})>")


class Subject(db.Model):
    __tablename__ = 'subjects'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    max_score = db.Column(db.Float)
    
    def __repr__(self):
        return f"<Subject(name: {self.name}, maximum score: {self.max_score})>"


class Result(db.Model):
    __tablename__ = 'results'
    
    id = db.Column(db.Integer, primary_key=True)
    
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    student = db.relationship('Student', back_populates='results')
    
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'))
    subject = db.relationship('Subject')
    
    score = db.Column(db.Float)
    
    def __repr__(self):
        return (f"<Result of student #{self.student.assigned_id}"
                f" in {self.subject.name}>")
