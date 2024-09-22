##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import smtplib
import pandas
import datetime as dt
import random
import os

bday_data = pandas.read_csv("birthdays.csv")

for (index, row_series) in bday_data.iterrows():

    if row_series["month"] == dt.datetime.now().month and row_series["day"] == dt.datetime.now().day:
        
        email_content = ""
        with open(f"letter_templates\{random.choice(os.listdir('letter_templates'))}", mode = "r") as letter:
            email_content = letter.read().replace("[NAME]", row_series["name"])
                    
        with smtplib.SMTP("smtp.gmail.com", port = 587) as conn:
            
            sender_email = "[SENDER_EMAIL]"
            sender_app_password = "[SENDER_APP_PASSWORD]"
            
            conn.starttls()
            conn.login(user = sender_email, password = sender_app_password)
            conn.sendmail(from_addr = sender_email,
                          to_addrs = sender_email,
                          msg = f"Subject: Happy Burtday!\n\n{email_content}")
            