from flask import redirect, url_for, request
from flask_admin.contrib.sqla import ModelView
from flask_security import current_user
from flask_admin import BaseView, expose
from app import admin, db
from app.models import Subject, Student, Result, Role, User
from app.forms import UploadForm
from app.excel_processing import get_df, get_subjects


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

class Upload(BaseView):
        
    @expose('/', methods=['GET', 'POST'])
    def upload(self):
        if not current_user.is_authenticated:
            return redirect(url_for('login'))
        
        if request.method == 'GET':
            return self.render('admin/upload.html', form=UploadForm())
        
        if request.method == 'POST':
            form = UploadForm(request.form)
            file_storage = request.files['file']
            grade = form.grade
            df = get_df(file_storage)
            html_table = df.head().to_html(classes=['table', 'table-hover', 'table-condensed', 'table-bordered'], border=0, index=False)
            subjects = get_subjects(df)
            return self.render('admin/uploaded.html', df=html_table)
            

admin.add_view(ProtectedModelView(Role, db.session))
admin.add_view(ProtectedModelView(User, db.session))

admin.add_view(SubjectModelView(Subject, db.session))
admin.add_view(ProtectedModelView(Student, db.session))
admin.add_view(ProtectedModelView(Result, db.session))
admin.add_view(Upload(name='Upload'))