from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/name")
def welcome():
    return "Welcome to our application!"
