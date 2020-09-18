from services.parser import Parser
from app import db
from models.flight import Flight

cols = ["flight_number", "origin_airport", "destination_airport",
        "carrier", "price", "day", "time", "duration", "available_seats"]
flights = Parser(file="scripts/flights.txt", header=cols).run()

for flight in flights:
    db.session.add(Flight(**flight))

db.session.commit()
