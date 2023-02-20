import requests
from _datetime import datetime

MY_LAT = 5.603717
MY_LNG = -0.186964

# iss location
# response = requests.get("http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# data = response.json()
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
# print(iss_position)
parameters = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted': 0,
}

response = requests.get("http://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
sunset = data['results']['sunset'].split('T')[1].split(':')[0]
print(sunset)

time_now = datetime.now().hour
print(time_now)

