import requests
from datetime import datetime, timezone
import smtplib
import time

MY_EMAIL = "Isaac.cTD@gmail.com"
PASSWORD = "dzauofhghfisuica"

MY_LAT = 1.342784
MY_LONG = 103.706827

def check_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG + 6:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now_UTC = datetime.now(timezone.utc).hour

    if time_now_UTC >= sunset or time_now_UTC <= sunrise:
        return True


while True:
    time.sleep(60)
    if check_position() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject: Look up!!!\n\nThe ISS is passing over you at this moment now!"
                )




