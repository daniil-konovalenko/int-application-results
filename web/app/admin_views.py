from app import admin, db
from flask_admin.contrib.sqla import ModelView
from app.models import Subject, Student, Result


class SubjectModelView(ModelView):
    column_editable_list = ['name', 'max_score']
    create_modal = True



admin.add_view(SubjectModelView(Subject, db.session))
admin.add_view(ModelView(Student, db.session))
admin.add_view(ModelView(Result, db.session))