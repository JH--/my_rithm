from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


class UserForm(FlaskForm):
    first_name = StringField("first_name", validators=[DataRequired()])
    last_name = StringField("last_name", validators=[DataRequired()])
    user_name = StringField("user_name", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])


class LoginForm(FlaskForm):
    user_name = StringField("user_name", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])

