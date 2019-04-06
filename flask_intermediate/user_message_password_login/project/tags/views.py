from flask import Blueprint, render_template, redirect, url_for, request
from flask_wtf.csrf import validate_csrf, ValidationError
from project.tags.forms import TagForm
from project.models import Tag, Message
from project import db

tags_blueprint = Blueprint("tags", __name__, template_folder="templates")


@tags_blueprint.route("/", methods=["GET"])
def index():
    return render_template("tags/index.html", tags=Tag.query.all())


@tags_blueprint.route("/new", methods=["GET"])
def new():
    form = TagForm()
    form.set_choices()
    return render_template("tags/new.html", form=form)


@tags_blueprint.route("/", methods=["POST"])
def new_tag():
    form = TagForm(request.form)
    form.set_choices()
    if form.validate():
        tag = Tag(request.form["tag"])
        messages = [Message.query.get(m) for m in form.messages.data]
        tag.messages.extend(messages)
        db.session.add(tag)
        db.session.commit()
        return redirect(url_for("tags.index"))
    return render_template("tags/new.html", form=form)


@tags_blueprint.route("/<int:id>", methods=["GET"])
def show(id):
    tag = Tag.query.get(id)
    if not tag:
        return render_template("404.html")
    return render_template("tags/show.html", tag=tag)


@tags_blueprint.route("/<int:id>/edit", methods=["GET"])
def edit(id):
    tag = Tag.query.get(id)
    if not tag:
        return render_template("404.html")
    messages = [m.id for m in tag.messages]
    form = TagForm(obj=tag)
    form.set_choices()
    form.messages.process_data(messages)
    return render_template("tags/edit.html", form=form, tag=tag)


@tags_blueprint.route("/<int:id>", methods=["PATCH"])
def edit_tag(id):
    form = TagForm(request.form)
    form.set_choices()
    if form.validate():
        tag = Tag.query.get(id)
        tag.tag = request.form["tag"]
        tag.messages = [Message.query.get(m) for m in form.messages.data]
        db.session.add(tag)
        db.session.commit()
    return redirect(url_for("tags.index"))


@tags_blueprint.route("/<int:id>", methods=["DELETE"])
def delete(id):
    try:
        validate_csrf(request.form.get("csrf_token"))
        tag = Tag.query.get(id)
        db.session.delete(tag)
        db.session.commit()
        return redirect(url_for("tags.index"))
    except ValidationError:
        return redirect(url_for("tags.index"))
