from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello!"


@app.route("/hi")
def hi():
    return "Hi!"


@app.route("/bye")
def bye():
    return "Bye!"


@app.route("/name/<person>")
def say_name(person):
    return f"The name is {person}"


@app.route("/name/<int:num>")
def favorite_num(num):
    return f"Your favorite number is {num}, which is half of {num * 2}"


@app.route("/add/<int:num_a>/<int:num_b>")
def add(num_a, num_b):
    return f"{num_a + num_b}"


@app.route("/subtract/<int:num_a>/<int:num_b>")
def subtract(num_a, num_b):
    return f"{num_a - num_b}"


@app.route("/multiply/<int:num_a>/<int:num_b>")
def multiply(num_a, num_b):
    return f"{num_a * num_b}"


@app.route("/divide/<int:num_a>/<int:num_b>")
def divide(num_a, num_b):
    return f"{num_a / num_b}"
