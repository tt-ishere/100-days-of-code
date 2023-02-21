import requests
import datetime
import os
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)


QUERY_TEXT = input("Tell me which exercises you did: ")
GENDER = "male"
WEIGHT_KG = 69.0
HEIGHT_CM = 190.00
AGE = 25

APP_ID = os.getenv("APP_ID")
APP_KEY = os.getenv("APP_KEY")

EXCERCISE_ENDPOINT = " https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = (
    "https://api.sheety.co/855aa867596ef604d9beceb244d5365d/myWorkouts/workouts"
)

HEADERS = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

PARAMS = {
    "query": QUERY_TEXT,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=EXCERCISE_ENDPOINT, json=PARAMS, headers=HEADERS)
response.raise_for_status()
result = response.json()

# formating date and time with strftime()
date = datetime.datetime.now()
today_date = f"{date.strftime('%x')}"
time = f"{date.strftime('%X')}"

sheety_auth = os.getenv("sheety_auth")
sheety_header = {"Content-Type": "application/json", "Authorization": sheety_auth}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheet_response = requests.post(
        SHEETY_ENDPOINT, json=sheet_inputs, headers=sheety_header
    )
    print(sheet_response.text)
