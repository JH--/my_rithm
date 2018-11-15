from flask import Blueprint, redirect, render_template, request, url_for
from flask_wtf.csrf import validate_csrf, ValidationError
from project.models import User, Message
from project.messages.forms import MessageForm
from project import db

messages_blueprint = Blueprint("messages", __name__, template_folder="templates")


def get_user_name(id):
    user = User.query.get(id)
    return f"{user.first_name} {user.last_name}"


@messages_blueprint.route("/", methods=["GET"])
def index():
    messages = Message.query.all()
    users = {m.user_id: get_user_name(m.user_id) for m in messages}
    return render_template("index.html", messages=messages, users=users)


@messages_blueprint.route("/new/<int:user_id>")
def new(user_id):
    form = MessageForm(request.form)
    return render_template("new.html", user_id=user_id, form=form)


@messages_blueprint.route("/<int:user_id>", methods=["POST"])
def add_message(user_id):
    form = MessageForm(request.form)
    if form.validate():
        db.session.add(Message(form.data["content"], user_id))
        db.session.commit()
        return redirect(url_for("messages.index"))
    return render_template("new.html", form=form)


@messages_blueprint.route("/<int:id>", methods=["GET"])
def show(id):
    return render_template("show.html", message=Message.query.get(id))


@messages_blueprint.route("/<int:id>", methods=["DELETE"])
def delete(id):
    try:
        validate_csrf(request.form.get("csrf_token"))
        db.session.delete(Message.query.get(id))
        db.session.commit()
        return redirect(url_for("messages.index"))
    except ValidationError:
        return redirect(url_for("messages.index"))


@messages_blueprint.route("/<int:id>/edit")
def edit(id):
    found_message = Message.query.get(id)
    form = MessageForm(obj=found_message)
    return render_template("edit.html", form=form, message=found_message)


@messages_blueprint.route("/<int:id>", methods=["PATCH"])
def edit_message(id):
    message = Message.query.get(id)
    form = MessageForm(request.form)
    if form.validate():
        message.content = form.data["content"]
        db.session.add(message)
        db.session.commit()
        return redirect(url_for("messages.index"))
    return render_template("edit.html", form=form, message=message)

