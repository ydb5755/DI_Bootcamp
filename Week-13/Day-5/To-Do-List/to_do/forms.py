from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, SubmitField

class AddTodo(FlaskForm):
    task = StringField('Task', validators=[DataRequired()])
    image = StringField('Image URL', validators=[DataRequired()])
    submit = SubmitField('Add to do')