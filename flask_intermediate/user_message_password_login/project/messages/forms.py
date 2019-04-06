from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, widgets
from wtforms.validators import DataRequired
from project.models import Tag


class MessageForm(FlaskForm):
    message = StringField("message", validators=[DataRequired()])
    tags = SelectMultipleField(
        "Tags",
        coerce=int,
        widget=widgets.ListWidget(prefix_label=False),
        option_widget=widgets.CheckboxInput(),
    )
    new_tag = StringField("new_tag")

    def set_choices(self):
        self.tags.choices = [(t.id, t.tag) for t in Tag.query.all()]

