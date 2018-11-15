from flask import Flask, redirect, url_for
from flask_modus import Modus
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:///flask_sqlalchemy_exercise"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

csrf = CSRFProtect(app)
modus = Modus(app)
db = SQLAlchemy(app)
Migrate(app, db)

from project.users.views import users_blueprint
from project.messages.views import messages_blueprint

app.register_blueprint(users_blueprint, url_prefix="/users")
app.register_blueprint(messages_blueprint, url_prefix="/messages")


@app.route("/")
def root():
    return redirect(url_for("messages.index"))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

