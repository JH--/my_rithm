from flask import Blueprint, redirect, render_template, request, url_for
from flask_wtf.csrf import validate_csrf, ValidationError
from project.departments.forms import NewDepartmentForm
from project.models import Department
from project import db

departments_blueprint = Blueprint("departments", __name__, template_folder="templates")


@departments_blueprint.route("/", methods=["GET"])
def index():
    return render_template("departments/index.html", departments=Department.query.all())


@departments_blueprint.route("/new", methods=["GET"])
def new():
    return render_template("departments/new.html", form=NewDepartmentForm())


@departments_blueprint.route("/", methods=["POST"])
def new_department():
    form = NewDepartmentForm(request.form)
    if form.validate():
        department = Department(request.form["name"])
        db.session.add(department)
        db.session.commit()
        return redirect(url_for("departments.index"))
    return redirect(url_for("departments.new"))


@departments_blueprint.route("/<int:id>", methods=["GET"])
def show(id):
    department = Department.query.get(id)
    if not department:
        return render_template("404.html")
    return render_template(
        "departments/show.html", department=department, employees=department.employees
    )


@departments_blueprint.route("/<int:id>", methods=["DELETE"])
def delete(id):
    try:
        validate_csrf(request.form.get("csrf_token"))
        db.session.delete(Department.query.get(id))
        db.session.commit()
    except ValidationError:
        pass
    finally:
        return redirect(url_for("departments.index"))


@departments_blueprint.route("/<int:id>/edit", methods=["GET"])
def edit(id):
    department = Department.query.get(id)
    if not department:
        return render_template("404.html")
    form = NewDepartmentForm(obj=department)
    return render_template("departments/edit.html", form=form, department=department)


@departments_blueprint.route("/<int:id>/edit", methods=["PATCH"])
def edit_department(id):
    form = NewDepartmentForm(request.form)
    if form.validate():
        department = Department.query.get(id)
        department.name = request.form["name"]
        db.session.commit()
    return redirect(url_for("departments.index"))

