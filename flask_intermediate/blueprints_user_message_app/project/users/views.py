from flask import Blueprint, render_template, redirect, url_for, request
from project.users.forms import UserForm
from project.models import User
from project import db

users_blueprint = Blueprint("users", __name__, template_folder="templates")


@users_blueprint.route("/", methods=["GET"])
def index():
    return render_template("index.html", users=User.query.all())


@users_blueprint.route("/", methods=["POST"])
def add_new_user():
    form = UserForm(request.form)
    if form.validate():
        db.session.add(User(request.form["first_name"], request.form["last_name"]))
        db.session.commit()
        return redirect(url_for("users.index"))
    return render_template("new.html", form=form)


@users_blueprint.route("/new", methods=["GET"])
def new():
    form = UserForm()
    return render_template("new.html", form=form)


@users_blueprint.route("/<int:id>/edit")
def edit(id):
    user = User.query.get(id)
    form = User(obj=owner)
    return render_template("edit.html", form=form, user=user)


@users_blueprint.route("/<int:id>", methods=["GET"])
def show(id):
    return render_template("show.html", user=User.query.get(id))

