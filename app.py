import os
from flask import Flask, render_template
from flask import Flask, render_template, request, redirect, url_for, flash, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
e = os.environ
app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql://{e["DB_USER"]}:{e["DB_PASSWORD"]}@{e["DB_HOST"]}/{e["DB_NAME"]}'
app.secret_key = e["APP_SECRET_KEY"]
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

from models.user import User  # noqa
from models.flight import Flight  # noqa


@app.route("/")
def home():
    username = request.cookies.get("username")
    if not username:
        return redirect(url_for("login"))
    return redirect(url_for("flights"))


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    username = request.form['username']
    user = User.query.filter_by(name=username).first()
    if user is None:
        user = User(name=username)
        db.session.add(user)
        db.session.commit()
    res = make_response(redirect("flights"))
    res.set_cookie("username", username)
    return res


@app.route("/logout")
def logout():
    res = make_response(redirect("login"))
    res.set_cookie("username", "", max_age=0)
    return res


@app.route("/flights")
def flights():
    flights = []
    search_query = request.args.get("search_flight")
    if not search_query:
        flights = Flight.query.all()
    else:
        search_flight = '%' + search_query + '%'
        flights = Flight.query.filter(or_(Flight.origin_airport.ilike(
            search_flight), Flight.destination_airport.ilike(search_flight))).all()
    return render_template("flights.html", flights=flights)


@app.route("/flight/<int:id>", methods=['GET', 'POST'])
def flight(id):
    flight = Flight.query.get(id)

    if request.method == "GET":
        return render_template('flight.html', flight=flight)

    requested_seats = int(request.form["flight_seats"])
    if requested_seats <= 0:
        flash({'title': 'Error',
               'body': 'You need to choose 1 or more seats'}, "red")
        return render_template("flight.html", flight=flight)

    if (flight.seats_left - requested_seats) >= 0:
        flight.taken_seats += requested_seats
        db.session.commit()
        flash({'title': 'Success!', 'body': 'You have done it!'}, "green")
    else:
        flash({'title': f'Seats left are smaller than what you have requested',
               'body': f'You have requested for {requested_seats} seats'}, "red")
    return redirect(url_for("flight", id=id))
