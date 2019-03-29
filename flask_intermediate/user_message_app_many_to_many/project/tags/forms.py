from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, widgets
from wtforms.validators import DataRequired
from project.models import Message


class TagForm(FlaskForm):
    tag = StringField("tag", validators=[DataRequired()])
    messages = SelectMultipleField(
        "messages",
        coerce=int,
        widget=widgets.ListWidget(prefix_label=False),
        option_widget=widgets.CheckboxInput(),
    )

    def set_choices(self):
        self.messages.choices = [(m.id, m.message) for m in Message.query.all()]

