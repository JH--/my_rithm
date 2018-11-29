from flask import Blueprint, render_template
from project.models import User

users_blueprint = Blueprint("users", __name__, template_folder="templates")


@users_blueprint.route("/", methods=["GET"])
def index():
    return render_template("index.html", users=User.query.all())

