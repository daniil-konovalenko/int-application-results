from flask.ext.wtf import Form
from wtforms import IntegerField, StringField, FileField, SelectField
from flask_wtf.file import FileRequired, FileAllowed
from wtforms.validators import DataRequired

from flask_security.forms import LoginForm, PasswordField, BooleanField
from flask_security.forms import SubmitField


class IDForm(Form):
    id = IntegerField('id', validators=[DataRequired()])


class LocalizedLoginForm(LoginForm):
    email = StringField(label='Логин')
    password = PasswordField(label='Пароль')
    remember = BooleanField(label='Запомнить меня')
    submit = SubmitField(label='Войти')


class UploadForm(Form):
    file = FileField()
    grade = SelectField(choices=[(str(gr), gr) for gr in [7, 8, 10]])
