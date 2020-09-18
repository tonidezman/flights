from app import db


class Flight(db.Model):
    __tablename__ = 'flights'
    id = db.Column(db.Integer, primary_key=True)
    flight_number = db.Column(db.String(250))
    origin_airport = db.Column(db.String(250))
    destination_airport = db.Column(db.String(250))
    carrier = db.Column(db.String(250))
    price = db.Column(db.Integer())
    day = db.Column(db.String(250))
    time = db.Column(db.String(250))
    duration = db.Column(db.String(250))
    available_seats = db.Column(db.Integer())
    taken_seats = db.Column(db.Integer(), default=0)

    @property
    def is_available(self):
        return self.taken_seats < self.available_seats
