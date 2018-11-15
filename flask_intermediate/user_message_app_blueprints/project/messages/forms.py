from flask_wtf import FlaskForm
from wtforms import StringField, validators


class MessageForm(FlaskForm):
    content = StringField("New Message", [validators.DataRequired()])
