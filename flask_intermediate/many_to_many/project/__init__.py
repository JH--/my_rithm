from flask import Flask, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_modus import Modus
from flask_wtf.csrf import CSRFProtect
from os import environ

app = Flask(__name__)
modus = Modus(app)
csrf = CSRFProtect(app)


app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:///many_to_many_example_sqlalchemy"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = environ.get("SECRET_KEY")
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from project.employees.views import employees_blueprint

app.register_blueprint(employees_blueprint, url_prefix="/employees")

from project.departments.views import departments_blueprint

app.register_blueprint(departments_blueprint, url_prefix="/departments")


def page_not_found(e):
    return render_template("404.html"), 404


app.register_error_handler(404, page_not_found)


@app.route("/")
def root():
    return redirect(url_for("employees.index"))

