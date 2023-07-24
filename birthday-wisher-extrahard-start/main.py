import pandas
import datetime as df
import smtplib
import random

myemail = "isaac.ctd@gmail.com"
password = "dzauofhghfisuica"


# ------------- Extra Hard Starting Project ----------------#
# 2. Check if today matches a birthday in the birthdays.csv
bd_df = pandas.read_csv("birthdays.csv")
now = df.datetime.now()
day = now.day
month = now.month

for (index, row) in bd_df.iterrows():
    if row.day == day and row.month == month:
        with open(f"./letter_templates/letter_{random.randint(1,3)}.txt") as letter:
            letter_tem = letter.read()
            formatted_tem = letter_tem.replace("[NAME]", row.names)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=myemail, password=password)
            connection.sendmail(
                from_addr=myemail,
                to_addrs=row.email,
                msg=f"Subject: Happy Birthday, {row.names}!\n\n{formatted_tem}")
