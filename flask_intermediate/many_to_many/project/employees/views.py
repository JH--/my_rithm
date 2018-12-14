from flask import Blueprint, redirect, render_template, request, url_for
from flask_wtf.csrf import validate_csrf, ValidationError
from project.employees.forms import NewEmployeeForm
from project.models import Employee, Department
from project import db

employees_blueprint = Blueprint("employees", __name__, template_folder="templates")


@employees_blueprint.route("/", methods=["GET"])
def index():
    return render_template("employees/index.html", employees=Employee.query.all())


@employees_blueprint.route("/new", methods=["GET"])
def new():
    form = NewEmployeeForm()
    form.set_choices()
    return render_template("employees/new.html", form=form)


@employees_blueprint.route("/", methods=["POST"])
def new_employee():
    form = NewEmployeeForm(request.form)
    form.set_choices()
    if form.validate():
        employee = Employee(request.form["name"], request.form["years_at_company"])
        db.session.add(employee)
        for department in form.departments.data:
            d = Department.query.get(department)
            d.employees.extend([employee])
        db.session.commit()
        return redirect(url_for("employees.index"))
    return redirect(url_for("employees.new"))


@employees_blueprint.route("/<int:id>", methods=["GET"])
def show(id):
    employee = Employee.query.get(id)
    if not employee:
        return render_template("404.html")
    return render_template(
        "employees/show.html", employee=employee, departments=employee.departments
    )


@employees_blueprint.route("/<int:id>/edit", methods=["GET"])
def edit(id):
    employee = Employee.query.get(id)
    if not employee:
        return render_template("404.html")
    form = NewEmployeeForm(obj=employee)
    form.set_choices()
    return render_template("employees/edit.html", form=form, employee=employee)


@employees_blueprint.route("/<int:id>", methods=["PATCH"])
def edit_employee(id):
    form = NewEmployeeForm(request.form)
    form.set_choices()
    if form.validate():
        employee = Employee.query.get(id)
        employee.name = request.form['name']
        employee.years_at_company = request.form['years_at_company']
        for department in employee.departments:
            employee.departments.remove(department)
        for department in form.departments.data:
            d = Department.query.get(department)
            d.employees.extend([employee])
        db.session.commit()
    return redirect(url_for('employees.index'))