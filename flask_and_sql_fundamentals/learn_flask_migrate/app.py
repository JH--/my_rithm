from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:///learn_flask_migrate"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
Migrate(app, db)


class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    excuses = db.relationship("Excuse", backref="Student", lazy="dynamic")

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f"The student's name is {self.first_name} {self.last_name}"


class Excuse(db.Model):
    __tablename__ = "excuses"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    is_believable = db.Column(db.Boolean)
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"))

    def __init__(self, name, is_believable, student_id):
        self.name = name
        self.is_believable = is_believable
        self.student_id = student_id
