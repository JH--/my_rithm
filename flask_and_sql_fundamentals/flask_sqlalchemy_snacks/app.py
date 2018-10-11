from flask import Flask, render_template, redirect, url_for, request
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:///flask_sqlalchemy_snacks"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
modus = Modus(app)
db = SQLAlchemy(app)


class Snack(db.Model):
    __tablename__ = "snacks"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    kind = db.Column(db.Text)

    def __init__(self, name, kind):
        self.name = name
        self.kind = kind

    def __repr__(self):
        return f"{self.kind} {self.name}"


@app.route("/")
def home():
    return redirect(url_for("index"))


@app.route("/snacks", methods=["GET"])
def index():
    return render_template("index.html", snacks=Snack.query.all())


@app.route("/snacks", methods=["POST"])
def add_snack():
    db.session.add(Snack(request.form["name"], request.form["kind"]))
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/snacks/new")
def new_snack():
    return render_template("new.html")


@app.route("/snacks/<int:id>", methods=["GET"])
def show_snack(id):
    snack = Snack.query.get(id)
    if not snack:
        return redirect(url_for("invalid"))
    return render_template("show.html", id=id, name=snack.name, kind=snack.kind)


@app.route("/snacks/<int:id>", methods=["PATCH"])
def update_snack(id):
    snack = Snack.query.get(id)
    snack.name = request.form["name"]
    snack.kind = request.form["kind"]
    db.session.add(snack)
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/snacks/<int:id>", methods=["DELETE"])
def delete_snack(id):
    db.session.delete(Snack.query.get(id))
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/snacks/<int:id>/<name>/<kind>")
def edit_snack(id, name, kind):
    return render_template("edit.html", id=id, name=name, kind=kind)


@app.route("/404")
def invalid():
    return render_template("invalid.html")
