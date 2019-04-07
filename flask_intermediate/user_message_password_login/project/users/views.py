from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
    flash,
    session,
    g,
)
from flask_wtf.csrf import validate_csrf, ValidationError
from project.users.forms import UserForm, LoginForm
from project.models import User
from project import db, bcrypt
from sqlalchemy.exc import IntegrityError
from project.decorators import (
    ensure_authenticated,
    prevent_double_login,
    ensure_correct_user,
)

users_blueprint = Blueprint("users", __name__, template_folder="templates")


@users_blueprint.before_request
def current_user():
    if session.get("user_id"):
        g.current_user = User.query.get(session["user_id"])
    else:
        g.current_user = None


@users_blueprint.route("/", methods=["GET"])
@ensure_authenticated
def index():
    return render_template("users/index.html", users=User.query.all())


@users_blueprint.route("/new", methods=["GET"])
@prevent_double_login
def new():
    form = UserForm()
    return render_template("users/new.html", form=form)


@users_blueprint.route("/", methods=["POST"])
@prevent_double_login
def new_user():
    form = UserForm(request.form)
    if form.validate():
        try:
            new_user = User(
                form.first_name.data,
                form.last_name.data,
                form.user_name.data,
                form.password.data,
            )
            db.session.add(new_user)
            db.session.commit()
            session["user_id"] = new_user.id
            flash("User Created!")
            return redirect(url_for("users.show", id=new_user.id))
        except IntegrityError:
            flash("Username already taken!")
    return render_template("users/new.html", form=form)


@users_blueprint.route("/login", methods=["GET"])
@prevent_double_login
def login():
    form = LoginForm()
    return render_template("users/login.html", form=form)


@users_blueprint.route("/login", methods=["POST"])
@prevent_double_login
def login_user():
    form = LoginForm(request.form)
    if form.validate():
        authenticated_user = User.authenticate(form.user_name.data, form.password.data)
        if authenticated_user:
            session["user_id"] = authenticated_user.id
            return redirect(url_for("users.show", id=authenticated_user.id))
        else:
            flash("Invalid Credentials!")
    return render_template("users/login.html", form=form)


@users_blueprint.route("/<int:id>", methods=["GET"])
@ensure_authenticated
@ensure_correct_user
def show(id):
    user = User.query.get(id)
    if not user:
        return render_template("404.html")
    return render_template("users/show.html", user=user, messages=user.messages)


@users_blueprint.route("/<int:id>/edit", methods=["GET"])
@ensure_authenticated
@ensure_correct_user
def edit(id):
    user = User.query.get(id)
    if not user:
        return render_template("404.html")
    form = UserForm(obj=user)
    return render_template("users/edit.html", form=form, user=user)


@users_blueprint.route("/<int:id>", methods=["PATCH"])
@ensure_authenticated
@ensure_correct_user
def edit_user(id):
    form = UserForm(request.form)
    if form.validate():
        user = User.query.get(id)
        user.first_name = request.form["first_name"]
        user.last_name = request.form["last_name"]
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("users.index"))
    return render_template("users/show.html", user=user)


@users_blueprint.route("/<int:id>", methods=["DELETE"])
@ensure_authenticated
@ensure_correct_user
def delete(id):
    try:
        validate_csrf(request.form.get("csrf_token"))
        user = User.query.get(id)
        for message in user.messages:
            db.session.delete(message)
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for("users.index"))
    except ValidationError:
        return redirect(url_for("users.index"))


@users_blueprint.route("/logout", methods=["GET"])
@ensure_authenticated
def logout():
    session.pop("user_id")
    flash("Logged out!")
    return redirect(url_for("users.login"))

