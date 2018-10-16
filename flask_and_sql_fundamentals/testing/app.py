from flask import Flask, redirect, url_for, request, render_template
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:///flask_testing"
modus = Modus(app)
db = SQLAlchemy(app)
Migrate(app, db)


class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"


@app.route("/")
def root():
    return redirect(url_for("index"))


@app.route("/students", methods=["GET"])
def index():
    return render_template("index.html", students=Student.query.all())


@app.route("/students", methods=["POST"])
def add_student():
    new_student = Student(request.form["first_name"], request.form["last_name"])
    db.session.add(new_student)
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/students/new")
def new():
    return render_template("new.html")


@app.route("/students/<int:id>/edit")
def edit(id):
    return render_template("edit.html", student=Student.query.get(id))


@app.route("/students/<int:id>", methods=["GET"])
def show_student(id):
    return render_template("show.html", student=Student.query.get(id))


@app.route("/students/<int:id>", methods=["PATCH"])
def edit_student(id):
    student = Student.query.get(id)
    student.first_name = request.form["first_name"]
    student.last_name = request.form["last_name"]
    db.session.add(student)
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    student = Student.query.get(id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for("index"))
