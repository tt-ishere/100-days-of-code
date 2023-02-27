import requests

SHEETY_ENDPOINT = (
    "https://api.sheety.co/855aa867596ef604d9beceb244d5365d/flightDeals/prices"
)


# This class is responsible for talking to the Google Sheet.
class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(SHEETY_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]

        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {"price": {"iataCode": city["iataCode"]}}
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data
            )
            print(response.text)
