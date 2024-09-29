import requests
from datetime import datetime, time
import smtplib

MY_LAT = 6.944139 # Your latitude
MY_LONG = 122.075540 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": "Asia/Hong_Kong"
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = data["results"]["sunset"].split("T")[1]

time_now = str(datetime.now()).split(" ")[1]

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

time_now = time(hour = int(time_now.split(":")[0]),
                minute = int(time_now.split(":")[1]), 
                second = 0)
# time_now = time(18, 0, 0)

# iss_latitude = MY_LAT + -5
# iss_longitude = MY_LONG + -5

if time_now >= time(hour = int(sunset.split(":")[0]), 
                    minute = int(sunset.split(":")[1]),
                    second = 0):
    if abs(iss_latitude - MY_LAT) <= 5 and abs(iss_longitude - MY_LONG) <= 5:
        
        sender_email = "[SENDER_EMAIL]"
        sender_app_password = "[SENDER_APP_PASSWORD]"   
        
        with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
            connection.starttls()
            
            connection.login(user = sender_email, password = sender_app_password)
            connection.sendmail(from_addr = sender_email,
                                to_addrs = sender_email,
                                msg = "Subject:ISS Notification\n\nISS is above you right now!!!")
