# This file will need to use the DataManager,FlightSearch, FlightData, Notification Manager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()


flight_search = FlightSearch()


# Get iata codes for destinations
if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

origin_city = "LON"
for destination in sheet_data:
    flight_data = flight_search.check_flights(origin_city, destination["iataCode"])
    try:
        if destination["lowestPrice"] > flight_data.price:
            notification_manager = NotificationManager()
            sms = f"Low price alert! Only {flight_data.price} to fly from {flight_data.origin_city}-{flight_data.origin_airport} to {flight_data.destination_city}-{flight_data.destination_airpot}, from {flight_data.flight_date} to {flight_data.return_flight_date}"
            notification_manager.send_sms(sms)
    except AttributeError:
        None
