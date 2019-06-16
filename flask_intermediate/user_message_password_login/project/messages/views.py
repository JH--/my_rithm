from flask import Blueprint, render_template, redirect, url_for, request
from flask_wtf.csrf import validate_csrf, ValidationError
from project.messages.forms import MessageForm
from project.models import Message, User, Tag
from project import db
from project.decorators import (
    ensure_authenticated,
    ensure_correct_user,
    ensure_correct_user_edit_delete,
)

messages_blueprint = Blueprint("messages", __name__, template_folder="templates")


@messages_blueprint.route("/", methods=["GET"])
def index():
    messages = Message.query.all()
    return render_template("messages/index.html", messages=messages)


@messages_blueprint.route("/new/<int:user_id>", methods=["GET"])
@ensure_authenticated
@ensure_correct_user
def new(user_id):
    if not User.query.get(user_id):
        return render_template("404.html")
    form = MessageForm()
    form.set_choices()
    return render_template("messages/new.html", user_id=user_id, form=form)


@messages_blueprint.route("/<int:user_id>", methods=["POST"])
@ensure_authenticated
@ensure_correct_user
def new_message(user_id):
    form = MessageForm(request.form)
    form.set_choices()
    if form.validate():
        user = User.query.get(user_id)
        message = Message(request.form["message"])
        tags = [Tag.query.get(t) for t in form.tags.data]
        new_tag = get_new_tag(request.form["new_tag"])
        if new_tag:
            tags.append(new_tag)
        message.tags.extend(tags)
        user.messages.extend([message])
        db.session.commit()
    return redirect(url_for("messages.index"))


def get_new_tag(new_tag):
    if new_tag:
        tag = Tag(new_tag)
        db.session.add(tag)
        db.session.commit()
        return tag


@messages_blueprint.route("/<int:id>", methods=["GET"])
def show(id):
    message = Message.query.get(id)
    if not message:
        return render_template("404.html")
    return render_template("messages/show.html", message=message)


@messages_blueprint.route("/<int:id>/edit", methods=["GET"])
@ensure_authenticated
@ensure_correct_user_edit_delete
def edit(id):
    message = Message.query.get(id)
    if not message:
        return render_template("404.html")
    tags = [t.id for t in message.tags]
    form = MessageForm(obj=message)
    form.set_choices()
    form.tags.process_data(tags)
    return render_template("messages/edit.html", form=form, message=message)


@messages_blueprint.route("/<int:id>", methods=["PATCH"])
@ensure_authenticated
@ensure_correct_user_edit_delete
def edit_message(id):
    form = MessageForm(request.form)
    form.set_choices()
    if form.validate():
        message = Message.query.get(id)
        message.message = request.form["message"]
        message.tags = [Tag.query.get(t) for t in form.tags.data]
        new_tag = get_new_tag(request.form["new_tag"])
        if new_tag:
            message.tags.append(new_tag)
        db.session.add(message)
        db.session.commit()
    return redirect(url_for("messages.index"))


@messages_blueprint.route("/<int:id>", methods=["DELETE"])
@ensure_authenticated
@ensure_correct_user_edit_delete
def delete(id):
    try:
        validate_csrf(request.form.get("csrf_token"))
        db.session.delete(Message.query.get(id))
        db.session.commit()
        return redirect(url_for("messages.index"))
    except ValidationError:
        return redirect(url_for("messages.index"))

