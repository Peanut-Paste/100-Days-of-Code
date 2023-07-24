from flight_search import FlightSearch
from data_manager import DataManager
from datetime import datetime, timedelta
from notification_manager import NotificationManager


FROM = "SIN"

flight_data = DataManager("prices")
flight = FlightSearch()
tele = NotificationManager()
email_data = DataManager("users")


now = datetime.now()
tomorrow = now + timedelta(days=1)
six_months = now + timedelta(days=180)


require_iataCode = [i for i in flight_data.data if i["iataCode"] == ""]
for i in require_iataCode:
    flight_data.edit_row("iataCode", i["id"], flight.get_iata_code(i["city"]))

for i in flight_data.data:
    flighta = (flight.get_flight_price(FROM, i["iataCode"], tomorrow, six_months))
    if flighta.price < i["lowestPrice"]:
        message = f"Low price alert! Only {flighta.price} to fly from " \
                  f"{flighta.departure_n}-{flighta.departure_code} to {flighta.arrival_n}-" \
                  f"{flighta.arrival_code}, from " \
                  f"{datetime.utcfromtimestamp(flighta.outbound_date).strftime('%d/%m/%Y')} " \
                  f"to {datetime.utcfromtimestamp(flighta.inbound_date).strftime('%d/%m/%Y')}"
        tele.message(message=message)
        for row in email_data.data:
            tele.email(row["email"], row["firstName"], message)


