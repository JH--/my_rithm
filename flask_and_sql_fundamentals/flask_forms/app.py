from flask import Flask, request, redirect, render_template, url_for, flash
from forms import SignupForm
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm(request.form)
    if request.method == "POST":
        if form.validate():
            flash("You have successfully signed up!")
            return redirect(url_for("welcome"))
    return render_template("signup.html", form=form)


@app.route("/welcome")
def welcome():
    return render_template("welcome.html")

