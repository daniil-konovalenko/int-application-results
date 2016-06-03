from app import db


class Results(db.Model):
    student_id = db.Column(db.Integer, primary_key=True)
    math_test_18 = db.Column(db.Float)
    math_test = db.Column(db.Float)
    math = db.Column(db.Float)
    philology = db.Column(db.Float)
    history = db.Column(db.Float)
    science = db.Column(db.Float)
    biology = db.Column(db.Float)
    chemistry = db.Column(db.Float)
    english = db.Column(db.Float)
    geography = db.Column(db.Float)
    final = db.Column(db.Float)
    comments = db.Column(db.UnicodeText)
    math_unified_plan = db.Column(db.Float)
    math_individual_plan =db.Column(db.Float)
    math_final = db.Column(db.Float)
    russian = db.Column(db.Float)
    # Please forgive me


    def __init__(self,
                 student_id,
                 math_test,
                 math,
                 philology,
                 history,
                 science,
                 biology,
                 chemistry,
                 english,
                 geography,
                 final,
                 math_test_18,
                 math_unified_plan,
                 math_individual_plan,
                 math_final,
                 russian,
                 ):
        self.student_id = student_id
        self.math_test = math_test
        self.math = math
        self.philology = philology
        self.history = history
        self.science = science
        self.biology = biology
        self.chemistry = chemistry
        self.english = english
        self.geography = geography
        self.final = final
        self.math_test_18 = math_test_18
        self.math_unified_plan = math_unified_plan
        self.math_individual_plan = math_individual_plan
        self.math_final = math_final
        self.russian = russian
    def __repr__(self):
        return '<Result of student #{}>'.format(self.student_id)

    def __str__(self):
        return '<Result of student #{}>'.format(self.student_id)

    def __getitem__(self, item):
        return self.__dict__.get(item)