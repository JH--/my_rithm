from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, PasswordField, IntergerField, validators


class SignupForm(FlaskForm):
    first_name = StringField("First Name", [validators.DataRequired()])
    last_name = StringField("Last_name", [validators.DataRequired()])

