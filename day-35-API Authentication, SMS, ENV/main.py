import pandas as pd
import os
import requests
import smtplib

Base_URL = "http://api.weatherapi.com/v1"
API = "/forecast.json"
api_key = "4d1bf61714b9463ea27112113230704"
my_lat = 1.352083
my_lon = 103.819839
MY_EMAIL = "isaac.ctd@gmail.com"
PASSWORD = "dzauofhghfisuica"


parameters = {
    "key": api_key,
    "q": f"{my_lat},{my_lon}",
    "aqi": "no",
    "tp": 15,
}

response = requests.get(Base_URL+API, params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False

forecast_slice = data["forecast"]["forecastday"][0]["hour"][7:20]

for hour_data in forecast_slice:
    condition_code = hour_data["condition"]["code"]
    if condition_code > 1063:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject: Reminder: To bring umbrella\n\nIt is going to rain."
        )

