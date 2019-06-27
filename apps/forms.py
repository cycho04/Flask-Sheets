from flask_wtf import Form
from wtforms import StringField, DateTimeField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired


class NewEmployeeForm(Form):
    first = StringField('First', validators=[DataRequired()])
    last = StringField('Last', validators=[DataRequired()])
    casino = SelectField('Casino', choices=[
        {'empire', 'Empire'}, {'lodi', 'Lodi'}])
    title = SelectField('Title', choices=[{'associate', 'Associate'}, {
        'supervisor', 'Supervisor'}])
    hired = DateTimeField('Hired Date')
    EIN = IntegerField('EIN')
    submit = SubmitField('Submit')
