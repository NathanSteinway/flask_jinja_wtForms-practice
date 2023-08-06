from flask_wtf import FlaskForm
from forms import TeamForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class TeamForm(FlaskForm):
    team_name = StringField('team name', validators=[DataRequired(), Length(min=4, max=255)])
    submit = StringField('submit')

class ProjectForm(FlaskForm):
    project_name = StringField('project name', validators=[DataRequired(), Length(min=4, max=255)])
    description = TextAreaField('description')
    completed = BooleanField("completed?")
    team_selection = SelectField("Team")
    submit = SubmitField("submit")