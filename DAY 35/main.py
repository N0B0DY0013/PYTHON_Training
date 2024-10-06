import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

LATITUDE = os.getenv("ENV_LATITUDE")
LONGTITUDE = os.getenv("ENV_LONGTITUDE")
API_KEY = os.getenv("OPEN_WEATHER_API")

TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")
ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={LATITUDE}&lon={LONGTITUDE}&appid={API_KEY}&units=metric")
response.raise_for_status()

data = response.json()

weather_info = data["weather"][0]

if int(weather_info["id"]) <= 700:
    print("Bring an umbrella today! ☂️")
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    
    message = client.messages.create(
        body="Bring an umbrella today! ☂️",
        from_ = TWILIO_NUMBER,
        to = os.getenv("TWILIO_REG_NUMBER")
    )
else:
    print("Umbrella not needed today. ☀️")
