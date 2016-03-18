from app import db


class Results(db.Model):
    student_id = db.Column(db.Integer, primary_key=True)
    math_test = db.Column(db.Integer)
    math = db.Column(db.Integer)
    philology = db.Column(db.Integer)
    history = db.Column(db.Integer)
    science = db.Column(db.Integer)
    comments = db.Column(db.UnicodeText)

    def __repr__(self):
        return '<Result of student #{}>'.format(self.student_id)

    def __str__(self):
        return '<Result of student #{}>'.format(self.student_id)
