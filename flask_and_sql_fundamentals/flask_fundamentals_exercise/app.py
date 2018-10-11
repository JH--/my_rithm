from flask import Flask, render_template, redirect, url_for, request
from flask_modus import Modus
from snack import Snack


# Flask CRUD
# For this application you will be building CRUD on the resouce snacks.
# Your application should:
#
# display all the snacks
# allow a user to create snacks
# each snack should have a name and kind
# allow a user to edit a snack
# allow a user to delete a snack
# You should use a list to store your snacks and make a class for a
# snack to create instances from.
#
# BONUS Make your app look amazing with some CSS! BONUS If you go to
# the show page for an invalid id, your applicaiton will break. Create
# a 404 page and redirect to it in the event that a user tries to go to
# the show or edit pages for a snack with an invalid id.
#

app = Flask(__name__)
modus = Modus(app)

snacks = [
    Snack("Potato Chips", "Jose Andres"),
    Snack("Chocolate Chip Cookies", "Bi-Rite"),
    Snack("Chicharrones", "4505"),
]


def find_snack(id, snacks):
    try:
        return next(snack for snack in snacks if snack.id == id)
    except StopIteration:
        return


@app.route("/")
def root():
    return redirect(url_for("index"))


@app.route("/snacks", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        snacks.append(Snack(request.form["name"], request.form["kind"]))
        return redirect(url_for("index"))

    return render_template("index.html", snacks=snacks)


@app.route("/snacks/new")
def new():
    return render_template("new.html")


@app.route("/snacks/<int:id>", methods=["GET", "PATCH", "DELETE"])
def show(id):
    snack = find_snack(id, snacks)
    if not snack:
        return redirect(url_for("invalid"))

    if request.method == b"PATCH":
        snack.name = request.form["name"]
        snack.kind = request.form["kind"]
        return redirect(url_for("index"))

    if request.method == b"DELETE":
        snacks.remove(snack)
        return redirect(url_for("index"))

    return render_template("show.html", snack=snack)


@app.route("/snacks/<int:id>/edit")
def edit(id):
    snack = find_snack(id, snacks)
    if not snack:
        return redirect(url_for("invalid"))

    return render_template("edit.html", snack=snack)


@app.route("/404")
def invalid():
    return render_template("invalid.html")
