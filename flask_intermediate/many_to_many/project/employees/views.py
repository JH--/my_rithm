from flask import Blueprint, redirect, render_template, request, url_for
from project.models import Employee

employees_blueprint = Blueprint("employees", __name__, template_folder="templates")


@employees_blueprint.route("/", methods=["GET"])
def index():
    return render_template("employees/index.html", employees=Employee.query.all())
