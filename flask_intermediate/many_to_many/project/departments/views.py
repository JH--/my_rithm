from flask import Blueprint
from project.models import Department

departments_blueprint = Blueprint("departments", __name__, template_folder="templates")
