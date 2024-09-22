import smtplib
import datetime as dt
import random

sender_email = "[SENDER_EMAIL]"
sender_app_password = "[SENDER_APP_PASSWORD]"

quotes = []

with open("quotes.txt", mode = "r") as file:
    quotes = file.readlines()

with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
    connection.starttls()

    connection.login(user = sender_email, password = sender_app_password)
    connection.sendmail(from_addr = sender_email, 
                        to_addrs = sender_email, 
                        msg = f"Subject:{dt.datetime.now().strftime('%A')} Motivation\n\n{random.choice(quotes)}")

