from flask import Blueprint, render_template, redirect, url_for, request
from flask_wtf.csrf import validate_csrf, ValidationError
from project.users.forms import UserForm
from project.models import User
from project import db

users_blueprint = Blueprint("users", __name__, template_folder="templates")


@users_blueprint.route("/", methods=["GET"])
def index():
    return render_template("users/index.html", users=User.query.all())


@users_blueprint.route("/new", methods=["GET"])
def new():
    form = UserForm()
    return render_template("users/new.html", form=form)


@users_blueprint.route("/", methods=["POST"])
def new_user():
    form = UserForm(request.form)
    if form.validate():
        db.session.add(User(request.form["first_name"], request.form["last_name"]))
        db.session.commit()
        return redirect(url_for("users.index"))
    return render_template("users/new.html", form=form)


@users_blueprint.route("/<int:id>", methods=["GET"])
def show(id):
    return render_template("users/show.html", user=User.query.get(id))


@users_blueprint.route("/<int:id>/edit", methods=["GET"])
def edit(id):
    user = User.query.get(id)
    form = UserForm(obj=user)
    return render_template("users/edit.html", form=form, user=user)


@users_blueprint.route("/<int:id>", methods=["PATCH"])
def edit_user(id):
    user = User.query.get(id)
    form = UserForm(request.form)
    if form.validate():
        user.first_name = request.form["first_name"]
        user.last_name = request.form["last_name"]
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("users.index"))
    return render_template("users/show.html", user=user)


@users_blueprint.route("/<int:id>", methods=["DELETE"])
def delete(id):
    try:
        validate_csrf(request.form.get('csrf_token'))
        db.session.delete(User.query.get(id))
        db.session.commit()
        return redirect(url_for('users.index'))
    except ValidationError:
        return redirect(url_for('users.index'))
        
