import dotenv
import os

dotenv.load_dotenv()

SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
SHEETY_BEARER_TOKEN = os.getenv("SHEETY_BEARER_TOKEN")
SHEETY_PROJECT_NAME = "flightDealsProject"
SHEETY_SHEET_NAME = "prices"
X_RAPIDAPI_HOST = "sky-scanner3.p.rapidapi.com"
X_RAPIDAPI_KEY = os.getenv("X_RAPIDAPI_KEY")