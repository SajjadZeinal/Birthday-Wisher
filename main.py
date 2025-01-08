##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

import smtplib
import datetime as dt
import random
import pandas as pd
import csv

today = dt.date.today().day
this_month = dt.date.today().month
my_email = "udemytest1993@gmail.com"
password = "pass"

birthday_data = pd.read_csv("birthdays.csv")

with open("birthdays.csv", "r") as file:
    csv_reader = csv.DictReader(file)
    data = [row for row in csv_reader]

letter_templates = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

for row in data:
    if int(row["month"]) == this_month and int(row["day"]) == today:
        letter_file = random.choice(letter_templates)
        file_path = rf"letter_templates\{letter_file}"

        with open(file_path, "r") as letter:
            text = letter.read()
            new_text = text.replace("[NAME]", row["name"])

        print(new_text)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # Make this connection secure
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=row["email"],
                msg=f"Subject:Happy Birthday\n\n {new_text}"
            )

