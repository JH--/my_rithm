from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:///flask_json"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
Migrate(app, db)


class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    author = db.Column(db.Text)

    def __init__(self, title, author):
        self.title = title
        self.author = author


@app.route("/", methods=["GET"])
def index():
    return jsonify(
        [
            {"id": book.id, "author": book.author, "title": book.title}
            for book in Book.query.all()
        ]
    )


@app.route("/", methods=["POST"])
def add_book():
    new_book = Book(author=request.json["author"], title=request.json["title"])
    db.session.add(new_book)
    db.session.commit()
    return jsonify(
        {"id": new_book.id, "author": new_book.author, "title": new_book.title}
    )
