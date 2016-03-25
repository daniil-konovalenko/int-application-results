from app import db


class Results(db.Model):
    student_id = db.Column(db.Integer, primary_key=True)
    math_test = db.Column(db.Float)
    math = db.Column(db.Float)
    philology = db.Column(db.Float)
    history = db.Column(db.Float)
    science = db.Column(db.Float)
    comments = db.Column(db.UnicodeText)

    def __init__(self, student_id, math_test, math, philology, history, science):
        self.student_id = student_id
        self.math_test = math_test
        self.math = math
        self.philology = philology
        self.history = history
        self.science = science

    def __repr__(self):
        return '<Result of student #{}>'.format(self.student_id)

    def __str__(self):
        return '<Result of student #{}>'.format(self.student_id)

    def __getitem__(self, item):
        return self.__dict__.get(item)