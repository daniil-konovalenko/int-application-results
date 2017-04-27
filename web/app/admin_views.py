from app import admin, db
from flask_admin.contrib.sqla import ModelView
from app.models import Subject, Student, Result, Role, User
from flask_security import current_user
from flask import redirect, url_for, request, abort


class ProtectedModelView(ModelView):
    def is_accessible(self):
        if not current_user.is_active or not current_user.is_authenticated:
            return False
        if current_user.has_role('superuser'):
            return True
    
    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                return redirect(url_for('/'))
            else:
                # login
                return redirect(url_for('security.login', next=request.url))


class SubjectModelView(ProtectedModelView):
    column_editable_list = ['name', 'max_score']
    create_modal = True




admin.add_view(ProtectedModelView(Role, db.session))
admin.add_view(ProtectedModelView(User, db.session))

admin.add_view(SubjectModelView(Subject, db.session))
admin.add_view(ProtectedModelView(Student, db.session))
admin.add_view(ProtectedModelView(Result, db.session))
