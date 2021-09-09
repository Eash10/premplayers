from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

from application.models import Teams, Players

class TeamsForm(FlaskForm):
    team_name = StringField('Team Name', 
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ] 
    )
    stadium = StringField('Stadium Name', 
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ] 
    )

    submit = SubmitField('Add Team')

class PlayersForm(FlaskForm):
    first_name = StringField('First Name', 
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ] 
    )
    surname = StringField('Surname Name', 
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ] 
    )

    submit = SubmitField('Add Player')

class UpdatePlayersForm(FlaskForm):
    first_name = StringField('First Name', 
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ] 
    )
    surname = StringField('Surname Name', 
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ] 
    )

    submit = SubmitField('Update Player')

class UpdateTeamsForm(FlaskForm):
    team_name = StringField('Team Name', 
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ] 
    )
    stadium = StringField('Stadium Name', 
        validators = [
            DataRequired(),
            Length(min=2, max=30)
        ] 
    )

    submit = SubmitField('Update Team')
