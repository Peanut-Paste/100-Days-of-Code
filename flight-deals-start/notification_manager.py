import requests
import smtplib

URL = f"https://api.telegram.org/bot6074336092:AAFUor0YoetJ4q0Nt4wyRR83-pmcg2prqZw/sendMessage"

MY_EMAIL = "isaac.ctd@gmail.com"
PASSWORD = "dzauofhghfisuica"


class NotificationManager:
    def message(self, message):
        parameter = {
            "chat_id": 740295348,
            "text": message
        }
        requests.get(URL, params=parameter)

    def email(self, email, firstname, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=email,
                                msg=f"Subject:Cheap Flight! \n\nHey {firstname}, \n"
                                    f"{message}.")

