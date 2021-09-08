from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError

from application.models import Teams, Players

class TeamsForm(FlaskForm):
    