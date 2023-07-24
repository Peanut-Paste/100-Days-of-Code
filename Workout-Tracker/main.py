import requests
from datetime import datetime
import os

APP_ID = os.environ.get("NUTRI_API_ID")
API_KEY = os.environ.get("NUTRI_API_KEY")
NUTRITIONX_URL = "https://trackapi.nutritionix.com"
EXERCISE_ENDPOINT_URL = "/v2/natural/exercise"
SHEETY_URL = "https://api.sheety.co/b9ee8ce6bdb18e42b20524d1e8093966/myWorkouts/workouts"

sheety_header = {
    "Authorization": os.environ.get("SHEETY_BEARER")
}


now = datetime.now()

nutri_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

u_input = input("Tell me which exercise you did: ")

exercise_params = {
    "query": u_input
}

nutritionx_response = requests.post(NUTRITIONX_URL + EXERCISE_ENDPOINT_URL, json=exercise_params, headers=nutri_headers)

for i in nutritionx_response.json()["exercises"]:
    duration = str(i["duration_min"])
    exercise = str(i["name"].title())
    calories = str(i["nf_calories"])

    sheety_params = {
        "workout": {
            "date": now.strftime("%d/%m/%Y"),
            "time": now.strftime("%H:%M"),
            "exercise": exercise,
            "duration": duration,
            "calories": calories,
        }
    }

    sheety_response = requests.post(SHEETY_URL, json=sheety_params, headers=sheety_header)

