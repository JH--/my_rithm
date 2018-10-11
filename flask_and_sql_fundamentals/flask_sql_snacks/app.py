from flask import Flask, render_template, redirect, url_for, request
from flask_modus import Modus
import db

app = Flask(__name__)
modus = Modus(app)


@app.route("/")
def home():
    return redirect(url_for("index"))


@app.route("/snacks", methods=["GET"])
def index():
    return render_template("index.html", snacks=db.get_all_snacks())


@app.route("/snacks", methods=["POST"])
def add_snack():
    db.add_snack(request.form["name"], request.form["kind"])
    return redirect(url_for("index"))


@app.route("/snacks/new")
def new_snack():
    return render_template("new.html")


@app.route("/snacks/<int:id>", methods=["GET"])
def show_snack(id):
    snack = db.show_snack(id)
    if not snack:
        return redirect(url_for("invalid"))
    return render_template("show.html", id=id, name=snack[1], kind=snack[2])


@app.route("/snacks/<int:id>", methods=["PATCH"])
def update_snack(id):
    new_name, new_kind = request.form["name"], request.form["kind"]
    db.update_snack(id, new_name, new_kind)
    return redirect(url_for("index"))


@app.route("/snacks/<int:id>", methods=["DELETE"])
def delete_snack(id):
    db.delete_snack(id)
    return redirect(url_for("index"))


@app.route("/snacks/<int:id>/<name>/<kind>")
def edit_snack(id, name, kind):
    return render_template("edit.html", id=id, name=name, kind=kind)


@app.route("/404")
def invalid():
    return render_template("invalid.html")
