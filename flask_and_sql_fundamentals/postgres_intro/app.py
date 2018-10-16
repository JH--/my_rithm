from flask import Flask, render_template, redirect, url_for, request
from flask_modus import Modus
import db

app = Flask(__name__)
modus = Modus(app)


@app.route("/")
def home():
    return redirect(url_for("index"))


@app.route("/toys", methods=["GET"])
def index():
    return render_template("index.html", toys=db.get_all_toys())


@app.route("/toys", methods=["POST"])
def add_toy():
    db.add_toy(request.form["name"])
    return redirect(url_for("index"))


@app.route("/toys/new")
def new_toy():
    return render_template("new.html")


@app.route("/toys/<int:id>", methods=["GET"])
def show_toy(id):
    toy = db.show_toy(id)
    return render_template("show.html", id=id, toy=toy)


@app.route("/toys/<int:id>", methods=["PATCH"])
def update_toy(id):
    new_name = request.form["name"]
    db.update_toy(id, new_name)
    return redirect(url_for("index"))


@app.route("/toys/<int:id>", methods=["DELETE"])
def delete_toy(id):
    db.delete_toy(id)
    return redirect(url_for("index"))


@app.route("/toys/<int:id>/edit")
def edit_toy(id):
    toy = db.show_toy(id)
    return render_template("edit.html", id=id, toy=toy)

