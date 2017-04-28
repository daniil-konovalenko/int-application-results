from flask.ext.wtf import Form
from wtforms import IntegerField, StringField
from wtforms.validators import DataRequired

from flask_security.forms import LoginForm, PasswordField, BooleanField
from flask_security.forms import SubmitField


class IDForm(Form):
    id = IntegerField('id', validators=[DataRequired])


class LocalizedLoginForm(LoginForm):
    email = StringField(label='Логин')
    password = PasswordField(label='Пароль')
    remember = BooleanField(label='Запомнить меня')
    submit = SubmitField(label='Войти')
