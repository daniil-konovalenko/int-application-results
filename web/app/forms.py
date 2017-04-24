from flask.ext.wtf import Form
from wtforms import IntegerField
from wtforms.validators import DataRequired


class IDForm(Form):
    id = IntegerField('id', validators=[DataRequired])

