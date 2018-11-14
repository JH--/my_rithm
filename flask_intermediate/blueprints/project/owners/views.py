from flask import Blueprint, redirect, render_template, request, url_for
from flask_wtf.csrf import validate_csrf, ValidationError
from project.models import Owner
from project.owners.forms import OwnerForm
from project import db

# let's create the owners_blueprint to register in our __init__.py
owners_blueprint = Blueprint("owners", __name__, template_folder="templates")


@owners_blueprint.route("/", methods=["GET"])
def index():
    return render_template("index.html", owners=Owner.query.all())


@owners_blueprint.route("/new")
def new():
    form = OwnerForm()
    return render_template("new.html", form=form)


@owners_blueprint.route("/", methods=["POST"])
def add_owner():
    form = OwnerForm(request.form)
    if form.validate():
        new_owner = Owner(request.form["first_name"], request.form["last_name"])
        db.session.add(new_owner)
        db.session.commit()
        return redirect(url_for("owners.index"))
    return render_template("new.html", form=form)


@owners_blueprint.route("/<int:id>/edit")
def edit(id):
    owner = Owner.query.get(id)
    form = OwnerForm(obj=owner)
    return render_template("edit.html", form=form, owner=owner)


@owners_blueprint.route("/<int:id>", methods=["PATCH"])
def edit_owner(id):
    found_owner = Owner.query.get(id)
    form = OwnerForm(request.form)
    if form.validate():
        found_owner.first_name = request.form["first_name"]
        found_owner.last_name = request.form["last_name"]
        db.session.add(found_owner)
        db.session.commit()
        return redirect(url_for("owners.index"))
    return render_template("edit.html", form=form, owner=found_owner)


@owners_blueprint.route("/<int:id>", methods=["DELETE"])
def delete(id):
    found_owner = Owner.query.get(id)
    try:
        validate_csrf(request.form.get("csrf_token"))
        db.session.delete(found_owner)
        db.session.commit()
        return redirect(url_for("owners.index"))
    except ValidationError:
        return render_template("owners.show.html", owner=found_owner)


@owners_blueprint.route("/<int:id>", methods=["GET"])
def show(id):
    found_owner = Owner.query.get(id)
    return render_template("show.html", owner=found_owner)

