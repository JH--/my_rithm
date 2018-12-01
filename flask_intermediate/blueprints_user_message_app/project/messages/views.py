from flask import Blueprint, render_template, redirect, url_for, request
from flask_wtf.csrf import validate_csrf, ValidationError
from project.messages.forms import MessageForm
from project.models import Message
from project import db


messages_blueprint = Blueprint("messages", __name__, template_folder="templates")


@messages_blueprint.route("/", methods=["GET"])
def index():
    return render_template("messages/index.html", messages=Message.query.all())


@messages_blueprint.route("/new/<int:user_id>", methods=["GET"])
def new(user_id):
    form = MessageForm()
    return render_template("messages/new.html", user_id=user_id, form=form)


@messages_blueprint.route("/<int:user_id>", methods=["POST"])
def new_message(user_id):
    form = MessageForm(request.form)
    if form.validate():
        db.session.add(Message(request.form["message"], user_id))
        db.session.commit()
    return redirect(url_for("messages.index"))

