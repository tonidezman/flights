import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
e = os.environ
app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql://{e["DB_USER"]}:{e["DB_PASSWORD"]}@{e["DB_HOST"]}/{e["DB_NAME"]}'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


@app.route("/")
def home():
    return "home page"


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/flights")
def flights():
    return render_template("flights.html")


@app.route("/flight")
def flight():
    svg = "./static/plane.svg"
    return render_template("flight.html", svg=svg)
