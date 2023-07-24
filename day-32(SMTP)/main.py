import smtplib
import datetime as dt
import random

my_email = "Isaac.cTD@gmail.com"
password = "dzauofhghfisuica"

now = dt.datetime.now()
day_of_the_week = now.weekday()
if day_of_the_week == 2:
    with open("quotes.txt", mode="r") as quotes:
        quote_list = quotes.readlines()
        chosen_quote = random.choice(quote_list)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="isaac.ctd@myyahoo.com",
            msg=f"Subject:Quote of the day\n\n{chosen_quote}"
        )
