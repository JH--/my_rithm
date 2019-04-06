from flask import Flask, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt
import os


app = Flask(__name__)
bcrypt = Bcrypt(app)
modus = Modus(app)
csrf = CSRFProtect(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:///user_messages"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from project.users.views import users_blueprint

app.register_blueprint(users_blueprint, url_prefix="/users")

from project.messages.views import messages_blueprint

app.register_blueprint(messages_blueprint, url_prefix="/messages")

from project.tags.views import tags_blueprint

app.register_blueprint(tags_blueprint, url_prefix="/tags")


def page_not_found(e):
    return render_template("404.html"), 404


app.register_error_handler(404, page_not_found)


@app.route("/")
def root():
    return redirect(url_for("messages.index"))
