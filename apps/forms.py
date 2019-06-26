from flask_wtf import Form
from wtforms import StringField, DateField, IntegerField, RadioField, SubmitField
from wtforms.validators import DataRequired


class NewEmployeeForm(Form):
    first = StringField('First', validators=[DataRequired()])
    last = StringField('Last', validators=[DataRequired()])
    casino = RadioField('Casino', choices=[
                        {'Empire': 'Empire'}, {'Lodi': 'Lodi'}])
