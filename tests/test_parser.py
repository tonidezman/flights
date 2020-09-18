from services.parser import Parser

FIRST_FLIGHT = {'flight_number': 'SA001',
                'origin_airport': 'SFO',
                'destination_airport': 'DEN',
                'carrier': 'SpeedyAir',
                'price': '400',
                'day': 'Sun',
                'time': '13:40',
                'duration': '20m',
                'available_seats': '50'}


def test_parse_one_line():
    cols = ["flight_number", "origin_airport", "destination_airport",
            "carrier", "price", "day", "time", "duration", "available_seats"]

    parser = Parser(file="tests/one_line.txt", header=cols)
    expected = [FIRST_FLIGHT]
    assert parser.run() == expected


def test_parse_multiple_lines():
    cols = ["flight_number", "origin_airport", "destination_airport",
            "carrier", "price", "day", "time", "duration", "available_seats"]

    parser = Parser(file="tests/multiple_lines.txt", header=cols)
    actual = parser.run()
    assert len(actual) == 3
    assert actual[0] == FIRST_FLIGHT
