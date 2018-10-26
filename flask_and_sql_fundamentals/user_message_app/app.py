from flask import Flask, render_template, redirect, url_for, request
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect, validate_csrf, ValidationError
from re import search
from forms import UserForm
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:///flask_sqlalchemy_exercise"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
csrf = CSRFProtect(app)
modus = Modus(app)
db = SQLAlchemy(app)
Migrate(app, db)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    messages = db.relationship("Message", backref="User", lazy="dynamic")

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"


class Message(db.Model):
    __tablename__ = "messages"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return f"User: {self.user_id} Message: {self.content}\n"


def get_user_name(id):
    user = User.query.get(id)
    return f"{user.first_name} {user.last_name}"


@app.route("/")
def home():
    return redirect(url_for("index"))


@app.route("/messages", methods=["GET"])
def index():
    messages = Message.query.all()
    users = {m.user_id: get_user_name(m.user_id) for m in messages}
    return render_template("index.html", messages=messages, users=users)


@app.route("/messages/new/<int:user_id>")
def new_message(user_id):
    return render_template("new_message.html", user_id=user_id)


@app.route("/messages/<int:id>", methods=["GET"])
def show_message(id):
    return render_template("show_message.html", message=Message.query.get(id))


@app.route("/messages/<int:id>", methods=["DELETE"])
def delete_message(id):
    db.session.delete(Message.query.get(id))
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/messages/<int:id>", methods=["PATCH"])
def message_edit(id):
    message = Message.query.get(id)
    edit = request.form["message"]
    if search("[^ ]+", edit):
        message.content = edit
        db.session.add(message)
        db.session.commit()
    return redirect(url_for("show_user", id=message.user_id))


@app.route("/messages/<int:user_id>", methods=["POST"])
def add_message(user_id):
    message = request.form["message"]
    if search("[^ ]+", message):
        db.session.add(Message(message, user_id))
        db.session.commit()
    return redirect(url_for("index"))


@app.route("/messages/<int:id>/edit")
def edit_message(id):
    return render_template("edit_message.html", message=Message.query.get(id))


@app.route("/users", methods=["GET"])
def show_users():
    return render_template("users.html", users=User.query.all())


@app.route("/users", methods=["POST"])
def add_user():
    form = UserForm(request.form)
    if form.validate():
        first_name = form.data["first_name"]
        last_name = form.data["last_name"]
        db.session.add(User(first_name, last_name))
        db.session.commit()
        return redirect(url_for("show_users"))
    return redirect(url_for("new_user"))


@app.route("/users/new")
def new_user():
    form = UserForm(request.form)
    return render_template("new_user.html", form=form)


@app.route("/users/<int:id>", methods=["GET"])
def show_user(id):
    return render_template(
        "show_user.html",
        user=User.query.get(id),
        messages=Message.query.filter_by(user_id=id),
    )


@app.route("/users/<int:id>", methods=["PATCH"])
def edit_user(id):
    user = User.query.get(id)
    form = UserForm(request.form)
    if form.validate():
        user.first_name = form.data["first_name"]
        user.last_name = form.data["last_name"]
        db.session.add(user)
        db.session.commit()
    return redirect(url_for("show_users"))


@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):
    try:
        validate_csrf(request.form.get("csrf_token"))
        db.session.query(Message).filter(Message.user_id == id).delete(
            synchronize_session=False
        )
        db.session.delete(User.query.get(id))
        db.session.commit()
    except ValidationError:
        return redirect(url_for("show_uers"))
    return redirect(url_for("index"))


@app.route("/users/<int:id>/edit")
def edit(id):
    found_user = User.query.get(id)
    form = UserForm(obj=found_user)
    return render_template("edit_user.html", form=form, user=found_user)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

