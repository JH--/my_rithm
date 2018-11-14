from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
import os

app = Flask(__name__)
csrf = CSRFProtect(app)
modus = Modus(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:///flask_blueprints"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")  # "THIS SHOULD BE HIDDEN!"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# import a blueprint that we will create
from project.owners.views import owners_blueprint

# register our blueprints with the application
app.register_blueprint(owners_blueprint, url_prefix="/owners")


@app.route("/")
def root():
    return "HELLO BLUEPRINTS!"
