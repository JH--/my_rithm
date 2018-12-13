from flask import Flask, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:///many_to_many_example_sqlalchemy"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from project.employees.views import employees_blueprint

app.register_blueprint(employees_blueprint, url_prefix="/employees")

from project.departments.views import departments_blueprint

app.register_blueprint(departments_blueprint, url_prefix="/departments")


@app.route("/")
def root():
    return redirect(url_for("employees.index"))

