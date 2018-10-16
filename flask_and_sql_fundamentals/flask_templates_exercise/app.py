from flask import Flask, render_template, request
from urllib import request as url_request
from re import search
import bs4

app = Flask(__name__)


# Flask Templating
# Create a new Flask application with the following:
#
# Part 1
# A base.html template for others to inherit from
# A route for /person/<name>/<age> which renders a
# template that displays the name and age entered
# for the URL. That template should inherit from
# base.html


@app.route("/person/<name>/<age>")
def display_person(name, age):
    return render_template("person.html", name=name, age=age)


# Part 2
# Refactor your calculator application from before!
#
# have a route for /calculate which renders a
# template called calc.html
# in calc.html, build a form which has two inputs
# (one with a name of num1 and another with the name
# of num2for numbers and a select field with the name
# of calculation with options for "add", "subtract",
# "multiply" and "divide".
# When the form is submitted it should make a request
# to a route called /math
# In your python file, accept the values from the form
# and depending on what the request contains, respond
# with the sum, difference, product or quotient.


@app.route("/calculate")
def show_calculator():
    return render_template("calc.html")


@app.route("/math")
def calculator():
    num1 = int(request.args.get("num1"))
    num2 = int(request.args.get("num2"))
    calculation = request.args.get("calculation")
    if calculation == "add":
        return f"{num1 + num2}"
    if calculation == "subtract":
        return f"{num1 - num2}"
    if calculation == "multiply":
        return f"{num1 * num2}"
    if calculation == "divide":
        return f"{num1 / num2}"


# Part 3
# Create a small application which grabs headlines
# from Google News by keyword. (This application is
# based on the Google News web scraper from the web
# scraping exercises.)
#
# This application should consist of two routes,
# / and /results
# When the server receives a request to /, it should
# render an HTML page with a form prompting the user
# for a keyword (e.g. "California"). Submitting the
# form should result in a request to /results, with
# the form input passed in the query string.
# When the server receives a request to /results, it
# should do the following:
# Grab the keyword from the query string;
# Make a request to https://news.google.com, and scrape
# the respose HTML for all news articles (links and
# headlines);
# Filter out articles whose headlines do not match the
# keyword passed in from the query string;
# Render an HTML page with matching articles (links and
# headlines) in a list.
#
def query_search(headline, query):
    if not query:
        return True
    for word in query:
        if not search(word.lower(), headline.text.lower()):
            return
    return True


@app.route("/")
def search_form():
    return render_template("search.html")


@app.route("/results")
def search_results():
    query = request.args.get("query").strip().split()
    news = url_request.urlopen("https://news.google.com").read()
    soup = bs4.BeautifulSoup(news, "html.parser")
    headlines = [
        h for h in soup.select("article a") if h.text and "articles" in h["href"]
    ]
    result = filter(lambda line: query_search(line, query), headlines)
    return render_template("results.html", headlines=result)
