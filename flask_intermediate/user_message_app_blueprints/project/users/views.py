from flask import Blueprint, redirect, render_template, request, url_for
from flask_wtf.csrf import validate_csrf, ValidationError
from project.models import User
from project.users.forms import UserForm
from project import db

users_blueprint = Blueprint("users", __name__, template_folder="templates")


@users_blueprint.route("/", methods=["GET"])
def index():
    return render_template("index.html", users=User.query.all())


@users_blueprint.route("/new")
def new():
    form = UserForm(request.form)
    return render_template("new.html", form=form)


@users_blueprint.route("/", methods=["POST"])
def add_user():
    form = UserForm(request.form)
    if form.validate():
        db.session.add(User(form.data["first_name"], form.data["last_name"]))
        db.session.commit()
        return redirect(url_for("show_users"))
    return redirect(url_for("new_user"))


@users_blueprint.route("/<int:id>", methods=["GET"])
def show(id):
    return render_template(
        "show.html",
        user=User.query.get(id),
        messages=Message.query.filter_by(user_id=id),
    )


@users_blueprint.route("/<int:id>", methods=["DELETE"])
def delete(id):
    try:
        validate_csrf(request.form.get("csrf_token"))
        db.session.query(Message).filter(Message.user_id == id).delete(
            synchronize_session=False
        )
        db.session.delete(User.query.get(id))
        db.session.commit()
        return redirect(url_for("users.index"))
    except ValidationError:
        return render_template("users.show.html", user=User.query.get(id))


@users_blueprint.route("/<int:id>/edit")
def edit(id):
    found_user = User.query.get(id)
    form = UserForm(obj=found_user)
    return render_template("edit.html", form=form, user=found_user)


@users_blueprint.route("/<int:id>", methods=["PATCH"])
def edit_user(id):
    user = User.query.get(id)
    form = UserForm(request.form)
    if form.validate():
        user.first_name = form.data["first_name"]
        user.last_name = form.data["last_name"]
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("users.index"))
    return render_template("edit.html", form=form, user=found_user)
