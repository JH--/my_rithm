from flask import Flask, render_template, redirect, url_for, request
from flask_modus import Modus
from toy import Toy

app = Flask(__name__)
modus = Modus(app)

duplo = Toy(name="duplo")
lego = Toy(name="lego")
knex = Toy(name="knex")

toys = [duplo, lego, knex]


@app.route("/toys", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        toys.append(Toy(request.form["name"]))
        return redirect(url_for("index"))

    return render_template("index.html", toys=toys)


@app.route("/toys/new")
def new():
    return render_template("new.html")


@app.route("/toys/<int:id>", methods=["GET", "PATCH", "DELETE"])
def show(id):
    found_toy = next(toy for toy in toys if toy.id == id)

    if request.method == b"PATCH":
        found_toy.name = request.form["name"]
        return redirect(url_for("index"))

    if request.method == b"DELETE":
        toys.remove(found_toy)
        return redirect(url_for("index"))

    return render_template("show.html", toy=found_toy)


@app.route("/toys/<int:id>/edit")
def edit(id):
    found_toy = next(toy for toy in toys if toy.id == id)
    return render_template("edit.html", toy=found_toy)

