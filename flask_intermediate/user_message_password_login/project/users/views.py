from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_wtf.csrf import validate_csrf, ValidationError
from project.users.forms import UserForm, LoginForm
from project.models import User
from project import db, bcrypt
from sqlalchemy.exc import IntegrityError

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
        try:
            db.session.add(
                User(
                    form.first_name.data,
                    form.last_name.data,
                    form.user_name.data,
                    form.password.data,
                )
            )
            db.session.commit()
            flash("User Created!")
            return redirect(url_for("users.index"))
        except IntegrityError:
            flash("Username already taken!")
    return render_template("users/new.html", form=form)


@users_blueprint.route("/login", methods=["GET"])
def login():
    form = LoginForm()
    return render_template("users/login.html", form=form)


@users_blueprint.route("/login", methods=["POST"])
def login_user():
    form = LoginForm(request.form)
    if form.validate():
        authenticated_user = User.authenticate(form.user_name.data, form.password.data)
        if authenticated_user:
            flash("You are logged in!")
            return redirect(url_for("users.show", id=authenticated_user.id))
        else:
            flash("Invalid Credentials!")
    return render_template("users/login.html", form=form)


@users_blueprint.route("/<int:id>", methods=["GET"])
def show(id):
    user = User.query.get(id)
    if not user:
        return render_template("404.html")
    return render_template("users/show.html", user=user, messages=user.messages)


@users_blueprint.route("/<int:id>/edit", methods=["GET"])
def edit(id):
    user = User.query.get(id)
    if not user:
        return render_template("404.html")
    form = UserForm(obj=user)
    return render_template("users/edit.html", form=form, user=user)


@users_blueprint.route("/<int:id>", methods=["PATCH"])
def edit_user(id):
    form = UserForm(request.form)
    if form.validate():
        user = User.query.get(id)
        user.first_name = request.form["first_name"]
        user.last_name = request.form["last_name"]
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("users.index"))
    return render_template("users/show.html", user=user)


@users_blueprint.route("/<int:id>", methods=["DELETE"])
def delete(id):
    try:
        validate_csrf(request.form.get("csrf_token"))
        user = User.query.get(id)
        for message in user.messages:
            db.session.delete(message)
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for("users.index"))
    except ValidationError:
        return redirect(url_for("users.index"))
